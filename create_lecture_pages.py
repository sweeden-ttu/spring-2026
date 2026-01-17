#!/usr/bin/env python3
"""
Create Jekyll-compatible markdown pages for lectures that reference YAML data.

This script generates static markdown files that read from dynamic YAML data sources,
ensuring a single source of truth for lecture information.
"""

import yaml
import json
from pathlib import Path
from datetime import datetime

def load_yaml_file(file_path):
    """Load YAML file."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def create_lecture_page(course_slug, lecture_data, course_info, output_dir):
    """Create a Jekyll markdown page for a lecture."""
    date_str = lecture_data['date']
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Create filename
    filename = f"{course_slug}-{date_str}.md"
    output_path = output_dir / filename
    
    # Front matter
    front_matter = {
        'layout': 'page',
        'title': lecture_data.get('title', 'Lecture'),
        'course': course_info['course']['name'],
        'course_slug': course_slug,
        'course_number': course_info['course']['code'],
        'date': date_str,
        'lecture_number': lecture_data.get('lecture_number', 0),
        'permalink': f"/lectures/{course_slug}/{date_str}/",
        'tags': [course_slug, 'spring-2026']
    }
    
    # Generate markdown content
    content = f"""---
layout: page
title: "{lecture_data.get('title', 'Lecture')}"
course: "{course_info['course']['name']}"
course_slug: "{course_slug}"
course_number: "{course_info['course']['code']}"
date: {date_str}
lecture_number: {lecture_data.get('lecture_number', 0)}
permalink: /lectures/{course_slug}/{date_str}/
tags:
  - {course_slug}
  - spring-2026
---

{{% comment %}} Load course and lecture data from YAML {{% endcomment %}}
{{% assign course_data = site.data.courses | where: "slug", page.course_slug | first %}}
{{% assign lecture_data = site.data.lectures | where: "course", page.course_slug | where: "date", page.date | first %}}

# {lecture_data.get('title', 'Lecture')}

**Course**: {course_info['course']['name']} ({course_info['course']['code']})  
**Date**: {date_obj.strftime('%B %d, %Y')}  
**Lecture Number**: {lecture_data.get('lecture_number', 0)}

{{% if lecture_data %}}
## Lecture Information

**Status**: {{{{ lecture_data.status | capitalize }}}}  
{{% if lecture_data.module_name %}}**Module**: {{{{ lecture_data.module_name }}}}{{% endif %}}

### Topics Covered

{{% for topic in lecture_data.topics %}}
- {{{{ topic }}}}
{{% endfor %}}

## Materials

### Slides and Notes

{{% if lecture_data.files.size > 0 %}}
{{% for file in lecture_data.files %}}
- **[[{{{{ file.filename }}}}]({{{{ file.local_path }}}})]**
  - Type: {{{{ file.type | capitalize }}}}
  - [View on Canvas]({{{{ file.canvas_url }}}})
{{% endfor %}}
{{% else %}}
*No files available yet.*
{{% endif %}}

### Video

{{% if lecture_data.video.available %}}
- [Watch Video]({{{{ lecture_data.video.url }}}})
- Local: {{{{ lecture_data.video.local_path }}}}
{{% else %}}
*Video not available.*
{{% endif %}}

### Transcript

{{% if lecture_data.transcript.available %}}
- [View Transcript]({{{{ lecture_data.transcript.local_path }}}})
{{% else %}}
*Transcript not available.*
{{% endif %}}

## Course Links

- [Canvas Course]({{{{ course_data.canvas_url }}}})
- [Syllabus]({{{{ course_data.syllabus_url }}}})
{{% if course_data.media_site_url %}}
- [Media Site]({{{{ course_data.media_site_url }}}})
{{% endif %}}
- [Course Page]({{{{ course_data.landing_pages.course_page }}}})

{{% else %}}
## Lecture Information

*Lecture data is being processed. Please check back soon.*

## Course Links

- [Canvas Course]({{{{ course_data.canvas_url }}}})
- [Syllabus]({{{{ course_data.syllabus_url }}}})
- [Course Page]({{{{ course_data.landing_pages.course_page }}}})
{{% endif %}}

---

## Notes

This lecture page is automatically generated from YAML data files. The content is updated when agents download materials from Canvas LMS.

**Data Sources**:
- Course info: `coursework/Spring2026/{course_slug}/_data/course_info.yaml`
- Lecture data: `coursework/Spring2026/{course_slug}/_data/lectures.yaml`
"""
    
    # Write file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(content)
    
    print(f"Created: {output_path}")
    return output_path

def main():
    """Main function."""
    base_path = Path(__file__).parent
    profile_lectures_path = Path(__file__).parent.parent.parent / "profile" / "_lectures"
    profile_lectures_path.mkdir(parents=True, exist_ok=True)
    
    courses = ["software-verification", "cryptography"]
    
    for course_slug in courses:
        course_path = base_path / course_slug
        data_path = course_path / "_data"
        
        # Load course info
        course_info_file = data_path / "course_info.yaml"
        if not course_info_file.exists():
            print(f"Skipping {course_slug}: course_info.yaml not found")
            continue
        
        course_info = load_yaml_file(course_info_file)
        
        # Load lectures
        lectures_file = data_path / "lectures.yaml"
        if not lectures_file.exists():
            print(f"Skipping {course_slug}: lectures.yaml not found")
            continue
        
        lectures_data = load_yaml_file(lectures_file)
        
        # Create pages for each lecture
        for lecture in lectures_data.get('lectures', []):
            # Add course identifier to lecture data
            lecture['course'] = course_slug
            create_lecture_page(course_slug, lecture, course_info, profile_lectures_path)
    
    print("\n✅ Lecture pages created!")

if __name__ == "__main__":
    main()
