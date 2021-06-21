# Usage 
Help text found when running main.py
```python
python main.py --help
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
{"season": 2020}

# Setup
Currently the only dependency of this software is the python package `requests`

