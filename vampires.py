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

# (8): ID, nickname, firstnames, lastname, clan, covenant, bloodline, misc
vamps = [
    # PCs are single-digit (hopefully...)
    (1, None, "Hauke", "Hinnrichs", "Nosferatu", "Ordo Dracul", None, None),
    (2, None, "Valeria", "von Vyborg", "Ventrue", "Invictus", None, None),
    (3, "Capt'n Ahab", "Sven", "Unterberg", "Mekhet", "Ordo Dracul", None, None),
    (4, "Thomas", "Thomas", "Du Bois", "Gangrel", None, None, None),
    (5, None, None, None, None, None, None, None),
    (6, None, None, None, None, None, None, None),
    (7, None, None, None, None, None, None, None),
    (8, None, None, None, None, None, None, None),
    (9, None, None, None, None, None, None, None),
    # NPCs start here, IDs are auto-incremented
    (None, None, "Werner", "Rosenberg", "Daeva", "Ordo Dracul", None, None)
    ]

# generate vampire db
with conn:
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS Vampires")
    cur.execute("CREATE TABLE Vampires(Id INTEGER PRIMARY KEY, Nickname TEXT, Firstname TEXT, Lastname TEXT, Clan TEXT, Covenant  TEXT, Bloodline TEXT, Misc TEXT)")
    cur.executemany("INSERT INTO Vampires VALUES(?, ?, ?, ?, ?, ?, ?, ?)", vamps)    
    
# examine db
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM Vampires")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# http://www.pythoncentral.io/introduction-to-sqlite-in-python/
# http://zetcode.com/db/sqlitepythontutorial/ (python2)
