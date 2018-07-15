#  -*- coding:  utf-8  -*-

import sqlite3

con = sqlite3.connect("Knowledgebase.db")
cur = con.cursor()

sql = """\

CREATE TABLE Concept (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statement INTEGER,
    name TEXT
);

CREATE TABLE Context (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statement INTEGER,
    name TEXT,
    concept TEXT
);

CREATE TABLE Text (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statement INTEGER,
    name TEXT
);

CREATE TABLE Equivalence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statement INTEGER,
    name TEXT,
    equivalent TEXT
);

CREATE TABLE Source  (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    statement INTEGER,
    name TEXT
);

"""
try:
    cur.executescript(sql)
except sqlite3.DatabaseError as err:
    print(err)
else:
    print('Ok')

cur.close()
con.close()
