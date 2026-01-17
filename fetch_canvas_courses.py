#!/usr/bin/env python3
"""
Fetch Canvas course data for Spring 2026 courses.

Uses canvas-lms-mcp configuration to connect to Canvas and retrieve
detailed course information including modules, assignments, and schedule.
"""

import json
import sys
from pathlib import Path
from datetime import datetime, timedelta

# Add canvas-lms-mcp to path
canvas_mcp_path = Path(__file__).parent.parent.parent / "canvas-lms-mcp"
sys.path.insert(0, str(canvas_mcp_path))

import httpx
import asyncio
from config import load_env_config, get_api_headers

# Spring 2026 course IDs
COURSE_IDS = {
    "cryptography": 70714,
    "software-verification": 70713
}

async def fetch_course_data(course_id: int):
    """Fetch comprehensive course data from Canvas."""
    config = load_env_config()
    headers = get_api_headers(config.api_token)
    
    async with httpx.AsyncClient(
        base_url=config.base_url,
        headers=headers,
        timeout=30.0
    ) as client:
        try:
            # Get course details
            course_resp = await client.get(f"/api/v1/courses/{course_id}")
            course_resp.raise_for_status()
            course_data = course_resp.json()
            
            # Get modules
            modules_resp = await client.get(
                f"/api/v1/courses/{course_id}/modules",
                params={"per_page": 100, "include": ["items"]}
            )
            modules = []
            if modules_resp.status_code == 200:
                modules = modules_resp.json()
            
            # Get assignments
            assignments_resp = await client.get(
                f"/api/v1/courses/{course_id}/assignments",
                params={"per_page": 100}
            )
            assignments = []
            if assignments_resp.status_code == 200:
                assignments = assignments_resp.json()
            
            # Get enrollments (to find instructor)
            enrollments_resp = await client.get(
                f"/api/v1/courses/{course_id}/enrollments",
                params={"type[]": "TeacherEnrollment", "per_page": 100}
            )
            instructors = []
            if enrollments_resp.status_code == 200:
                instructors = enrollments_resp.json()
            
            return {
                "course": course_data,
                "modules": modules,
                "assignments": assignments,
                "instructors": instructors
            }
        except Exception as e:
            print(f"Error fetching course {course_id}: {e}", file=sys.stderr)
            return None

async def main():
    """Main function to fetch all course data."""
    print("Fetching Spring 2026 course data from Canvas...")
    
    all_course_data = {}
    for course_slug, course_id in COURSE_IDS.items():
        print(f"\nFetching data for {course_slug} (ID: {course_id})...")
        data = await fetch_course_data(course_id)
        if data:
            all_course_data[course_slug] = data
            print(f"✅ Retrieved {len(data['modules'])} modules, {len(data['assignments'])} assignments")
            if data['instructors']:
                print(f"   Instructors: {len(data['instructors'])} found")
    
    # Save to JSON file
    output_file = Path(__file__).parent / "canvas_course_data.json"
    with open(output_file, "w") as f:
        json.dump(all_course_data, f, indent=2, default=str)
    
    print(f"\n✅ Course data saved to {output_file}")
    return all_course_data

if __name__ == "__main__":
    asyncio.run(main())
