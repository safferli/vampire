# -*- coding: utf-8 -*-

#%%
import sqlite3 as lite
import sys
import os

#%%
os.getcwd()
os.chdir("D:\\github\\vampire")

conn = lite.connect("vamps.db")

#%%
# with takes care of connection closing, and error handling already!
# with also auto-commits changes to the db
with conn:
    cur = conn.cursor()
    cur.execute("SELECT SQLITE_VERSION()")
    data = cur.fetchone()
    
    print("SQLite version: %s" % data)

#%%


    


