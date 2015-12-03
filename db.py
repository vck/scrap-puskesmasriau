#!/usr/bin/env python
# coding=utf-8

import MySQLdb
from app import fetchdata
from config import *


print 'connecting to database...'
db = MySQLdb.connect(host, username, password, db)
print 'connected to database'
cur = db.cursor()

print 'checking database...'
cur.execute('DROP TABLE IF EXISTS puskesmas')
print 'creating table for puskesmas_scraper'
sql_table = """CREATE TABLE puskesmas (
             id MEDIUMINT NOT NULL AUTO_INCREMENT,
            address TEXT NOT NULL,
            PRIMARY KEY (id)
            ) ENGINE=MyISAM;"""
cur.execute(sql_table)
print 'table for puskesmas_scraper created successfully'

print 'fetching data and insert to database, now!'
for item in fetchdata():
    sql = """INSERT INTO puskesmas(id, address) VALUES (NULL, "{}")""".format(item)
    cur.execute(sql)
    db.commit()
    print "data input succed!"

print "done!"
