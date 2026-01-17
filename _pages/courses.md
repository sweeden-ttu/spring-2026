---
layout: default
title: Courses
permalink: /courses/
---

# Spring 2026 Courses

## Software Verification and Validation (CS-5374)

{% assign sv_course = site.data['software-verification-course_info'] %}
{% assign sv_lectures = site.data['software-verification-lectures'] %}

### Course Information

- **Course**: {{ sv_course.course.name }}
- **Code**: {{ sv_course.course.code }}
- **Canvas ID**: {{ sv_course.course.canvas_id }}
- **Semester**: {{ sv_course.course.semester }}

### Links

- [Canvas Course]({{ sv_course.links.canvas }})
- [Syllabus]({{ sv_course.links.syllabus }})
{% if sv_course.links.media_site %}
- [Media Site]({{ sv_course.links.media_site }})
{% endif %}

### Lectures

{% if sv_lectures.lectures %}
{% for lecture in sv_lectures.lectures %}
- **Lecture {{ lecture.lecture_number }}** ({{ lecture.date }}): {{ lecture.title }}
  - Status: {{ lecture.status }}
  - Topics: {{ lecture.topics | join: ", " }}
{% endfor %}
{% else %}
*No lectures data available yet.*
{% endif %}

---

## Cryptography (CS-6343)

{% assign crypto_course = site.data['cryptography-course_info'] %}
{% assign crypto_lectures = site.data['cryptography-lectures'] %}

### Course Information

- **Course**: {{ crypto_course.course.name }}
- **Code**: {{ crypto_course.course.code }}
- **Canvas ID**: {{ crypto_course.course.canvas_id }}
- **Semester**: {{ crypto_course.course.semester }}

### Links

- [Canvas Course]({{ crypto_course.links.canvas }})
- [Syllabus]({{ crypto_course.links.syllabus }})

### Lectures

{% if crypto_lectures.lectures %}
{% for lecture in crypto_lectures.lectures %}
- **Lecture {{ lecture.lecture_number }}** ({{ lecture.date }}): {{ lecture.title }}
  - Status: {{ lecture.status }}
{% endfor %}
{% else %}
*No lectures data available yet.*
{% endif %}
