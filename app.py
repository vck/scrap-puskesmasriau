#!/usr/bin/env python
# coding=utf-8

from urllib2 import urlopen
from bs4 import BeautifulSoup as bs

def fetchdata():
    soup = bs(urlopen("http://gsb.riau.go.id/index.php?act=Profil&task=puskesmas2"))
    exception = [' Non Rawat Inap', 'Sumber : Dinas Kesehatan Provinsi Riau', ' Rawat Inap']
    text = [x.text.encode('ascii').strip('()') for x in soup.find_all("i") if x.text not in exception]
    return text


