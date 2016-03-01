# Hereby
Python library for accessing files in the same folder as your code

## Installation

```pip install hereby```

## Usage

```
from hereby import Here
here = Here(__file__)

f = here.open('file_next_to_sourcecode.txt')
print(f.read())
```
