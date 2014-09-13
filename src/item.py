#!/usr/bin/env python
# encoding: utf-8

import re


class Item(object):

    def __init__(self, data, t=''):
        self._t = t
        self._data = {}
        if t:
            match = re.compile(r"^{}_(.*?)$".format(self._t), re.I)
        else:
            match = re.compile(r".*")

        for k, v in data.items():
            if match.match(k):
                key = match.findall(k)[0].lower()
                self._data[key] = v

        if self._data.get('_data') or self._data.get('_t'):
            raise NameError("Can not use '_data' or '_t' attribute of Item")

    def GetInfo(self, formatStr):
        rlt = formatStr
        for k, v in self._data.items():
            rlt = rlt.replace('%' + str(k), str(v))

        return rlt

    def GetKeys(self):
        return self._data.keys()

    def __getattribute__(self, name):
        if (name != "_data") and (name in self._data.keys()):
            return self._data[str(name).lower()]
        else:
            return super(Item, self).__getattribute__(name)

    def __eq__(self, right):
        return self._data == right._data

    def __ne__(self, right):
        return self._data != right._data

    def __repr__(self):
        return '[' + self.GetInfo(', '.join(map(lambda k: '%' + str(k), self._data.keys()))) + ']'

if __name__ == '__main__':
    pass

