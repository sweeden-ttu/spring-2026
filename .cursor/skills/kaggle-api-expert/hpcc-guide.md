# HPCC Jupyter Notebook Guide for Kaggle API

This guide covers using Kaggle API with Jupyter notebooks on Texas Tech HPCC (High Performance Computing Center).

## Prerequisites

### VPN Connection (Required)

**Before starting any HPCC operations**, you must be connected to the Texas Tech VPN.

**Always ask**: "Are you connected to the Texas Tech VPN?"

If not connected:
1. Launch Texas Tech VPN client
2. Connect using your TTU credentials
3. Verify connection before proceeding

**HPCC resources are only accessible via VPN**.

### HPCC Account

- Active Texas Tech HPCC account
- Jupyter notebook access enabled
- Proper credentials for HPCC login

## Accessing HPCC Jupyter

### Step 1: Connect to VPN

1. Open Texas Tech VPN client
2. Enter TTU credentials
3. Connect to VPN
4. Verify successful connection

### Step 2: Access Jupyter Portal

HPCC Jupyter portal is typically available at:
- `https://jupyter.hpcc.ttu.edu/` (check HPCC documentation for current URL)

Or access via HPCC portal:
- Visit HPCC main portal
- Navigate to "Interactive Apps" or "Jupyter Notebook"

### Step 3: Launch Jupyter Session

1. Select Jupyter Notebook option
2. Choose resource allocation (CPU/GPU, memory, time)
3. Launch notebook session
4. Wait for session to start

## Installing Kaggle API in HPCC Jupyter

### Method 1: pip install in Notebook

```python
# Run in Jupyter notebook cell
!pip install kaggle --user

# Verify installation
!kaggle --version
```

### Method 2: Terminal Installation

If you have terminal access on HPCC:

```bash
# SSH to HPCC (after VPN connection)
ssh username@hpcc-login.ttu.edu

# Install Kaggle API
pip install kaggle --user

# Add to PATH if needed
export PATH=$PATH:~/.local/bin
```

## Setting Up Credentials

### Method 1: Upload kaggle.json via Jupyter

1. **Get kaggle.json**: Download from Kaggle Account → API section
2. **Upload to Jupyter**: Use Jupyter file browser to upload `kaggle.json`
3. **Create .kaggle directory**: 
   ```python
   import os
   os.makedirs('/home/username/.kaggle', exist_ok=True)
   ```
4. **Move file**:
   ```python
   !mv kaggle.json ~/.kaggle/
   ```
5. **Set permissions**:
   ```python
   !chmod 600 ~/.kaggle/kaggle.json
   ```

### Method 2: Environment Variables

```python
import os
os.environ['KAGGLE_USERNAME'] = 'your-kaggle-username'
os.environ['KAGGLE_KEY'] = 'your-kaggle-api-key'
```

### Method 3: Programmatic Setup (Not Recommended for Security)

```python
import json
import os

kaggle_creds = {
    "username": "your-username",
    "key": "your-api-key"
}

os.makedirs('/home/username/.kaggle', exist_ok=True)

with open('/home/username/.kaggle/kaggle.json', 'w') as f:
    json.dump(kaggle_creds, f)

os.chmod('/home/username/.kaggle/kaggle.json', 0o600)
```

## Using Kaggle API in HPCC Jupyter

### Download Competition Data

```python
import kaggle

# Download competition dataset
!kaggle competitions download -c competition-name

# Extract files
import zipfile
with zipfile.ZipFile('competition-name.zip', 'r') as zip_ref:
    zip_ref.extractall('./data')
```

### Working with Datasets

```python
# Download public dataset
!kaggle datasets download -d username/dataset-name

# List available datasets
!kaggle datasets list -s dataset-name
```

### Submitting to Competitions

```python
# Submit predictions
!kaggle competitions submit \
    -c competition-name \
    -f predictions.csv \
    -m "Model: XGBoost with feature engineering"

# Check submission status
!kaggle competitions submissions competition-name
```

## HPCC Resource Management

### Data Storage Locations

- **Home Directory** (`~`): Limited (~50GB), persistent
- **Scratch Space** (`/scratch/username/`): Larger, temporary
- **Work Directory**: Session-specific, cleaned after job

**Recommendation**: Store large datasets in scratch space:

```python
import os
scratch_dir = f'/scratch/{os.environ["USER"]}/kaggle_data'
os.makedirs(scratch_dir, exist_ok=True)
os.chdir(scratch_dir)
```

### Module Loading

HPCC uses environment modules. Load required software:

```python
# Example: Load Python module
!module load python/3.9

# Load GPU modules if needed
!module load cuda/11.8
!module load cudnn/8.9
```

Check available modules:
```python
!module avail
```

### Resource Allocation

When launching Jupyter session:
- **CPU cores**: Request appropriate number
- **Memory**: Request sufficient RAM for datasets
- **Time limit**: Set appropriate walltime
- **GPU**: Request if using GPU-accelerated training

## Troubleshooting HPCC Issues

### VPN Connection Problems

**Symptom**: Cannot access HPCC portal

**Solution**:
1. Verify VPN is connected
2. Check VPN client status
3. Try reconnecting to VPN
4. Verify HPCC portal URL is correct

### Jupyter Session Not Starting

**Symptom**: Jupyter session fails to launch

**Solution**:
1. Check resource availability
2. Reduce requested resources (CPU/memory)
3. Check for error messages in job queue
4. Try different time slot

### Kaggle API Not Working

**Symptom**: API calls fail in HPCC Jupyter

**Solution**:
```python
# Verify credentials
!cat ~/.kaggle/kaggle.json

# Test API
!kaggle competitions list

# Check internet connectivity from HPCC
!curl https://www.kaggle.com
```

### Permission Errors

**Symptom**: Permission denied errors

**Solution**:
```python
# Fix permissions
!chmod 600 ~/.kaggle/kaggle.json
!chmod 700 ~/.kaggle
```

## Best Practices for HPCC + Kaggle

1. **Always verify VPN** before HPCC access
2. **Use scratch space** for large datasets and outputs
3. **Clean up temporary files** after jobs complete
4. **Save important work** to home directory or external storage
5. **Monitor resource usage** to stay within limits
6. **Use appropriate resource requests** (don't over-request)
7. **Test locally first** when possible before using HPCC resources

---

**Reference**: 
- HPCC User Guide: https://www.depts.ttu.edu/hpcc/userguides/general_guides/jupyter-notebooks.php
- Contact HPCC Support: support@hpcc.ttu.edu
