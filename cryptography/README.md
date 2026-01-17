# Cryptography (CS-6343) - Spring 2026

## Course Overview

**Course Name**: Cryptography  
**Course Number**: CS-6343  
**Semester**: Spring 2026  
**Canvas ID**: 70714

This course provides an advanced study of cryptographic systems, security protocols, and modern encryption techniques. Students will explore symmetric and asymmetric encryption, hash functions, digital signatures, public key cryptography, number theory foundations, attack models, and security goals.

## Quick Links

- [Canvas Course](https://texastech.instructure.com/courses/70714)
- [Syllabus](https://texastech.instructure.com/courses/70714/assignments/syllabus)
- [Course Landing Page](/courses/cryptography/)
- [Course Calendar (iCal)](https://texastech.instructure.com/feeds/calendars/course_tPfa5STeKYoJe9DlOXVO5CKezugv193nXP3IAfnI.ics)

## Course Schedule

- **Start Date**: January 14, 2026
- **End Date**: May 15, 2026
- **Time Zone**: America/Chicago

## Topics Covered

- Historical overview of cryptography
- Basic terminology and security goals
- Number theory foundations
- Symmetric encryption (block ciphers, modes of operation)
- Public key encryption (RSA, Diffie-Hellman)
- Hash functions and digital signatures
- Attack models and security goals
- Modern cryptographic protocols

## Folder Structure

```
cryptography/
├── README.md                  # This file - course overview
├── syllabus.yaml              # Course schedule and lecture metadata
├── AGENT_INSTRUCTIONS.md      # Agent workflow instructions
├── _data/                     # Dynamic YAML data files (updated weekly)
│   ├── lectures.yaml          # Lecture metadata and file paths
│   └── course_info.yaml       # Course information and links
├── _lectures/                 # Organized by lecture date
│   ├── 2026-01-15/            # Lecture 1: Introduction to Cryptography
│   │   ├── canvas/            # Materials from Canvas LMS
│   │   ├── notes/             # Slide decks and notes
│   │   ├── video/             # Video files
│   │   └── transcript/        # Audio transcription files
│   └── [additional lectures]/
├── _assignments/              # Assignment materials
├── _resources/                # Additional resources
│   ├── references.bib         # Bibliography
│   ├── figures/               # Diagrams and images
│   └── templates/             # LaTeX templates
└── _output/                   # Generated content
    ├── markdown/              # Processed markdown articles
    └── latex/                 # Final LaTeX articles
```

## Lecture Materials

Lecture materials are organized by date in the `_lectures/` directory. Each lecture folder contains:

- **canvas/**: Original files downloaded from Canvas LMS
- **notes/**: Slide decks (PDF, PPTX) and extracted notes
- **video/**: Video lecture recordings
- **transcript/**: Audio transcriptions with timestamps

## Data-Driven Content

This course uses a **data-driven approach** where:

- **Static Markdown files** (in Jekyll site) reference dynamic YAML data
- **YAML data files** (in `_data/`) are updated weekly by agents downloading Canvas materials
- **Single source of truth**: Course information is stored in YAML, referenced by multiple markdown files

### YAML Data Files

- `_data/lectures.yaml`: Lecture metadata, file paths, status
- `_data/course_info.yaml`: Course links, instructor info, schedule

### Jekyll Integration

Markdown files in the Jekyll site reference this data:

```liquid
{% assign lectures = site.data.lectures | where: "course", "cryptography" %}
{% for lecture in lectures %}
  - {{ lecture.title }} ({{ lecture.date }})
{% endfor %}
```

## Agent Instructions

This course has dedicated agents for:
- **Expert Research Scientist**: Organizes materials, downloads from Canvas, researches additional resources
- **Assistant Note Taker**: Creates daily summaries, manages notes and transcripts

See `AGENT_INSTRUCTIONS.md` for detailed workflow.

## Notes

- All materials are organized by lecture date (YYYY-MM-DD format)
- Download materials before each lecture
- Update `syllabus.yaml` and `_data/lectures.yaml` after each lecture with status and file paths
- YAML data files are the single source of truth for lecture information
