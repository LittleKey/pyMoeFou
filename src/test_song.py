#!/usr/bin/env python
# encoding: utf-8

import unittest
import song


class TestSong(unittest.TestCase):

    def setup(self):
        pass

    def tearDown(self):
        pass

    def testGetInfo(self):
        d = {"sub_id": 2009, "sub_name": "Hey", "sub_url": "http://littlekey.me"}

        s = song.Song(d)

        self.assertEqual(s.GetInfo("%name|%id|%url"), "Hey|2009|http://littlekey.me")

if __name__ == '__main__':
    unittest.main()
