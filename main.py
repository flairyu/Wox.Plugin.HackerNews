# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from wox import Wox

class DictClass(Wox):

    def query(self,query):
        proxies = {}
        if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
            proxies = {
              "http": "http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
              "http": "https://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))
            }
            #self.debug(proxies)

        url = 'http://dict.baidu.com/s?wd=' + query
        r = requests.get(url, proxies = proxies)
        bs = BeautifulSoup(r.text)
        c = bs.select('#empty-body')
        results = []
        for i in c:
            results.append({
                "Title": i.find('strong').text,
                "SubTitle": i.find('p').text,
                "IcoPath":"Images/app.ico",
                "ContextData": "ctxData",
            })
        return results
    
    def context_menu(self, data):
        results = []
        results.append({
            "Title": "Context menu entry",
            "SubTitle": "Data: {}".format(data),
            "IcoPath":"Images/app.ico"
        })
        return results

if __name__ == "__main__":
    DictClass()
