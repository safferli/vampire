# -*- coding: utf-8 -*-

#%%
import sqlite3 as lite
# import sys
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

# read vampire data from vamps.py
with open(vamps.py, 'rb') as file:
    exec(file.read())


# generate vampire db
with conn:
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Vampires")
    cur.execute("CREATE TABLE Vampires(Id INTEGER PRIMARY KEY, Nickname TEXT, Firstname TEXT, Lastname TEXT, Clan TEXT, Covenant  TEXT, Bloodline TEXT, Misc TEXT)")
    cur.executemany("INSERT INTO Vampires VALUES(?, ?, ?, ?, ?, ?, ?, ?)", vamps)

#%%

# examine db
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Vampires")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# http://www.pythoncentral.io/introduction-to-sqlite-in-python/
# http://zetcode.com/db/sqlitepythontutorial/ (python2)
