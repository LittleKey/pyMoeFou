#!/usr/bin/env python
# encoding: utf-8

import unittest
import music


class TestMusic(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_GetInfo(self):
        d = {"wiki_id": 1994, "wiki_name": "abcd"}

        m = music.Music(d)

        self.assertEqual(m.GetInfo('%id-%name'), '1994-abcd')

if __name__ == '__main__':
    unittest.main()
