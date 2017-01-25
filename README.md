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
