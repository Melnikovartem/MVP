from urllib import request  #urllib.request is faster than requsets
from lxml import html       #in the future there will be our own parser
                            #now it is aviable with lxml

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'} #Why not Apple?

class xps:
    '''
    #XPath Shortcuts
    '''
    lbl = '//div[@class="kris-news-tit"]/a/div/text()'
    lnk = '//div[@class="kris-news-tit"]/a/@href'
    dat = '//div[@class="kris-news-data-txt"]/text()'
    cnt = '//div[@class="kris-redaktor-format"]'
    cnl = '//div[@class="kris-redaktor-format"]/p/a/@href'
    
class service: 
    '''
    useful class for less code in another class
    '''
    @staticmethod
    def normlisT(a, b, c):
        lst = []
        for i in range(len(a)):
            lst.append( {'date' : a[i], 'title' : b[i], 'link' : c[i]} )
        return lst
    @staticmethod
    def normlist(e):
        a = e[0]
        b = e[1]
        c = e[2]
        return service.normlisT(a, b, c)
    @staticmethod
    def gluelist(a):
        return (lambda ll: [el for lst in ll for el in lst])(a)

class Site:
    '''
    main parsing class
    '''
    url = ""
    pg = ""             #pagination
    _range = range(-1)  #range of search
    def __init__(self, url):
        self.url = url
    def __init__(self, url, pg,  _range):
        self.url = url
        self.pg = pg
        self._range = _range
    def __init__(self, url, pg,  a, b):
        self.url = url
        self.pg = pg
        self._range = range(a, b + 1)
    
    def getlist(self):
        lst = []
        if (self._range != range(-1)):
            for i in self._range:
                src = html.fromstring(request.urlopen(
                        request.Request(
                        self.url + self.pg + str(i),
                         headers = headers)).read().decode('utf-8'))
                lst.append( service.normlist(tuple ( map (src.xpath,
                                    (xps.dat, xps.lbl, xps.lnk)))))
            lst = service.gluelist(lst)
            return lst

def getData(url):
    src = html.fromstring(request.urlopen(request.Request(url, headers = headers)).read().decode('utf-8'))
  	linkTag = src.xpath(xps.cnl)
  	if(len(linkTag) > 0):
      return getData(linkTag[0])
	  else:
	      images = src.xpath('//img/@src')
	     	textBlock = src.xpath(xps.cnt)[0]
    		textSrc = []
    		for i in textBlock:
   		      textSrc.append((i.text_content().replace('\r','')).replace('\n', '').replace('\t', ''))
    return ({'text': ''.join(textSrc), 'images': images})          

def get_posts(n = 5):
    # your logic
    # last n posts
    # let n = 5
    return Site('http://lycu1580.mskobr.ru/novosti/', '?p=', 0, n).getlist()
    """
    Output format:
    [{'link': '/novosti/27_oktyabrya_2017_g_sostoyalos_ocherednoe_zanyatie_liceistov_v_tehnoparke_mosgormash/',
    'title': '27 октября 2017 г. состоялось очередное занятие лицеистов в технопарке "Мосгормаш"', 
    'date': '31.10.17'}, {...}, ..., {...} ]
    """
