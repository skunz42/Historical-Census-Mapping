# Historical-Census-Mapping

Mapping Historical Census Data.

## Installation

### Prerequisites
[GEOS](https://trac.osgeo.org/geos/)

```bash
sudo apt-get install libgeos-dev
``` 

### Clone the repo

```bash
git clone https://github.com/skunz42/Historical-Census-Mapping
```

### Creating Virtual Environment

From the root directory of the repository run:

```bash
python -m venv ./venv
source ./venv/bin/activate
```

### Install required packages

```bash
pip install -r requirements.txt
```

## Usage

```python
python mergetool <file1.json> <file2.json> <Merged.json>
```
