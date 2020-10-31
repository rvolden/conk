# conk
Cython Smith-Waterman aligner for C3POa

Requirements:
 - Cython
 - setuptools
 - wheel

To build the module and install, run `make`.
To clean up this directory, run `make clean`.

Usage in python:
```python3
from conk import conk

seq = 'AAAAA'
penalty = 20

scores = conk.conk(seq, seq, penalty)
```
