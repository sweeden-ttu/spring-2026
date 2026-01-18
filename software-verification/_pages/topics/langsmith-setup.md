---
layout: article
title: LangSmith Setup Instructions
key: langsmith-setup
tags:
  - LangSmith
  - Setup
  - LLM Testing
  - Tools
permalink: /software-verification/topics/langsmith-setup/
---

LangSmith is a powerful platform for building, testing, and monitoring production-grade LLM applications. This comprehensive guide will walk you through setting up LangSmith for use in CS-5374, ensuring you're ready for hands-on exercises and labs involving LLM testing and evaluation.

<!--more-->

## What is LangSmith?

LangSmith provides a comprehensive suite of capabilities for developing LLM applications:

- **Debugging and tracing**: Monitor LLM application execution in real-time
- **Testing and evaluation**: Create test suites and evaluate model performance
- **Monitoring and observability**: Track application behavior in production
- **Data collection and analysis**: Gather and analyze interaction data

This platform is essential for the course's focus on testing and evaluating AI/LLM systems.

## Prerequisites

Before beginning the setup, ensure you have:

1. **Python 3.8+** installed on your system
2. **pip** or **conda** package manager
3. **Internet connection** for accessing LangSmith services
4. **LangSmith account** (we'll create this during setup)

## Installation Steps

### Step 1: Create LangSmith Account

1. Visit [https://smith.langchain.com/](https://smith.langchain.com/)
2. Sign up for a free account using your university email
3. Verify your email address
4. Complete the initial setup wizard

### Step 2: Install LangSmith SDK

Install the LangSmith Python SDK using pip:

```bash
pip install langsmith
```

For conda users:

```bash
conda install -c conda-forge langsmith
```

Verify installation:

```bash
python -c "import langsmith; print(langsmith.__version__)"
```

### Step 3: Configure API Key

#### Get Your API Key

1. Log in to LangSmith at [https://smith.langchain.com/](https://smith.langchain.com/)
2. Navigate to **Settings** → **API Keys**
3. Click **Create API Key**
4. Copy the generated key (you won't be able to see it again!)

#### Set Environment Variable

**On macOS/Linux:**

```bash
export LANGCHAIN_API_KEY="your-api-key-here"
```

Add to your `~/.bashrc` or `~/.zshrc` for persistence:

```bash
echo 'export LANGCHAIN_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc
```

**On Windows:**

```cmd
setx LANGCHAIN_API_KEY "your-api-key-here"
```

Or use PowerShell:

```powershell
$env:LANGCHAIN_API_KEY="your-api-key-here"
[System.Environment]::SetEnvironmentVariable('LANGCHAIN_API_KEY', 'your-api-key-here', 'User')
```

#### Alternative: Use .env File

Create a `.env` file in your project directory:

```env
LANGCHAIN_API_KEY=your-api-key-here
LANGCHAIN_PROJECT=cs-5374-project
LANGCHAIN_TRACING_V2=true
```

Then load it in Python:

```python
from dotenv import load_dotenv
load_dotenv()
```

### Step 4: Configure Project Settings

Set additional environment variables:

```bash
export LANGCHAIN_PROJECT="cs-5374-project"
export LANGCHAIN_TRACING_V2="true"
```

These settings:
- **LANGCHAIN_PROJECT**: Organizes your traces into a named project
- **LANGCHAIN_TRACING_V2**: Enables tracing for your LLM calls

### Step 5: Verify Installation

Create a simple test script `test_langsmith.py`:

```python
from langsmith import Client

client = Client()
print("LangSmith connection successful!")
print(f"Connected to project: {client.default_project}")
```

Run the test:

```bash
python test_langsmith.py
```

If successful, you should see:
```
LangSmith connection successful!
Connected to project: cs-5374-project
```

## Configuration Methods

### Method 1: Environment Variables (Recommended)

```bash
export LANGCHAIN_API_KEY="your-api-key"
export LANGCHAIN_PROJECT="cs-5374-project"
export LANGCHAIN_TRACING_V2="true"
```

### Method 2: Configuration File

Create `langsmith_config.yaml`:

```yaml
langsmith:
  api_key: your-api-key-here
  project: cs-5374-project
  tracing: true
```

### Method 3: Python Configuration

```python
import os
os.environ["LANGCHAIN_API_KEY"] = "your-api-key"
os.environ["LANGCHAIN_PROJECT"] = "cs-5374-project"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
```

## Course Materials

### Download Course Files

Course materials for LangSmith setup are available:

- **[LangSmith Setup Instructions PDF]({{ '/software-verification/_lectures/2026-01-14/canvas/v0.1_LangSmith_Setup_Instructions-v1.pdf' | relative_url }})**
- **[LangSmith Zip Archive]({{ '/software-verification/_lectures/2026-01-14/canvas/langsmith.zip' | relative_url }})**

These files contain additional examples and exercises specific to our course.

### Local File Locations

Materials are stored locally at:
- `software-verification/_lectures/2026-01-14/canvas/v0.1_LangSmith_Setup_Instructions-v1.pdf`
- `software-verification/_lectures/2026-01-14/canvas/langsmith.zip`

## Usage in Course

LangSmith will be used extensively for:

1. **Testing LLM Applications**: Creating and running test suites
2. **Debugging Prompts**: Tracing prompt execution and identifying issues
3. **Evaluating Model Performance**: Comparing different models and configurations
4. **Tracing Execution Flows**: Understanding how LLM applications process requests

### Course Exercises

Refer to specific lecture materials for hands-on exercises:
- Lecture 15: LangSmith + Hands-on Experience
- Labs involving LLM testing and evaluation
- Course projects requiring LLM testing

## Troubleshooting

### Common Issues and Solutions

#### API Key Not Found

**Symptoms**: `KeyError` or "API key not found" errors

**Solution**:
```bash
# Verify environment variable is set
echo $LANGCHAIN_API_KEY

# Re-export if missing
export LANGCHAIN_API_KEY="your-api-key"
```

#### Connection Errors

**Symptoms**: Network errors or connection timeouts

**Solutions**:
1. Verify internet connection
2. Check LangSmith service status
3. Verify API key is valid and not expired
4. Check firewall settings

#### Project Not Found

**Symptoms**: "Project not found" warnings

**Solution**: Projects are created automatically on first trace. Ensure `LANGCHAIN_PROJECT` is set:

```bash
export LANGCHAIN_PROJECT="cs-5374-project"
```

### Getting Help

- **LangSmith Documentation**: [https://docs.smith.langchain.com/](https://docs.smith.langchain.com/)
- **Course Canvas**: [View on Canvas](https://texastech.instructure.com/courses/70713)
- **Instructor Office Hours**: See Canvas for schedule
- **LangSmith Community**: Check LangSmith Discord or forums

## Best Practices

1. **Keep API Keys Secure**: Never commit API keys to version control
2. **Use Project Names**: Organize traces with meaningful project names
3. **Enable Tracing**: Keep `LANGCHAIN_TRACING_V2=true` during development
4. **Review Traces**: Regularly check LangSmith dashboard for insights

## Additional Resources

- [LangSmith Quick Start Guide](https://docs.smith.langchain.com/quickstart)
- [LangSmith Tracing Documentation](https://docs.smith.langchain.com/tracing)
- [LangSmith Evaluation Guide](https://docs.smith.langchain.com/evaluation)
- [LangSmith Best Practices](https://docs.smith.langchain.com/best-practices)

---

**Important Note**: This setup is required for **Lecture 15 (LangSmith + Hands-on Experience)** and all subsequent labs involving LLM testing and evaluation. Please complete the setup before that lecture.

**Related Topics**: 
- [Topic 15: LangSmith + Hands-on Experience]({{ '/software-verification/topics/15-langsmith-hands-on/' | relative_url }})
- [Topic 16: AI/LLM/RL Evaluation]({{ '/software-verification/topics/16-ai-llm-rl-evaluation/' | relative_url }})
