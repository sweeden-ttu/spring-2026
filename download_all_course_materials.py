#!/usr/bin/env python3
"""
Download ALL module files for a course from Canvas LMS.

This script:
1. Fetches all modules for a course
2. Downloads all files from all modules
3. Organizes files by date/module in canvas folders
4. Updates YAML data files with download status
5. Extracts content from PDFs for notes/outlines
"""

import json
import sys
import os
import yaml
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
COURSE_CONFIG = {
    "software-verification": {
        "canvas_id": 70713,
        "course_slug": "software-verification"
    }
}

async def get_file_download_url(client, file_id, course_id):
    """Get download URL for a file."""
    try:
        url = f"/api/v1/files/{file_id}/public_url"
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"  Error getting download URL for file {file_id}: {e}", file=sys.stderr)
        return None

async def get_file_metadata(client, file_id, course_id):
    """Get file metadata."""
    try:
        url = f"/api/v1/courses/{course_id}/files/{file_id}"
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"  Error getting file metadata {file_id}: {e}", file=sys.stderr)
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
        print(f"  Error downloading {url}: {e}", file=sys.stderr)
        return False

async def fetch_all_modules(course_id):
    """Fetch all modules for a course."""
    config = load_env_config()
    headers = get_api_headers(config.api_token)
    
    async with httpx.AsyncClient(
        base_url=config.base_url,
        headers=headers,
        timeout=60.0
    ) as client:
        try:
            response = await client.get(
                f"/api/v1/courses/{course_id}/modules",
                params={"per_page": 100, "include": ["items"]}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching modules: {e}", file=sys.stderr)
            return []

async def fetch_module_items(course_id, module_id):
    """Fetch all items from a module."""
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
            print(f"Error fetching module items: {e}", file=sys.stderr)
            return []

async def process_course(course_slug, course_config):
    """Process a course and download all materials."""
    config = load_env_config()
    headers = get_api_headers(config.api_token)
    course_id = course_config["canvas_id"]
    
    base_path = Path(__file__).parent / course_slug
    data_path = base_path / "_data"
    
    # Load existing YAML files
    course_info_file = data_path / "course_info.yaml"
    lectures_file = data_path / "lectures.yaml"
    
    course_info = {}
    lectures_data = {"lectures": []}
    
    if course_info_file.exists():
        with open(course_info_file, 'r') as f:
            course_info = yaml.safe_load(f) or {}
    
    if lectures_file.exists():
        with open(lectures_file, 'r') as f:
            lectures_data = yaml.safe_load(f) or {"lectures": []}
    
    # Initialize indexing status if not present
    if "indexing_status" not in course_info:
        course_info["indexing_status"] = {
            "last_indexed": None,
            "modules_indexed": [],
            "files_downloaded": 0
        }
    
    print(f"\n{'='*60}")
    print(f"Processing course: {course_slug}")
    print(f"{'='*60}")
    
    async with httpx.AsyncClient(
        base_url=config.base_url,
        headers=headers,
        timeout=60.0
    ) as client:
        # Fetch all modules
        print("\nFetching all modules...")
        modules = await fetch_all_modules(course_id)
        print(f"Found {len(modules)} modules")
        
        all_downloaded_files = []
        module_to_lecture_map = {}
        
        # Map existing lectures to modules
        for lecture in lectures_data.get("lectures", []):
            if lecture.get("module_id"):
                module_to_lecture_map[lecture["module_id"]] = lecture
        
        # Process each module
        for module in modules:
            module_id = module["id"]
            module_name = module.get("name", f"Module {module_id}")
            
            print(f"\nProcessing module: {module_name} (ID: {module_id})")
            
            # Check if already indexed
            if module_id in course_info["indexing_status"]["modules_indexed"]:
                print(f"  Module already indexed, skipping...")
                continue
            
            # Fetch module items
            items = await fetch_module_items(course_id, module_id)
            print(f"  Found {len(items)} items")
            
            # Determine lecture date from module or use module completion date
            lecture_date = None
            if module.get("completed_at"):
                try:
                    lecture_date = datetime.fromisoformat(module["completed_at"].replace('Z', '+00:00')).strftime("%Y-%m-%d")
                except:
                    pass
            
            # Try to match with existing lecture
            lecture = module_to_lecture_map.get(module_id)
            if lecture:
                lecture_date = lecture["date"]
            elif not lecture_date:
                # Use module position to estimate date (assuming weekly schedule)
                # Start date + (position - 1) weeks
                start_date = datetime.strptime(course_info["course"]["start_date"], "%Y-%m-%d")
                weeks_offset = (module.get("position", 1) - 1)
                estimated_date = start_date.replace(day=start_date.day + (weeks_offset * 7))
                lecture_date = estimated_date.strftime("%Y-%m-%d")
            
            lecture_folder = base_path / "_lectures" / lecture_date
            canvas_folder = lecture_folder / "canvas"
            canvas_folder.mkdir(parents=True, exist_ok=True)
            
            # Process each item
            for item in items:
                if item.get("type") == "File" and item.get("content_id"):
                    file_id = item["content_id"]
                    
                    print(f"    Processing file: {item.get('title', f'file_{file_id}')}")
                    
                    # Get file metadata
                    file_meta = await get_file_metadata(client, file_id, course_id)
                    if not file_meta:
                        continue
                    
                    # Get download URL
                    download_info = await get_file_download_url(client, file_id, course_id)
                    if not download_info:
                        continue
                    
                    # Download file to canvas folder
                    filename = file_meta.get("filename", item.get("title", f"file_{file_id}"))
                    dest_path = canvas_folder / filename
                    
                    download_url = download_info.get("public_url") or download_info.get("url")
                    if download_url:
                        print(f"      Downloading to {dest_path}...")
                        success = await download_file(client, download_url, dest_path)
                        if success:
                            print(f"      ✓ Downloaded successfully")
                            all_downloaded_files.append({
                                "file_id": file_id,
                                "filename": filename,
                                "module_id": module_id,
                                "module_name": module_name,
                                "lecture_date": lecture_date,
                                "local_path": str(dest_path.relative_to(base_path)),
                                "canvas_url": file_meta.get("url", ""),
                                "size": file_meta.get("size", 0),
                                "content_type": file_meta.get("content-type", "")
                            })
                
                elif item.get("type") == "ExternalUrl":
                    # Save external URL information
                    print(f"    External URL: {item.get('title', 'Link')}")
                    print(f"      URL: {item.get('external_url', '')}")
                    
                    # Save URL info to a text file
                    url_file = canvas_folder / f"{item.get('title', 'external_link')}.url.txt"
                    with open(url_file, 'w') as f:
                        f.write(f"Title: {item.get('title', 'External Link')}\n")
                        f.write(f"URL: {item.get('external_url', '')}\n")
                        f.write(f"Module: {module_name}\n")
                        f.write(f"Date: {lecture_date}\n")
            
            # Mark module as indexed
            if module_id not in course_info["indexing_status"]["modules_indexed"]:
                course_info["indexing_status"]["modules_indexed"].append(module_id)
        
        # Update course_info.yaml
        course_info["indexing_status"]["last_indexed"] = datetime.now().isoformat()
        course_info["indexing_status"]["files_downloaded"] = len(all_downloaded_files)
        
        with open(course_info_file, 'w') as f:
            yaml.dump(course_info, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
        print(f"\n✅ Updated {course_info_file}")
        print(f"   Indexed {len(course_info['indexing_status']['modules_indexed'])} modules")
        print(f"   Downloaded {len(all_downloaded_files)} files")
        
        # Update lectures.yaml with downloaded files
        print(f"\nUpdating lectures.yaml with downloaded files...")
        for file_info in all_downloaded_files:
            # Find or create lecture entry
            lecture = None
            for lec in lectures_data["lectures"]:
                if lec.get("module_id") == file_info["module_id"] or lec.get("date") == file_info["lecture_date"]:
                    lecture = lec
                    break
            
            if not lecture:
                # Create new lecture entry
                lecture = {
                    "lecture_number": len(lectures_data["lectures"]) + 1,
                    "date": file_info["lecture_date"],
                    "title": file_info["module_name"],
                    "status": "downloaded",
                    "module_id": file_info["module_id"],
                    "module_name": file_info["module_name"],
                    "topics": [],
                    "files": [],
                    "video": {"available": False, "url": "", "local_path": ""},
                    "transcript": {"available": False, "local_path": ""},
                    "notes": []
                }
                lectures_data["lectures"].append(lecture)
            
            # Add file to lecture
            file_entry = {
                "filename": file_info["filename"],
                "file_id": file_info["file_id"],
                "type": "notes" if file_info["filename"].endswith(".pdf") else "other",
                "local_path": file_info["local_path"],
                "canvas_url": file_info["canvas_url"],
                "downloaded": True
            }
            
            # Check if file already in list
            if not any(f.get("file_id") == file_info["file_id"] for f in lecture.get("files", [])):
                if "files" not in lecture:
                    lecture["files"] = []
                lecture["files"].append(file_entry)
        
        # Sort lectures by date
        lectures_data["lectures"].sort(key=lambda x: x.get("date", ""))
        
        # Update lecture numbers
        for i, lecture in enumerate(lectures_data["lectures"], 1):
            lecture["lecture_number"] = i
        
        with open(lectures_file, 'w') as f:
            yaml.dump(lectures_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        
        print(f"✅ Updated {lectures_file}")
        print(f"   Total lectures: {len(lectures_data['lectures'])}")
    
    return all_downloaded_files

async def main():
    """Main function."""
    print("Downloading ALL course materials from Canvas...")
    
    for course_slug, course_config in COURSE_CONFIG.items():
        await process_course(course_slug, course_config)
    
    print("\n" + "="*60)
    print("✅ Complete!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(main())
