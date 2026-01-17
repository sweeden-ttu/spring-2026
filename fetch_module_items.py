#!/usr/bin/env python3
"""
Fetch module items for Software Verification course to extract lecture information.
"""

import json
import sys
from pathlib import Path

canvas_mcp_path = Path(__file__).parent.parent.parent / "canvas-lms-mcp"
sys.path.insert(0, str(canvas_mcp_path))

import httpx
import asyncio
from config import load_env_config, get_api_headers

async def fetch_module_items(course_id: int, module_id: int):
    """Fetch items from a specific module."""
    config = load_env_config()
    headers = get_api_headers(config.api_token)
    
    async with httpx.AsyncClient(
        base_url=config.base_url,
        headers=headers,
        timeout=30.0
    ) as client:
        try:
            response = await client.get(
                f"/api/v1/courses/{course_id}/modules/{module_id}/items",
                params={"per_page": 100}
            )
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching module items: {e}", file=sys.stderr)
            return []

async def main():
    """Fetch module items for Software Verification course."""
    # Software Verification course ID and module IDs from previous fetch
    course_id = 70713
    module_ids = [811209, 811217, 811245, 811248, 811331, 813151]
    
    print(f"Fetching module items for course {course_id}...")
    
    all_items = {}
    for module_id in module_ids:
        print(f"  Fetching items for module {module_id}...")
        items = await fetch_module_items(course_id, module_id)
        if items:
            all_items[module_id] = items
            print(f"    Found {len(items)} items")
    
    output_file = Path(__file__).parent / "module_items.json"
    with open(output_file, "w") as f:
        json.dump(all_items, f, indent=2, default=str)
    
    print(f"\n✅ Module items saved to {output_file}")
    return all_items

if __name__ == "__main__":
    asyncio.run(main())
