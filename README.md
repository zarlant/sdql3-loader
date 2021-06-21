# Installation
The tool can be installed with pip /pipx or run directly from src/cli.py

Installing using pipx from main sdql-loader directory:

```bash
pipx install .
```

If making local changes for testing, force a new install via:
```bash
pipx install . --force
```

# Usage 
Help text found when running sdql-load
```bash
sdql-load --help
```

## Finding Data
The script will attempt to import and merge any dictionaries found in the data-file path.

If the data-file passed does not end in .py, the software will attempt to load the data as raw json from the file via a call to:
```python
json.load("data_file_descriptor")
```

## Data Examples 
### Storing data in python, filename: data.py
```python
data = {"season": 2020}
```

### Storing data as raw json, filename: data.json
```javascript
{"season": 2020}
```

# Setup
Currently the only dependency of this software is the python package `requests`

