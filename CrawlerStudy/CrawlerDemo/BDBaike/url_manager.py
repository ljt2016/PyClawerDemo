'''
Created on 2017年4月6日

@author: Magister
'''


class UrlManager(object):
    
    #Initialize UrlManager with two empty URL sets old_urls set and new_urls set.
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
    #add a new url to new URL set
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        
    #add a new set of urls
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    
    def has_next_url(self):
        return len(self.new_urls) != 0

    
    def get_new_url(self):
        ret_url = self.new_urls.pop()
        self.old_urls.add(ret_url)
        return ret_url

    

    
    
    
    
    
    
    
    
    
    



