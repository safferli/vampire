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

# list of vampires
# (8): ID, nickname, firstnames, lastname, clan, covenant, bloodline, misc
vamps = [
    # PCs are single-digit (hopefully...)
    (1, None, "Hauke", "Hinnrichs", "Nosferatu", "Ordo Dracul", None, None),
    (2, None, "Valeria", "von Vyborg", "Ventrue", "Invictus", None, None),
    (3, "Capt'n Ahab", "Sven", "Unterberg", "Mekhet", "Ordo Dracul", None, None),
    (4, "Fred", "Thomas", "Du Bois", "Gangrel", None, None, None),
    (5, None, None, None, None, None, None, None),
    (6, None, None, None, None, None, None, None),
    (7, None, None, None, None, None, None, None),
    (8, None, None, None, None, None, None, None),
    (9, None, None, None, None, None, None, None),
    # NPCs start here, IDs are auto-incremented
    (None, None, "Lucretia", None, "Mekhet", "Ordo Dracul", None, None),
    (None, None, "Nicolaus", None, None, "Ordo Dracul", None, None),
    (None, None, "Werner", "Rosenberg", "Daeva", "Ordo Dracul", None, None),
    (None, None, "Sebastian", "Radlov", "Gangrel", "Kartianer", None, None), 
    (None, None, "Baron Otto", "von Ulrich", "Mekhet", "Ordo Dracul", None, None), 
    (None, None, "Stephen", "Welsh", "Nosferatu", "Ordo Dracul", None, None), 
    (None, None, "Mara", None, None, "Ordo Dracul", None, None), 
    (None, "Uhrmacher", None, None, None, "Ordo Dracul", None, None), 
    (None, "Henri", None, None, "Daeva", "Invictus", None, None), 
    (None, None, "Elise", None, None, None, None, None),
    (None, "Donut", "Freddy", None, None, None, None, None),
    (None, "Mutter Ey", None, None, "Daeva", None, None, None),
    (None, "Wolfi", None, None, "Gangrel", None, None, None),
    (None, "Biene", None, None, "Gangrel", None, None, None),
    (None, None, "Alois", "Reynard", "Ventrue", "Invictus", None, None),
    (None, "Ratte", None, None, "Gangrel", "Invictus", None, None),
    (None, None, None, "Matsumoto", "Nosferatu", "Ordo Dracul", "Kufukuji", None),
    (None, "Architekt", "Hektor", None, None, "Ordo Dracul", None, None),
    (None, "Der Philosoph", None, None, None, "Ordo Dracul", None, None),
    (None, None, "Asmodius", "Schneider", None, "Ordo Dracul", None, None), 
    (None, None, "Markus", "Sommerfeld", "Ventrue", "Kartianer", None, None),
    (None, None, "Artur", "Braunberg", "Daeva", "Kartianer", None, None),
    (None, None, "Noach", None, "Nosferatu", None, None, None),
    (None, None, "Dr Frederik", "Austein", None, None, None, None), 
    (None, None, "Hamish", None, None, "Invictus", None, None),
    (None, None, "Amalia", "Ziller", "Ventrue", "Invictus", None, None),
    (None, None, "Anja", None, None, "Lancea Sancta", None, None),
    (None, None, "Maria", "Malgrab", "Daeva", None, None, None),
    (None, None, "Adrian", "von Langenfelden", None, "Kartianer", None, None),
    (None, None, None, "Weitenau", None, None, None, None),
    (None, None, None, "Brauner", None, None, None, None)
    #(None, None, "", "", "", None, None, None)
    ]

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
