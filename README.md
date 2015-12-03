# scrap-puskesmasriau
scraper untuk data lokasi puskesmas di Provinsi Riau.

## tentang

terdiri dari scraper yang melakukan scraping dan parsing terhadap website riau.go.id dan robot updater yang berfungsi untuk menambahkan data-data tersebut ke database.

## instalasi

 ### GNU/Linux Mint-Ubuntu
- versi python: **Python2.7**
- install modul yang diperlukan:

```
$ sudo apt-get install python-pip
$ sudo pip install -r req.txt
```

konfigurasi database, edit file config.py
kemudian masukkan host (defaultly 'localhost')
```
host = 'localhost'
username = 'root'
password = PASSWORDANDA
db = DATABASE
```

## penggunaan

`$ python db.py`

# lisensi


[![License](https://img.shields.io/packagist/l/doctrine/orm.svg)](http://www.apache.org/licenses/LICENSE-2.0.html)


```
The MIT License (MIT)

Copyright © 2015 Vicky Vernando Dasta

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```


## pengembang

`vickydasta`
