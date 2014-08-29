#!/usr/bin/env python
# encoding: utf-8

import unittest
import itemfactory
from song import Song
from music import Music


class TestItemFactory(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_Get(self):
        itemFactory = itemfactory.ItemFactory('sub')

        d = {"sub_id": 999, "sub_name": "bbb"}

        rlt = itemFactory.Get(d)
        s = Song(d, 'sub')

        self.assertEqual(rlt, s)

    def test_Get_V2(self):
        itemFactory = itemfactory.ItemFactory('wiki')

        d = {"wiki_id": 999, "wiki_name": "bbb"}

        rlt = itemFactory.Get(d)
        m = Music(d)

        self.assertEqual(rlt, m)


if __name__ == '__main__':
    unittest.main()

