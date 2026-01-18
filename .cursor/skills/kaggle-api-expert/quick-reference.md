# Kaggle API Quick Reference

Quick reference guide for common Kaggle API operations.

## Authentication

```bash
# Verify credentials
kaggle --version

# Test authentication
kaggle competitions list
```

## Dataset Operations

```bash
# List datasets
kaggle datasets list

# Search datasets
kaggle datasets list -s search-term

# Download dataset
kaggle datasets download -d username/dataset-name

# Create new dataset
kaggle datasets create -p /path/to/dataset -r zip

# Update existing dataset
kaggle datasets version -p /path/to/dataset -m "Update message"
```

## Competition Operations

```bash
# List competitions
kaggle competitions list

# Download competition data
kaggle competitions download -c competition-name

# Submit predictions
kaggle competitions submit -c competition-name -f predictions.csv -m "Message"

# View submissions
kaggle competitions submissions competition-name

# View leaderboard
kaggle competitions leaderboard competition-name

# Get leaderboard (download CSV)
kaggle competitions leaderboard competition-name --download
```

## Notebook Operations

```bash
# List notebooks
kaggle kernels list

# Push notebook
kaggle kernels push -p /path/to/notebook

# Pull notebook
kaggle kernels pull username/notebook-slug

# Output notebook
kaggle kernels output username/notebook-slug
```

## Python API Usage

```python
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

# Download dataset
api.dataset_download_files('username/dataset-name', path='./data', unzip=True)

# Submit to competition
api.competition_submit('predictions.csv', 'Submission message', 'competition-name')
```

## HPCC Jupyter Usage

```python
# In HPCC Jupyter notebook
!pip install kaggle --user

# Set credentials (if not using kaggle.json)
import os
os.environ['KAGGLE_USERNAME'] = 'username'
os.environ['KAGGLE_KEY'] = 'api-key'

# Download competition
!kaggle competitions download -c competition-name

# Extract
import zipfile
with zipfile.ZipFile('competition-name.zip', 'r') as z:
    z.extractall('./data')
```

## Common Workflows

### Download Competition Data

```bash
kaggle competitions download -c competition-name
unzip competition-name.zip -d ./data
```

### Submit Prediction

```bash
kaggle competitions submit -c competition-name -f predictions.csv -m "Description"
```

### Create Dataset

```bash
mkdir my-dataset
# Add files to my-dataset/
kaggle datasets create -p my-dataset -r zip
```

### Check Submission Status

```bash
kaggle competitions submissions competition-name
```
