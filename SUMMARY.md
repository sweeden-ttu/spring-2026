# Spring 2026 Course Setup - Summary

## ✅ Completed Tasks

### 1. Master Courses Configuration
- ✅ Created `master_courses.yaml` with complete course metadata
- ✅ Includes Canvas IDs, syllabus URLs, media links, calendar feeds
- ✅ Stubbed lecture schedules for both courses

### 2. Folder Structure
- ✅ Created complete directory structure for both courses:
  - `cryptography/` with `_lectures/`, `_assignments/`, `_resources/`, `_output/`
  - `software-verification/` with same structure

### 3. Agent Instructions
- ✅ Created `AGENT_INSTRUCTIONS.md` for each course
- ✅ Defined workflows for Expert Research Scientist and Assistant Note Taker
- ✅ Includes calendar sync, material download, daily summaries, and research tasks

### 4. Course Documentation
- ✅ Created `syllabus.yaml` for each course with lecture schedules
- ✅ Created `README.md` files for navigation
- ✅ Updated course landing pages with planner sections

### 5. Faculty Research
- ✅ Found detailed profile for **Akbar Siami Namin** from [TTU CS Faculty Directory](https://www.depts.ttu.edu/cs/faculty/akbar_siami-namin/index.php)
- ✅ Created `FACULTY_PROFILES.md` with comprehensive instructor information
- ⚠️ **Hasan Al-Qudah** not found in public faculty directory (may be graduate student/adjunct)

### 6. Canvas Integration
- ✅ Created scripts to fetch Canvas data
- ✅ Extracted module information for Software Verification course
- ✅ Identified instructors from Canvas enrollment data

### 7. Landing Pages
- ✅ Updated `/courses/cryptography/` with planner table
- ✅ Updated `/courses/software-verification/` with planner and instructor info
- ✅ Created Spring 2026 overview page

## 📋 Faculty Information

### Akbar Siami Namin, Ph.D.
**Position**: Professor, Department of Computer Science  
**Faculty Page**: [TTU CS Faculty Directory](https://www.depts.ttu.edu/cs/faculty/akbar_siami-namin/index.php)

**Education**:
- Ph.D., Computer Science, University of Western Ontario
- M.S., Lakehead University at University of Western Ontario

**Research Interests**:
- Natural Language Processing
- Software & Cyber Security
- Machine Learning
- Program Analysis & Software Testing
- Modeling Human Factors
- Sequence and Time Series Analysis

**Research Labs**:
- **AVESTA (Advanced Empirical Software Testing and Analysis)** - Lab Director
- **Center for the Science & Engineering of Cyber Security (CSECS)** - Member

**Notable Work**: Leads AVESTA research group focused on empirical software engineering and program analysis

### Hasan Al-Qudah
**Status**: Not found in public TTU CS faculty directory  
**Notes**: May be a graduate student, visiting faculty, or adjunct instructor. Contact information to be obtained from course materials.

## 📁 File Structure Created

```
Spring2026/
├── master_courses.yaml              # Master course configuration
├── canvas_course_data.json          # Raw Canvas data
├── module_items.json                # Module items data
├── FACULTY_PROFILES.md              # Detailed faculty information
├── README.md                        # Overview and navigation
├── cryptography/
│   ├── syllabus.yaml
│   ├── AGENT_INSTRUCTIONS.md
│   ├── README.md
│   └── [folder structure]
└── software-verification/
    ├── syllabus.yaml
    ├── AGENT_INSTRUCTIONS.md
    ├── README.md
    └── [folder structure]
```

## 🔗 Key Links

### Software Verification (CS-5374)
- **Canvas**: https://texastech.instructure.com/courses/70713
- **Syllabus**: https://texastech.instructure.com/courses/70713/assignments/syllabus
- **Media Site**: https://engrmediacast.ttu.edu/Mediasite/Channel/96542-cs5374-d01-namin-spring-2026
- **Course Page**: /courses/software-verification/

### Cryptography (CS-6343)
- **Canvas**: https://texastech.instructure.com/courses/70714
- **Syllabus**: https://texastech.instructure.com/courses/70714/assignments/syllabus
- **Course Page**: /courses/cryptography/

## 📝 Next Steps

1. **Research Additional Faculty Info**:
   - Find Google Scholar profiles for Akbar Siami Namin
   - Find LinkedIn/IEEE profiles
   - Determine Hasan Al-Qudah's role and contact info

2. **Download Materials**:
   - Use Canvas MCP tools to download slide decks
   - Download video files from Mediasite
   - Organize materials in lecture folders

3. **Calendar Synchronization**:
   - Set up sync between Canvas and Gmail calendars
   - Create calendar events for upcoming lectures

4. **Fill Planner**:
   - Update planner tables as lectures progress
   - Add notes, slides, transcripts as available

5. **Daily Summaries**:
   - Agents will create summaries after each lecture
   - Research additional resources for each topic

## 📚 References

- [TTU CS Faculty Directory](https://www.depts.ttu.edu/cs/faculty/)
- [TTU CS Research Centers](https://www.depts.ttu.edu/cs/research/)
- [Center for the Science & Engineering of Cyber Security (CSECS)](https://www.depts.ttu.edu/cs/research/csecs/people.php)
- [AVESTA Research Group](https://www.depts.ttu.edu/cs/research/)
