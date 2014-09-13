#!/usr/bin/env python
# encoding: utf-8

import unittest
import item


class TestItem(unittest.TestCase):

    def setUp(self):
        self.d = {"id": 1974, "name": "Yooo~", "list": ["1", "2", {1:2}, 3]}
        self.t = item.Item(self.d)

    def tearDown(self):
        pass

    def test_GetInfo(self):
        rlt = self.t.GetInfo('name: %name\nid: %id\nlist: %list')

        self.assertEqual(rlt, "name: Yooo~\nid: 1974\nlist: ['1', '2', {1: 2}, 3]")

    def test_GetName(self):
        rlt = self.t.name

        self.assertEqual(rlt, 'Yooo~')

    def test_GetID(self):
        rlt = self.t.id

        self.assertEqual(rlt, 1974)

    def test_GetList(self):
        rlt = self.t.list

        self.assertEqual(rlt, ["1", "2", {1:2}, 3])

    def test___eq__(self):
        t = item.Item(self.d)

        self.assertEqual(t, self.t)

    def test___repr__(self):
        self.assertEqual(repr(self.t), "[['1', '2', {1: 2}, 3], 1974, Yooo~]")

    def test_GetKeys(self):
        self.assertEqual(self.t.GetKeys(), ["list", "id", "name"])


if __name__ == '__main__':
    unittest.main()

