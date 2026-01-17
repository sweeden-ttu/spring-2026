# Spring 2026 Course Structure Summary

## ✅ Completed Setup

### Folder Structure

Both courses now have the following structure:

```
{course-slug}/
├── README.md                  # High-level course overview
├── syllabus.yaml              # Course schedule and lecture metadata
├── AGENT_INSTRUCTIONS.md      # Agent workflow instructions
├── _data/                     # Dynamic YAML data files (updated weekly)
│   ├── course_info.yaml       # Course information and links
│   └── lectures.yaml          # Lecture metadata and file paths
└── _lectures/                 # Organized by lecture date (YYYY-MM-DD)
    ├── 2026-01-15/            # Lecture folders
    │   ├── canvas/            # Materials from Canvas LMS
    │   ├── notes/             # Slide decks and notes
    │   ├── video/             # Video files
    │   └── transcript/        # Audio transcription files
    ├── 2026-01-19/            # Upcoming Monday
    ├── 2026-01-21/            # Upcoming Wednesday
    └── 2026-01-23/            # Upcoming Friday
```

## Software Verification (CS-5374)

### Media Sites & Landing Pages

- **Canvas Course**: https://texastech.instructure.com/courses/70713
- **Syllabus**: https://texastech.instructure.com/courses/70713/assignments/syllabus
- **Media Site (Mediasite)**: https://engrmediacast.ttu.edu/Mediasite/Channel/96542-cs5374-d01-namin-spring-2026
- **Calendar Feed**: https://texastech.instructure.com/feeds/calendars/course_StkXgOD3d2Rw2tv46ad0H4DyetiapkEA4bz1rUd1.ics
- **Course Landing Page**: /courses/software-verification/

### Lectures

**Completed**:
- **Lecture 1** (2026-01-15): Introduction to Software Testing
  - Module: "Lecture Notes : Software Testing"
  - File: Introduction to Testing.pdf (File ID: 11826183)
  - Status: Completed (file needs to be downloaded)

**Upcoming This Week**:
- **Lecture 2** (2026-01-19, Monday): TBD
- **Lecture 3** (2026-01-21, Wednesday): TBD
- **Lecture 4** (2026-01-23, Friday): TBD

## Cryptography (CS-6343)

### Media Sites & Landing Pages

- **Canvas Course**: https://texastech.instructure.com/courses/70714
- **Syllabus**: https://texastech.instructure.com/courses/70714/assignments/syllabus
- **Media Site**: Not available (403 Forbidden on Canvas API)
- **Calendar Feed**: https://texastech.instructure.com/feeds/calendars/course_tPfa5STeKYoJe9DlOXVO5CKezugv193nXP3IAfnI.ics
- **Course Landing Page**: /courses/cryptography/

### Lectures

**Planned**:
- **Lecture 1** (2026-01-15): Introduction to Cryptography
  - Status: Planned
  - Materials: To be downloaded from Canvas

## Data-Driven Architecture

### YAML Data Files (Single Source of Truth)

All course information is stored in YAML files that are updated by agents:

1. **`_data/course_info.yaml`**: Course links, instructor info, schedule
2. **`_data/lectures.yaml`**: Lecture metadata, file paths, status

### Jekyll Integration

Static markdown files in `/profile/_lectures/` reference the YAML data:

```liquid
{% assign sv_lectures = site.data['software-verification-lectures'].lectures.lectures %}
{% assign lecture_data = sv_lectures | where: "date", page.date | first %}
```

This ensures:
- **Single source of truth**: Update YAML files, markdown automatically reflects changes
- **No duplicate data**: Course info stored once, referenced everywhere
- **Easy updates**: Agents update YAML files weekly, no need to edit markdown

## Next Steps

1. **Download Lecture 1 Materials**:
   - Run `download_recent_lecture.py` to download files for 2026-01-15
   - Extract content from PDF slides
   - Update `lectures.yaml` with extracted content

2. **Weekly Updates**:
   - Agents download new materials each week
   - Update `_data/lectures.yaml` with new lecture info
   - Markdown pages automatically reflect updates

3. **Content Extraction**:
   - Extract text from PDF slides
   - Transcribe video content
   - Store in YAML for easy reference

## File Locations

- **Course Data**: `coursework/Spring2026/{course-slug}/_data/`
- **Lecture Materials**: `coursework/Spring2026/{course-slug}/_lectures/{date}/`
- **Jekyll Pages**: `profile/_lectures/{course-slug}-{date}.md`
- **Course Landing Pages**: `profile/_courses/{course-slug}.md`
