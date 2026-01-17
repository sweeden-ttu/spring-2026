# Software Verification and Validation (CS-5374) - Spring 2026

## Course Overview

**Course Name**: Software Verification and Validation  
**Course Number**: CS-5374  
**Semester**: Spring 2026  
**Canvas ID**: 70713

This course covers methods and techniques for verifying and validating software systems, including testing strategies, formal methods, model checking, specification analysis, and continuous verification. Students will learn to apply modern verification tools and techniques to ensure software quality and reliability.

## Instructors

- **Primary Instructor**: [Akbar Siami Namin, Ph.D.](/faculty/akbar-siami-namin/)
- **Co-Instructor**: [Hasan Al-Qudah](/faculty/hasan-al-qudah/)

## Quick Links

- [Canvas Course](https://texastech.instructure.com/courses/70713)
- [Syllabus](https://texastech.instructure.com/courses/70713/assignments/syllabus)
- [Media Site (Mediasite)](https://engrmediacast.ttu.edu/Mediasite/Channel/96542-cs5374-d01-namin-spring-2026)
- [Course Landing Page](/courses/software-verification/)
- [Course Calendar (iCal)](https://texastech.instructure.com/feeds/calendars/course_StkXgOD3d2Rw2tv46ad0H4DyetiapkEA4bz1rUd1.ics)

## Course Schedule

- **Start Date**: January 14, 2026
- **End Date**: May 15, 2026
- **Time Zone**: America/Chicago

## Topics Covered

- Software testing fundamentals and strategies
- LangSmith setup and hands-on experiences
- Open source tools for testing/debugging AI/LLM/RL systems
- Formal methods and model checking
- Specification and requirements analysis
- Continuous verification
- Integration testing
- Unit testing strategies

## Folder Structure

```
software-verification/
├── README.md                  # This file - course overview
├── syllabus.yaml              # Course schedule and lecture metadata
├── AGENT_INSTRUCTIONS.md      # Agent workflow instructions
├── _data/                     # Dynamic YAML data files (updated weekly)
│   ├── lectures.yaml          # Lecture metadata and file paths
│   └── course_info.yaml       # Course information and links
├── _lectures/                 # Organized by lecture date
│   ├── 2026-01-14/            # Lecture 1: Introduction to Software Testing
│   │   ├── canvas/            # Materials from Canvas LMS
│   │   ├── notes/             # Slide decks and notes
│   │   ├── video/             # Video files
│   │   └── transcript/        # Audio transcription files
│   ├── 2026-01-21/            # Lecture 2: LangSmith Setup
│   └── 2026-01-28/            # Lecture 3: OpenSource Tools
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
{% assign lectures = site.data.lectures | where: "course", "software-verification" %}
{% for lecture in lectures %}
  - {{ lecture.title }} ({{ lecture.date }})
{% endfor %}
```

## Agent Instructions

This course has dedicated agents for:
- **Expert Research Scientist**: Organizes materials, downloads from Canvas, researches additional resources
- **Assistant Note Taker**: Creates daily summaries, manages notes and transcripts

See `AGENT_INSTRUCTIONS.md` for detailed workflow.

## Course-Specific Notes

### LangSmith
- Course includes LangSmith setup and hands-on experiences
- Setup instructions available in lecture materials

### Media Site
- Video lectures are hosted on Mediasite
- Access via: [Mediasite Channel](https://engrmediacast.ttu.edu/Mediasite/Channel/96542-cs5374-d01-namin-spring-2026)

## Notes

- All materials are organized by lecture date (YYYY-MM-DD format)
- Download materials before each lecture
- Update `syllabus.yaml` and `_data/lectures.yaml` after each lecture with status and file paths
- YAML data files are the single source of truth for lecture information
