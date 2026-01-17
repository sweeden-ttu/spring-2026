#!/usr/bin/env python3
"""
Download lecture materials from Canvas LMS for Spring 2026 courses.

This script:
1. Fetches module items for each course
2. Downloads files for recent lectures
3. Extracts metadata and creates YAML data files
4. Organizes files in date-based folders
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
from urllib.parse import urlparse
import asyncio

# Add canvas-lms-mcp to path
canvas_mcp_path = Path(__file__).parent.parent.parent / "canvas-lms-mcp"
sys.path.insert(0, str(canvas_mcp_path))

import httpx
from config import load_env_config, get_api_headers

# Course configuration
COURSES = {
    "software-verification": {
        "canvas_id": 70713,
        "course_slug": "software-verification",
        "modules": [811245, 811248, 813151]  # From previous fetch
    },
    "cryptography": {
        "canvas_id": 70714,
        "course_slug": "cryptography",
        "modules": []  # To be fetched
    }
}

async def get_file_download_url(client, file_id, course_id=None):
    """Get download URL for a file."""
    try:
        if course_id:
            url = f"/api/v1/courses/{course_id}/files/{file_id}/public_url"
        else:
            url = f"/api/v1/files/{file_id}/public_url"
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error getting download URL for file {file_id}: {e}", file=sys.stderr)
        return None

async def download_file(client, url, output_path):
    """Download a file from URL."""
    try:
        response = await client.get(url, follow_redirects=True)
        response.raise_for_status()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'wb') as f:
            f.write(response.content)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}", file=sys.stderr)
        return False

async def fetch_module_items(course_id, module_id):
    """Fetch items from a module."""
    config = load_env_config()
    headers = get_api_headers(config.api_token)
    
    async with httpx.AsyncClient(
        base_url=config.base_url,
        headers=headers,
        timeout=60.0
    ) as client:
        try:
            response = await client.get(
                f"/api/v1/courses/{course_id}/modules/{module_id}/items",
                params={"per_page": 100, "include": ["content_details"]}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching module {module_id}: {e}", file=sys.stderr)
            return []

async def get_file_metadata(client, file_id, course_id=None):
    """Get file metadata."""
    try:
        if course_id:
            url = f"/api/v1/courses/{course_id}/files/{file_id}"
        else:
            url = f"/api/v1/files/{file_id}"
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error getting file metadata {file_id}: {e}", file=sys.stderr)
        return None

async def process_course(course_slug, course_config):
    """Process a course and download materials."""
    config = load_env_config()
    headers = get_api_headers(config.api_token)
    course_id = course_config["canvas_id"]
    
    base_path = Path(__file__).parent / course_slug
    lectures_path = base_path / "_lectures"
    data_path = base_path / "_data"
    data_path.mkdir(parents=True, exist_ok=True)
    
    all_lectures_data = []
    
    async with httpx.AsyncClient(
        base_url=config.base_url,
        headers=headers,
        timeout=60.0
    ) as client:
        # Get modules if not provided
        if not course_config.get("modules"):
            modules_resp = await client.get(
                f"/api/v1/courses/{course_id}/modules",
                params={"per_page": 100}
            )
            if modules_resp.status_code == 200:
                modules = modules_resp.json()
                course_config["modules"] = [m["id"] for m in modules]
        
        # Process each module
        for module_id in course_config["modules"]:
            print(f"\nProcessing module {module_id}...")
            items = await fetch_module_items(course_id, module_id)
            
            for item in items:
                if item.get("type") == "File" and item.get("content_id"):
                    file_id = item["content_id"]
                    
                    # Get file metadata
                    file_meta = await get_file_metadata(client, file_id, course_id)
                    if not file_meta:
                        continue
                    
                    # Get download URL
                    download_info = await get_file_download_url(client, file_id, course_id)
                    if not download_info:
                        continue
                    
                    # Determine lecture date from module or file name
                    # For now, use current date or extract from module name
                    lecture_date = datetime.now().strftime("%Y-%m-%d")
                    lecture_folder = lectures_path / f"lecture-{lecture_date}"
                    lecture_folder.mkdir(parents=True, exist_ok=True)
                    
                    # Create subdirectories
                    (lecture_folder / "canvas").mkdir(exist_ok=True)
                    (lecture_folder / "notes").mkdir(exist_ok=True)
                    (lecture_folder / "video").mkdir(exist_ok=True)
                    (lecture_folder / "transcript").mkdir(exist_ok=True)
                    
                    # Download file
                    file_name = file_meta.get("filename", f"file_{file_id}")
                    file_ext = Path(file_name).suffix
                    
                    # Determine destination based on file type
                    if file_ext.lower() in ['.pdf', '.pptx', '.ppt']:
                        dest_path = lecture_folder / "notes" / file_name
                    elif file_ext.lower() in ['.mp4', '.mov', '.avi']:
                        dest_path = lecture_folder / "video" / file_name
                    else:
                        dest_path = lecture_folder / "canvas" / file_name
                    
                    print(f"  Downloading {file_name}...")
                    download_url = download_info.get("public_url") or download_info.get("url")
                    if download_url:
                        success = await download_file(client, download_url, dest_path)
                        if success:
                            print(f"    ✓ Saved to {dest_path}")
                    
                    # Create lecture data entry
                    lecture_data = {
                        "lecture_date": lecture_date,
                        "module_id": module_id,
                        "module_name": item.get("title", ""),
                        "files": [{
                            "file_id": file_id,
                            "filename": file_name,
                            "display_name": item.get("title", file_name),
                            "content_type": file_meta.get("content-type", ""),
                            "size": file_meta.get("size", 0),
                            "url": file_meta.get("url", ""),
                            "local_path": str(dest_path.relative_to(base_path)),
                            "download_url": download_url
                        }],
                        "title": item.get("title", ""),
                        "status": "downloaded"
                    }
                    all_lectures_data.append(lecture_data)
    
    # Save lecture data to YAML-ready JSON
    data_file = data_path / "lectures.json"
    with open(data_file, "w") as f:
        json.dump(all_lectures_data, f, indent=2, default=str)
    
    print(f"\n✅ Lecture data saved to {data_file}")
    return all_lectures_data

async def main():
    """Main function."""
    print("Downloading lecture materials from Canvas...")
    
    for course_slug, course_config in COURSES.items():
        print(f"\n{'='*60}")
        print(f"Processing course: {course_slug}")
        print(f"{'='*60}")
        await process_course(course_slug, course_config)

if __name__ == "__main__":
    asyncio.run(main())
