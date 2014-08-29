#!/usr/bin/env python
# encoding: utf-8

import item


class ItemFactory(object):

    def __init__(self, t):
        self._t = t

    def Get(self, d):
        return item.Item(d, self._t)

if __name__ == '__main__':
    pass

