# renumber

Renumbers image sequences by renaming them sequentially

For example: prodeng11.jpg prodeng11.png prodeng27.jpg prodeng32.jpg
prodeng32.png prodeng33.png prodeng47.png prodeng55.jpg prodeng55.png
prodeng56.jpg prodeng68.jpg prodeng72.png prodeng94.png render17.jpg
render22.jpg render37.jpg render55.jpg render96.jpg

Would become: (split by sequence)
prodeng01.jpg prodeng02.jpg prodeng03.jpg prodeng04.jpg prodeng05.jpg
prodeng06.jpg prodeng01.png prodeng02.png prodeng03.png prodeng04.png
prodeng05.png prodeng06.png prodeng07.png render01.jpg render02.jpg render03.jpg
render04.jpg render05.jpg

Includes options for adding padding, rename files in place or create new ones,
specify the start number of sequence etc. Please read through the renumber()
docstring for more.


```python
import renumber

# Path to source directory where the files to renumber reside
src_dir = 'path to source directory'

# Path to destination directory where the new renumbered files should be created.
# This is optional parameter if not given, a new directory called
# 'renumbered_<random_number>' will be created in the `src_dir`.
# Also if `in_place=True` is specified then this parameter is ignored
# and files in src_dir will be replaced by the new renumbered files.
dst_dir = 'path to destination directory'

# If True the files will be renamed in place otherwise
# `dst_dir` will be used if given else a new directory called 
# 'renumbered_<random_number>' will be created in the `src_dir`
in_place = False


# Number to start sequencing from, if not given lowest file number will be used
start_at = 37


# Padding (leading zeroes) for file numbers, defaults to 2
padding = 4


renumber.renumber(
    src_dr=src_dir,
    dst_dir=dst_dir,
    in_place=in_placem,
    start_at=start_at,
    padding=padding,
)
```
