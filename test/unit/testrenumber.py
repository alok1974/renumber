#!/usr/bin/env python

import os
import shutil
import unittest
import tempfile
import random

import renumber


def create_test_files(file_names, root_dir):
    if not os.path.exists(root_dir):
            os.makedirs(root_dir)
    for file_ in os.listdir(root_dir):
        os.unlink(os.path.join(root_dir, file_))

    for file_name in file_names:
        file_path = os.path.join(root_dir, file_name)
        with open(file_path, 'w') as fp:
            fp.write('')


class TestRenumber(unittest.TestCase):
    def setUp(self):
        self.test_file_names = [
            'prodeng11.jpg',
            'prodeng11.png',
            'prodeng27.jpg',
            'prodeng32.jpg',
            'prodeng32.png',
            'prodeng33.png',
            'prodeng47.png',
            'prodeng55.jpg',
            'prodeng55.png',
            'prodeng56.jpg',
            'prodeng68.jpg',
            'prodeng72.png',
            'prodeng94.png',
            'weta17.jpg',
            'weta22.jpg',
            'weta37.jpg',
            'weta55.jpg',
            'weta96.jpg'
        ]

        self.expected_file_names = [
            # jpg seq
            'prodeng11.jpg',
            'prodeng12.jpg',
            'prodeng13.jpg',
            'prodeng14.jpg',
            'prodeng15.jpg',
            'prodeng16.jpg',

            # png seq
            'prodeng11.png',
            'prodeng12.png',
            'prodeng13.png',
            'prodeng14.png',
            'prodeng15.png',
            'prodeng16.png',
            'prodeng17.png',

            # weta seq
            'weta17.jpg',
            'weta18.jpg',
            'weta19.jpg',
            'weta20.jpg',
            'weta21.jpg',

        ]

        self.root_dir = tempfile.mkdtemp()
        self.dst_dir = tempfile.mkdtemp()

        create_test_files(self.test_file_names, self.root_dir)

    def tearDown(self):
        if os.path.exists(self.root_dir):
            shutil.rmtree(self.root_dir)

        if os.path.exists(self.dst_dir):
            shutil.rmtree(self.dst_dir)

    def test_renumber_defaults(self):
        renumber.renumber(self.root_dir)
        renumbered_file_names = os.listdir(
            os.path.join(self.root_dir, 'renumbered')
        )

        self.assertEqual(
            sorted(renumbered_file_names),
            sorted(self.expected_file_names),
        )

    def test_renumber_in_place(self):
        renumber.renumber(self.root_dir, in_place=True)
        renumbered_file_names = os.listdir(self.root_dir)

        self.assertEqual(
            sorted(renumbered_file_names),
            sorted(self.expected_file_names),
        )

    def test_renumber_dst_dir(self):
        renumber.renumber(self.root_dir, dst_dir=self.dst_dir)
        renumbered_file_names = os.listdir(self.dst_dir)

        self.assertEqual(
            sorted(renumbered_file_names),
            sorted(self.expected_file_names),
        )

    def test_renumber_start_at(self):
        random_start_at = random.randint(10, 90)
        expected_file_names = (
            ['prodeng{0}.jpg'.format(random_start_at + i) for i in range(6)]
            + ['prodeng{0}.png'.format(random_start_at + i) for i in range(7)]
            + ['weta{0}.jpg'.format(random_start_at + i) for i in range(5)]
        )

        renumber.renumber(
            self.root_dir, dst_dir=self.dst_dir, start_at=random_start_at)
        renumbered_file_names = os.listdir(self.dst_dir)

        self.assertEqual(
            sorted(renumbered_file_names),
            sorted(expected_file_names),
        )

    def test_renumber_padding(self):
        renumber.renumber(self.root_dir, in_place=True, padding=5)
        last_file = sorted(os.listdir(self.root_dir))[-1]
        self.assertEqual(last_file, 'weta00021.jpg')


if __name__ == '__main__':
    unittest.main()
