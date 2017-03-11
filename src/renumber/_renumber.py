"""
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

"""
import os
import shutil
import uuid


def _split_name_number(name):
    # Splits a given string into name and number where number is the at the end
    # of the string, e.g. 'foo2bar003baz001' will be split into 'foo2bar003baz'
    # and '001'
    num_part = []
    name_part = []
    reversed_ = reversed(name)
    while True:
        c = next(reversed_)
        if not c.isdigit():
            name_part = [c] + list(reversed_)
            name_part.reverse()
            break
        num_part.insert(0, c)
    return ''.join(name_part), ''.join(num_part)


def renumber(src_dir, dst_dir=None, in_place=False, start_at=None, padding=2):
    """
    Renames files representing an image sequence in the given directory to
    number them sequentially. File with same name and extension belong in the
    same sequence.

    Args:
        src_dir (str): Path to source directory containing the image sequence

        dst_dir (str, optional): Path to destination directory where the
            renamed files should be created. If not specified or None, a
            directory named 'renumbered_XXXXXXXX' (where XXXXXXXX is a random
            number) is created in the `src_dir`. Defaults to None

        in_place (bool, optional): If true, the files are named in place and
            `dst_dir` is ignored. Defaults to False

        start_at (int, optional): The number at which the image sequence should
            start. For example if start_at=3 then images will be named as
            image03.jpg, image04.jpg, ....
            Default to None, in this case the image sequnce numbering will
            start from the lowest numbered image.

        padding (int, optional): Specifies the number of leading zeroes in the
            number part of the image file name. Defaults to 2.

    Returns:
        Path(str) to the directory where renumbered files are created


    """

    # Create destination directory as required
    if dst_dir is None:
        renumbered_dir_name = '{0}_{1}'.format(
            'renumbered', uuid.uuid4().hex[:8])
        dst_dir = os.path.join(src_dir, renumbered_dir_name)
        if not os.path.exists(dst_dir):
            os.makedirs(dst_dir)

    # Iterate and collect file data by root name and number
    file_data = {}
    for content in os.listdir(src_dir):
        if not os.path.isfile(os.path.join(src_dir, content)):
            continue
        file_name, ext = content.rsplit('.', 1)
        name_part, num_part = _split_name_number(file_name)
        file_data.setdefault((name_part, ext), []).append(num_part)

    # Rename by sequentially numbering
    for (root_name, ext), nums in file_data.iteritems():
        min_num = (
            start_at
            if start_at is not None
            else min([int(n) for n in nums if n])
        )

        for index, num in enumerate(sorted(nums)):
            src_file_name = '{0}{1}.{2}'.format(root_name, num, ext)

            new_num = str(min_num + index).zfill(padding)
            dst_file_name = '{0}{1}.{2}'.format(root_name, new_num, ext)

            src = os.path.join(src_dir, src_file_name)
            dst = os.path.join(dst_dir, dst_file_name)

            shutil.copy2(src, dst)

            # We can use os.rename or shutil.move instead of below logic
            # but that does not cover the corner case when the number of a
            # source file is same as given start_at. In such case the names
            # collides and the wrong file will be picked up for renaming. To
            # safely avoid this, we first copy to dst dir and if required to
            # to change in place we simply reverse copy from dst to source
            # after deleting source files first.
            if in_place:
                os.unlink(src)
                new_src = dst
                new_dst = os.path.join(src_dir, dst_file_name)
                shutil.copy2(new_src, new_dst)
                os.unlink(dst)

    # Finally remove the dst_dir if in_place is required
    if in_place:
        shutil.rmtree(dst_dir)
        return src_dir
    else:
        return dst_dir
