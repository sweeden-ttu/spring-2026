---
layout: article
title: LangSmith + Hands-on Experience
key: topic-15-langsmith-hands-on
tags:
  - LangSmith
  - LLM Testing
  - Practical
  - Hands-on
permalink: /software-verification/topics/15-langsmith-hands-on/
---

This topic provides comprehensive hands-on experience with LangSmith for testing, debugging, and evaluating LLM applications. Through practical exercises and real-world scenarios, students will learn essential techniques for using LangSmith effectively in production-grade LLM development.

<!--more-->

## Overview

LangSmith is a powerful platform for building, testing, and monitoring production-grade LLM applications. This hands-on topic focuses on practical application of LangSmith's capabilities for real-world LLM testing and evaluation scenarios.

## Learning Objectives

By the end of this topic, students will be able to:
- Set up and configure LangSmith for LLM testing
- Use LangSmith for debugging LLM applications
- Create and run test suites for LLM evaluation
- Analyze traces and performance metrics
- Apply LangSmith to real-world LLM testing scenarios

## Prerequisites

- **LangSmith Setup**: Complete [LangSmith Setup Instructions]({{ '/software-verification/topics/langsmith-setup/' | relative_url }}) first
- Python environment with LangSmith installed
- Basic understanding of LLM applications

## Hands-on Exercises

### Exercise 1: Basic Tracing

Learn to trace LLM application execution:
- Set up tracing in your application
- View traces in LangSmith UI
- Analyze execution flow

### Exercise 2: Test Suite Creation

Create test cases for LLM evaluation:
- Define test inputs and expected outputs
- Run test suites
- Analyze results

### Exercise 3: Debugging with LangSmith

Use LangSmith to debug LLM issues:
- Identify prompt problems
- Trace execution paths
- Optimize performance

## Setup Instructions

**Important**: Complete the [LangSmith Setup Instructions]({{ '/software-verification/topics/langsmith-setup/' | relative_url }}) before this lecture.

### Quick Start

```bash
# Install LangSmith
pip install langsmith

# Set up environment
export LANGCHAIN_API_KEY="your-api-key"
export LANGCHAIN_PROJECT="cs-5374-lab"
export LANGCHAIN_TRACING_V2="true"
```

## Related Materials

- **[LangSmith Setup Instructions]({{ '/software-verification/topics/langsmith-setup/' | relative_url }})**
- [LangSmith Documentation](https://docs.smith.langchain.com/)
- Course Canvas: [View Materials](https://texastech.instructure.com/courses/70713)

## Lab Files

Download lab materials from Canvas:
- LangSmith setup files
- Example code and exercises
- Lab assignments

## Resources

### Documentation
- [LangSmith Quick Start](https://docs.smith.langchain.com/quickstart)
- [LangSmith Tracing Guide](https://docs.smith.langchain.com/tracing)
- [LangSmith Testing Guide](https://docs.smith.langchain.com/evaluation)

### Course Materials
- Lecture slides and notes (available on Canvas)
- Lab assignment specifications

---

[← Topic 14: Student Presentation]({{ '/software-verification/topics/14-student-presentation-3/' | relative_url }}) | [Topic 16: AI/LLM/RL Evaluation →]({{ '/software-verification/topics/16-ai-llm-rl-evaluation/' | relative_url }})
