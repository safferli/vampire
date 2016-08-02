# -*- coding: utf-8 -*-

#%%
import sqlite3 as lite
# import sys
import os

#%%
os.getcwd()
#os.chdir("D:\\github\\vampire")
os.chdir("/home/csafferling/Documents/github/vampire")

conn = lite.connect("vampires_dus.db")

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
with open("vampires.py", 'rb') as file:
    exec(file.read())

# read connections data from connections.py
with open("connections.py", 'rb') as file:
    exec(file.read())

# generate sqlite DBs
with conn:
    cur = conn.cursor()
    # generate vampires db
    cur.execute("DROP TABLE IF EXISTS Vampires")
    cur.execute("CREATE TABLE Vampires(Id INTEGER PRIMARY KEY, Nickname TEXT, Firstname TEXT, Lastname TEXT, Clan TEXT, Covenant  TEXT, Bloodline TEXT, Misc TEXT)")
    cur.executemany("INSERT INTO Vampires VALUES(?, ?, ?, ?, ?, ?, ?, ?)", vamps)
    # generate connections db
    cur.execute("DROP TABLE IF EXISTS Connections")
    cur.execute("CREATE TABLE Connections(from_id INTEGER, to_id INTEGER, bi_directional INTEGER, connection_type TEXT, connection_details TEXT, start_date TEXT, end_date TEXT, misc TEXT)")
    cur.executemany("INSERT INTO Connections VALUES(?, ?, ?, ?, ?, ?, ?, ?)", connections)

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
