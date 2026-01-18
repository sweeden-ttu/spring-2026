---
layout: article
title: Adequacy Criterion
key: topic-02-adequacy-criterion
tags:
  - Testing
  - Adequacy
  - Coverage
  - Metrics
permalink: /software-verification/topics/02-adequacy-criterion/
---

Adequacy criteria define when testing is "good enough" by providing objective measures to determine test suite quality and completeness. Understanding adequacy criteria is essential for making informed decisions about test coverage and when to stop testing.

<!--more-->

## What are Adequacy Criteria?

**Adequacy criteria** are objective measures that determine:
- **When to stop testing**: When is testing sufficient?
- **Test quality**: How good is the test suite?
- **Coverage**: What percentage of the software has been tested?

These criteria provide quantitative metrics for evaluating test suites, moving beyond subjective judgments about test completeness.

### The Testing Dilemma

One of the fundamental challenges in software testing is determining:
- How many tests are enough?
- Which tests should be prioritized?
- When can we confidently stop testing?

Adequacy criteria address these questions by providing measurable standards.

## Types of Adequacy Criteria

### Statement Coverage

**Statement coverage** measures the percentage of executable statements that have been executed by at least one test case.

- **Minimum criterion**: Every executable statement must be executed at least once
- **Goal**: Achieve 100% statement coverage (when feasible)
- **Limitation**: Does not guarantee all execution paths are tested

### Branch Coverage

**Branch coverage** (also called decision coverage) measures the percentage of decision branches that have been executed by test cases.

- **More comprehensive** than statement coverage
- **Requirement**: Each branch (true/false) of every decision must be executed
- **Better indicator** of test thoroughness than statement coverage alone

### Path Coverage

**Path coverage** measures the percentage of execution paths through the program that have been tested.

- **Most comprehensive** coverage criterion
- **Often infeasible** for complex programs with many paths
- **Practical approach**: Test critical paths and representative paths

### Condition Coverage

**Condition coverage** focuses on boolean conditions, ensuring each boolean expression is evaluated to both true and false.

- **Important for** complex decision logic
- **Complements** branch coverage
- **Useful for** testing conditional expressions

### Modified Condition/Decision Coverage (MC/DC)

**MC/DC** ensures each condition independently affects the decision outcome.

- **Commonly used** in safety-critical systems
- **More rigorous** than simple condition coverage
- **Required by** many safety standards (e.g., DO-178B/C)

## Measuring Adequacy

### Coverage Tools

Various tools are available for measuring code coverage:

- **JaCoCo**: Java code coverage tool
- **Coverage.py**: Python coverage measurement
- **Istanbul/nyc**: JavaScript coverage
- **gcov**: C/C++ coverage tool

### Coverage Analysis

When analyzing coverage:

1. **Set target coverage**: Determine acceptable coverage level (e.g., 80% statement coverage)
2. **Identify gaps**: Find uncovered code areas
3. **Prioritize**: Focus on critical or high-risk areas
4. **Iterate**: Add tests to improve coverage

### Trade-offs

Different coverage criteria have trade-offs:

- **Higher coverage**: More thorough but requires more test cases
- **Path coverage**: Comprehensive but often impossible to achieve 100%
- **Statement coverage**: Easy to measure but may miss important paths
- **Branch coverage**: Good balance between thoroughness and feasibility

## Practical Applications

### In Software Development

Adequacy criteria help development teams:

1. **Measure test completeness**: Quantify how well the software is tested
2. **Guide test creation**: Identify areas needing more tests
3. **Make release decisions**: Determine if testing is sufficient for release
4. **Track quality metrics**: Monitor testing progress over time

### Coverage Levels

Common coverage targets:

- **Unit tests**: 80-90% statement coverage
- **Integration tests**: 60-80% branch coverage
- **System tests**: Path-based coverage of critical paths
- **Safety-critical**: 100% MC/DC coverage (where required)

## Limitations and Considerations

### Coverage ≠ Quality

**Important**: High coverage does not guarantee:
- All bugs are found
- Correctness of software
- Good test quality
- Appropriate test cases

### Other Quality Factors

Beyond coverage, consider:
- **Test relevance**: Do tests verify important requirements?
- **Test maintenance**: Are tests maintainable?
- **Test execution time**: Can tests run efficiently?
- **Defect detection**: Do tests actually find bugs?

## Advanced Topics

### Mutation Testing

**Mutation testing** evaluates test adequacy by introducing small changes (mutations) to code and checking if tests detect them.

- High-quality test suites should kill most mutants
- Provides insight into test effectiveness
- Computationally expensive but powerful

### Property-Based Testing

**Property-based testing** uses adequacy criteria based on properties that should hold across many test inputs.

- Generates many test cases automatically
- Tests properties rather than specific values
- Effective for finding edge cases

## Related Course Materials

Check course materials for lectures covering:
- Code coverage tools and techniques
- Testing metrics and measurements
- Adequacy criteria in practice

## Summary

Adequacy criteria provide:
- **Objective measures** of test completeness
- **Guidance** for test creation and prioritization
- **Metrics** for tracking testing progress
- **Standards** for quality assurance

Understanding and applying adequacy criteria is essential for effective software testing and quality assurance.

## Further Reading

- Software Testing: Principles and Practices (textbook)
- IEEE Standards on Software Testing
- Code coverage tools documentation

---

**Previous Topic**: [Introduction to V&V]({{ '/software-verification/topics/01-introduction-vv/' | relative_url }}) ←  
**Next Topic**: [Black Box Testing]({{ '/software-verification/topics/04-black-box-testing/' | relative_url }}) →
