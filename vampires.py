# -*- coding: utf-8 -*-

#%%
import sqlite3 as lite
import sys
import os

#%%
os.getcwd()
os.chdir("D:\\github\\vampire")

#%%
conn = lite.connect("vamps.db")

with conn:
    cur = conn.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    data = cur.fetchone()
    
    print("SQLite version:", data)


#%%
con = None

try:
    con = lite.connect('test.db')
    cur = con.cursor()

    cur.execute('SELECT SQLITE_VERSION()')

    data = cur.fetchone()

    print("SQLite Version: %s", data)

except lite.Error, e:
    print("Error %s:", %e.args[0])
    sys.exit(1)
    
finally:
    
    if con:
        con.close()