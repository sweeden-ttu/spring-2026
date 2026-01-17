# Spring 2026 Coursework

Course materials and organization for Spring 2026 courses at Texas Tech University.

## Courses

- **CS-5374**: Software Verification and Validation
- **CS-6343**: Cryptography

## Structure

```
Spring2026/
├── README.md                  # This file
├── _config.yml                # Jekyll configuration
├── Gemfile                    # Ruby dependencies
├── master_courses.yaml        # Master course configuration
├── software-verification/     # CS-5374 course materials
│   ├── README.md             # Course overviewf
│   ├── _data/                # YAML data files
│   └── _lectures/            # Organized by date
└── cryptography/              # CS-6343 course materials
    ├── README.md
    ├── syllabus.yaml
    ├── _data/
    └── _lectures/
```

## Setup Prerequisites

- Ruby 3.2.0+ (see `.ruby-version`)
- Bundler

### Installation

```bash
# Install dependencies
bundle install

# Build the site
bundle exec jekyll build

# Serve locally
bundle exec jekyll serve
```

The site will be available at `http://localhost:4000`

## Data-Driven Architecture

All course information is stored in YAML files:
f- `{course}/_data/course_info.yaml` - Course links and metadata
- `{course}/_data/lectures.yaml` - Lecture schedule and file paths

f
## License

This repository contains cf
