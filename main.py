# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import webbrowser
from wox import Wox,WoxAPI

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
        #c = bs.select('#empty-body')
        c = bs.select('.tab-content')
        results = []
        for index, i in enumerate(c):
            if not i.find('p'):
                break
            results.append({
                "Title": str(index+1)+":",
                "SubTitle": i.find('p').text.strip().replace("\n",""),
                "IcoPath":"Images/app.ico",
                "JsonRPCAction":{
                #You can invoke both your python functions and Wox public APIs .
                #If you want to invoke Wox public API, you should invoke as following format: Wox.xxxx
                #you can get the public name from https://github.com/qianlifeng/Wox/blob/master/Wox.Plugin/IPublicAPI.cs,
                #just replace xxx with the name provided in this url
                "method": "openUrl",
                #you MUST pass parater as array
                "parameters":[url],
                #hide the query wox or not
                "dontHideAfterAction":True
                }
            })
        if not results and query:
            results.append({
                "Title": query,
                "SubTitle": "未能找到数据",
                "IcoPath":"Images/app.ico",
                "ContextData": "ctxData"
            })
        return results

    def openUrl(self,url):
        webbrowser.open(url)
        #WoxAPI.change_query(url)

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
