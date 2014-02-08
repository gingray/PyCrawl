import string
from web_client import WebClient

__author__ = 'gingray'


class FetcherBase():
    def __init__(self, web_client, worker):
        self.stop = False
        self.worker = worker
        self.web_client = web_client

    def get_url(self):
        raise NotImplemented

    def process(self):
        while not self.stop:
            url = self.get_url()
            content = ""
            try:
                content = self.web_client.get(url)
            except Exception as e:
                print str(e)
            try:
                self.worker(url, content)
            except Exception as e:
                print str(e)


class RangeFetcher(FetcherBase):
    def __init__(self, web_client, worker, template, start, end):
        FetcherBase.__init__(self, web_client, worker)
        self.template = template
        self.start = start
        self.end = end

    def get_url(self):
        ret_val = self.template % self.start
        self.start += 1
        if self.start > self.end:
            self.stop = True
        return ret_val


class UrlFileFetcher(FetcherBase):
    def __init__(self, web_client, worker, filename):
        FetcherBase.__init__(self,web_client, worker)
        f = open(filename, "r")
        self.lines = f.readlines()
        f.close()
        self.start = 0
        self.end = len(self.lines)

    def get_url(self):
        url = self.lines[self.start].strip()
        self.start += 1
        if self.start >= self.end:
            self.stop = True
        return url

