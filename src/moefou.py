#!/usr/bin/env python
# encoding: utf-8

import requests
import re
import itemfactory


class MoeFou(object):

    def __init__(self):
        self.api_key = '09edf82ae867ef45f95136105eefcd5c053fc66bc'

    def GetSongByName(self, name):
        return self.GetSongFromSub(name)

    def GetMusicByName(self, name):
        return self.GetMusicFromWiki(name)

    #def _SearchWiki(self, data):
    #    return self._Get('http://api.moefou.org/search/wiki.json', data)

    #def SearchSub(self, data):
    #    return self._Get('http://api.moefou.org/search/sub.json', data)

    def _GetSthFromSwer(self, sth, swer, name):
        data = {
                'keyword': name,
                'wiki_type': sth,
                'page': 1,
                'api_key': self.api_key
                }

        rlt = []
        itemFactory = itemfactory.ItemFactory(swer)
        haveNext = True

        while haveNext:
            d = self.__getattribute__("_Search" + swer).__call__(data)

            dInfo = d['information']
            dList = d[swer + 's'] or []

            if dInfo['has_error']:
                raise Exception('Has error in search from moefou')

            for it in dList:
                rlt.append(itemFactory.Get(it))

            data['page'] += 1
            haveNext = dInfo.get('may_have_next', False)

        return rlt

    def _Search(self, wikiType, data):
        return self._Get('http://api.moefou.org/search/{}.json'.format(wikiType), data)

    def __getattribute__(self, name):
        matchGet = re.compile(r"^Get(.*?)From(.*?)$")
        if name.startswith("_Search"):
            url = name[7:].lower()
            return lambda d: self._Search(url, d)
        elif matchGet.match(name):
            t, w = map(lambda s: s.lower(), matchGet.findall(name)[0])
            return lambda n: self._GetSthFromSwer(sth=t, swer=w, name=n)
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

