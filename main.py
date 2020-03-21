# -*- coding: utf-8 -*-

# import requests
# from bs4 import BeautifulSoup
# import webbrowser
from wox import Wox

class DictClass(Wox):

    def query(self,query):
        # proxies = {}
        # if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
        #     proxies = {
        #       "http": "http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
        #       "http": "https://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))
        #     }
            #self.debug(proxies)
        results = []
        results.append({
            "Title": "Hello World",
            "SubTitle": "Query: {}".format(query),
            "IcoPath":"Images/app.ico",
            "ContextData": "ctxData"
        })
        return results
        # r = requests.get('https://news.ycombinator.com/',proxies = proxies)
        # bs = BeautifulSoup(r.text)
        # results = []
        # for i in bs.select(".comhead"):
        #     title = i.previous_sibling.text
        #     url = i.previous_sibling["href"]
        #     results.append({"Title": title ,"IcoPath":"Images/app.ico","JsonRPCAction":{"method": "openUrl","parameters":[url],"dontHideAfterAction":True}})

        # return results

    # def openUrl(self,url):
    #     webbrowser.open(url)
    #     #todo:doesn't work when move this line up 
    #     WoxAPI.change_query(url)
    
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
