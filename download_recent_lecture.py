#!/usr/bin/env python3
"""
Download files for the most recent lecture from Canvas LMS.

This script:
1. Identifies the most recent lecture from lectures.yaml
2. Downloads all files for that lecture
3. Updates the YAML file with download status
"""

import yaml
import sys
import os
from pathlib import Path
from datetime import datetime
import asyncio

# Add canvas-lms-mcp to path
canvas_mcp_path = Path(__file__).parent.parent.parent / "canvas-lms-mcp"
sys.path.insert(0, str(canvas_mcp_path))

import httpx
from config import load_env_config, get_api_headers

async def get_file_download_url(client, file_id, course_id):
    """Get download URL for a file."""
    try:
        url = f"/api/v1/files/{file_id}/public_url"
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error getting download URL for file {file_id}: {e}", file=sys.stderr)
        return None

async def get_file_metadata(client, file_id, course_id):
    """Get file metadata."""
    try:
        url = f"/api/v1/courses/{course_id}/files/{file_id}"
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error getting file metadata {file_id}: {e}", file=sys.stderr)
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

async def download_lecture_files(course_slug, course_id, lecture_data, base_path):
    """Download all files for a lecture."""
    config = load_env_config()
    headers = get_api_headers(config.api_token)
    
    lecture_date = lecture_data['date']
    lecture_path = base_path / "_lectures" / lecture_date
    
    downloaded_files = []
    
    async with httpx.AsyncClient(
        base_url=config.base_url,
        headers=headers,
        timeout=60.0
    ) as client:
        for file_info in lecture_data.get('files', []):
            file_id = file_info.get('file_id')
            if not file_id:
                continue
            
            print(f"\nProcessing file: {file_info.get('filename', f'file_{file_id}')}")
            
            # Get file metadata
            file_meta = await get_file_metadata(client, file_id, course_id)
            if not file_meta:
                continue
            
            # Get download URL
            download_info = await get_file_download_url(client, file_id, course_id)
            if not download_info:
                continue
            
            # Determine destination
            filename = file_meta.get('filename', file_info.get('filename', f'file_{file_id}'))
            file_ext = Path(filename).suffix.lower()
            
            if file_ext in ['.pdf', '.pptx', '.ppt', '.doc', '.docx']:
                dest_path = lecture_path / "notes" / filename
            elif file_ext in ['.mp4', '.mov', '.avi', '.mkv']:
                dest_path = lecture_path / "video" / filename
            elif file_ext in ['.zip', '.tar', '.gz']:
                dest_path = lecture_path / "canvas" / filename
            else:
                dest_path = lecture_path / "canvas" / filename
            
            # Download file
            download_url = download_info.get('public_url') or download_info.get('url')
            if download_url:
                print(f"  Downloading to {dest_path}...")
                success = await download_file(client, download_url, dest_path)
                if success:
                    print(f"    ✓ Downloaded successfully")
                    file_info['downloaded'] = True
                    file_info['local_path'] = str(dest_path.relative_to(base_path))
                    downloaded_files.append(file_info)
                else:
                    print(f"    ✗ Download failed")
    
    return downloaded_files

def get_most_recent_lecture(lectures_file):
    """Get the most recent lecture from lectures.yaml."""
    with open(lectures_file, 'r') as f:
        data = yaml.safe_load(f)
    
    lectures = data.get('lectures', [])
    if not lectures:
        return None
    
    # Sort by date, most recent first
    sorted_lectures = sorted(
        lectures,
        key=lambda x: datetime.strptime(x['date'], "%Y-%m-%d"),
        reverse=True
    )
    
    return sorted_lectures[0]

async def main():
    """Main function."""
    base_path = Path(__file__).parent
    
    # Process Software Verification course
    sv_path = base_path / "software-verification"
    sv_lectures_file = sv_path / "_data" / "lectures.yaml"
    
    if sv_lectures_file.exists():
        print("="*60)
        print("Processing Software Verification Course")
        print("="*60)
        
        recent_lecture = get_most_recent_lecture(sv_lectures_file)
        if recent_lecture:
            print(f"\nMost recent lecture: {recent_lecture['title']} ({recent_lecture['date']})")
            downloaded = await download_lecture_files(
                "software-verification",
                70713,
                recent_lecture,
                sv_path
            )
            
            # Update YAML file
            with open(sv_lectures_file, 'r') as f:
                data = yaml.safe_load(f)
            
            # Update the lecture entry
            for i, lecture in enumerate(data['lectures']):
                if lecture['date'] == recent_lecture['date']:
                    data['lectures'][i] = recent_lecture
                    break
            
            with open(sv_lectures_file, 'w') as f:
                yaml.dump(data, f, default_flow_style=False, sort_keys=False)
            
            print(f"\n✅ Downloaded {len(downloaded)} files")
            print(f"✅ Updated {sv_lectures_file}")
        else:
            print("No lectures found in lectures.yaml")
    
    print("\n" + "="*60)
    print("Done!")
    print("="*60)

if __name__ == "__main__":
    asyncio.run(main())
