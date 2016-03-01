# Here
Python library for accessing files in the same folder as your code

## Installation

```pip install here```

## Usage

```
from here import Here
here = Here(__file__)

f = here.open('file_next_to_sourcecode.txt')
print(f.read())
```
