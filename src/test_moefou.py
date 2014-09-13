#!/usr/bin/env python
# encoding: utf-8

import unittest
import moefou
from song import Song
from music import Music
from itemfactory import ItemFactory
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

    def test_GetSongByMusic(self):
        m = self.mf.GetMusicByName("光明之刃")[0]
        rlt = self.mf.GetSongByMusic(m)

        self.assertEqual(rlt[-1], self.mf.GetSongByID(95297))

    def test_GetSongByID(self):
        s1 = self.mf.GetSongByID(95297)
        s2 = self.mf.GetSongByName("生命の桜歌")[0]

        self.assertEqual(s1, s2)

    def test_GetMusicByID(self):
        m1 = self.mf.GetMusicByID(11093)
        m2 = self.mf.GetMusicByName("光明之刃")[0]

        self.assertEqual(m1, m2)

    def test_GetUpBySong(self):
        s = self.mf.GetSongByName("hello goodbye &amp; hello")
        up = self.mf.GetUpBySong(s[0])[0]

        self.assertEqual(up.url, "http://nyan.90g.org/c/4/58/c11b0b0dbb1a9fb18980484a9480534a.mp3")

if __name__ == '__main__':
    unittest.main()
