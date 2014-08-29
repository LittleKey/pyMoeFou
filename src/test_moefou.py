#!/usr/bin/env python
# encoding: utf-8

import unittest
import moefou
from song import Song
from music import Music
import json


class TestMoeFou(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.mf = moefou.MoeFou()

    def tearDown(self):
        pass

    def test_GetMusicByName(self):
        rlt = self.mf.GetMusicByName("噬神者广播剧")
        with open("test.json") as fp:
            d = json.load(fp)
        m = Music(d['response']['wikis'][0])

        self.assertEqual(rlt, [m])

    @unittest.SkipTest
    def test_GetMusicByName_v2(self):
        rlt = self.mf.GetMusicByName("闪之轨迹OST")

        self.assertEqual(rlt, set(["英雄传说 闪之轨迹 OST"]))

    @unittest.SkipTest
    def test_GetSongByName(self):
        rlt = self.mf.GetSongByName("翼年代记")

        self.assertEqual(rlt, [])

    def test_GetSongByName_V2(self):
        rlt = self.mf.GetSongByName("祈り～You Raise Me Up Instrumental")
        with open("test_v2.json") as fp:
            d = json.load(fp)
        s = Song(d['response']['subs'][0])

        self.assertEqual(rlt, [s])

if __name__ == '__main__':
    unittest.main()
