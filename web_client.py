import urllib2

__author__ = 'gingray'


class WebClient:
    def __init__(self):
        self.opener = urllib2.build_opener()
        self.encoding = None
        self.use_encoding = True
        self.connection_timeout = None
        self.opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0"),
                                  ("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8")]

    def get(self, url):
        if self.encoding is None:
            self.encoding = "utf-8"
        if self.connection_timeout is None:
            self.connection_timeout = 2
        response = self.opener.open(url, None, self.connection_timeout)
        data = response.read()
        if self.use_encoding:
            return data.decode(self.encoding)
        return data