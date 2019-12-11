# Historical-Census-Mapping

Mapping Historical Census Data.

## Installation

### Prerequisites
[GEOS](https://trac.osgeo.org/geos/)

```bash
sudo apt-get install libgeos-dev
``` 

### Windows Requirements
You'll need to install the wheels required for shapely. Go [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely) and download the .whl for Shapely that also matches your Python install. For example, if you have x64 bit python you would need win_amd64.whl.

Then, when you get to install the required packages, before installing other packages. Do:

```powershell
pip install 'C:\where ever downloaded\Shapely-1.6.4.post2-cp38-cp38-win_amd64.whl'
```

Then you can install the rest of the packages.

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
