#!/usr/bin/env python
# encoding: utf-8

import requests
import re
import itemfactory

def undefine(func):
    def RaiseNameError(s, *a):
        raise NameError("Not define {} on {}".format(func.__name__, s.__class__))

    return RaiseNameError


class MoeFou(object):

    def __init__(self):
        self.api_key = '09edf82ae867ef45f95136105eefcd5c053fc66bc'

    def GetSongByName(self, name):
        return self.GetSoneFromSub(name)

    def GetMusicByName(self, name):
        return self.GetMusicFromWiki(name)

    def _GetItemByID(self, item, ID):
        t = item == "song" and "sub" or "wiki"
        data = {
                "{}_id".format(t): ID,
                "api_key": self.api_key
                }

        d = self._Get("http://api.moefou.org/{}/detail.json".format(item), data)
        itemFactory = itemfactory.ItemFactory(t)

        return itemFactory.Get(d[t])

    def _GetAllPage(self, nextIter, t):
        itemFactory = itemfactory.ItemFactory(t)
        rlt = []
        haveNext = True
        page = 1

        while haveNext:
            d = nextIter(page)

            dInfo = d['information']
            dList = d[t + 's'] or []

            if dInfo['has_error']:
                raise Exception('Has error in search from moefou')

            for it in dList:
                rlt.append(itemFactory.Get(it))

            page += 1
            haveNext = dInfo.get('may_have_next', False)

        return rlt

    def GetSongByMusic(self, m):
        def nextIter(page):
            data = {
                    "wiki_id": m.id,
                    "api_key": self.api_key,
                    "page": page
                    }

            return self._Get("http://api.moefou.org/music/subs.json", data)

        return self._GetAllPage(nextIter, 'sub')

    def _GetSthFromSwer(self, sth, swer, name):
        def nextIter(page):
            data = {
                    'keyword': name,
                    'wiki_type': sth,
                    'page': page,
                    'api_key': self.api_key
                    }

            return self.__getattribute__("_Search" + swer).__call__(data)

        return self._GetAllPage(nextIter, swer)

    def _Search(self, wikiType, data):
        return self._Get('http://api.moefou.org/search/{}.json'.format(wikiType), data)

    def __getattribute__(self, name):
        matchGet = re.compile(r"^Get(.*?)From(.*?)$")
        matchGetByID = re.compile(r"^Get(.*?)ByID$", re.I)
        if len(name) > 7 and name.startswith("_Search"):
            url = name[7:].lower()
            return lambda d: self._Search(url, d)
        elif matchGet.match(name):
            t, w = map(lambda s: s.lower(), matchGet.findall(name)[0])
            return lambda n: self._GetSthFromSwer(sth=t, swer=w, name=n)
        elif matchGetByID.match(name):
            item = matchGetByID.findall(name)[0].lower()
            return lambda ID: self._GetItemByID(item, ID)
        else:
            return super(MoeFou, self).__getattribute__(name)

    def _Get(self, url, data):
        r = requests.get(url, params=data)

        if not r.ok:
            raise r.raise_for_status

        d = r.json()

        if d['response']['information']['has_error']:
            raise Exception('Has error in search from moefou')

        return d['response']

if __name__ == '__main__':
    pass

