# renumber

Renumbers image sequences by renaming them sequentially

For example: prodeng11.jpg prodeng11.png prodeng27.jpg prodeng32.jpg
prodeng32.png prodeng33.png prodeng47.png prodeng55.jpg prodeng55.png
prodeng56.jpg prodeng68.jpg prodeng72.png prodeng94.png weta17.jpg
weta22.jpg weta37.jpg weta55.jpg weta96.jpg

Would become: (split by sequence)
prodeng01.jpg prodeng02.jpg prodeng03.jpg prodeng04.jpg prodeng05.jpg
prodeng06.jpg prodeng01.png prodeng02.png prodeng03.png prodeng04.png
prodeng05.png prodeng06.png prodeng07.png weta01.jpg weta02.jpg weta03.jpg
weta04.jpg weta05.jpg

Includes options for adding padding, rename files in place or create new ones,
specify the start number of sequence etc. Please read through the renumber()
docstring for more.


```python
import renumber

src_dir = 'path to source directory'

dst_dir = 'path to destination directory'

in_place = False  # If True the files will be renamed in place otherwise
`dst_dir` will be used if given else a new directory called 'renumbered' will
be created in the `src_dir`

start_at = 37  # Number to start sequencing from, if not given lowest file
number will be used

padding = 4  # Padding (leading zeroes) for file numbers, defaults to 2
renumber.renumber(
    src_dr=src_dir,
    dst_dir=dst_dir,
    in_place=in_placem,
    start_at=start_at,
    padding=padding,
)
```