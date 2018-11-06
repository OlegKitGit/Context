<<<<<<< HEAD:Create_Database.py
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
=======
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
>>>>>>> 82621972fa04c6511a74e42b5d1c62cace449b1d:create_database.py
