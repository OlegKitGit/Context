import string
import re
import sqlite3
from datetime import datetime, date, time


def add_to_base(input_string, text, source):

    if input_string != '':

        con = sqlite3.connect("Knowledgebase.db")
        cur = con.cursor()

        statement_date = datetime.now().strftime("%Y%m%d%H%M%S")

        sql = """"""
        output_string = ''

        pattern = r'^([-+0-9a-zа-я\s]+)\=\s([-+0-9a-zа-я\s]+)'
        p = re.compile(pattern)

        result = re.match(p, input_string)

        if result:
            result.group(1)
            result.group(2)

            sql = sql + """INSERT INTO Equivalence (statement, name, equivalent) VALUES ('""" + statement_date + """', '""" + result.group(1) + """', '""" + result.group(2) + """');"""
            if text != '\n':
                sql = sql + """INSERT INTO Text (statement, name) VALUES ('""" + statement_date + """', '""" + text + """');"""
            if source != '':
                sql = sql + """INSERT INTO Source (statement, name) VALUES ('""" + statement_date + """', '""" + source + """');"""
            cur.executescript(sql)
            task_commit = print("\nYour statement was successfully entered in the database")
            cur.close()
            con.commit()
            con.close()
            return 'Ok'
            
        pattern = r'\<([-+0-9a-zа-я\s]+)'
        p = re.compile(pattern)

        result = re.findall(p, input_string)

        if result:

            result[0] = result[0].strip()
            text = text.replace("'", '')

            input_string = input_string.split(',')
            concepts = []
            for i in input_string:
                if '<' + result[0] != i.strip():
                    concepts.append(i.strip())

            sql = sql + """INSERT INTO Context (statement, name) VALUES ('""" + statement_date + """', '""" + result[0] + """');"""
            if text != '\n' and '\n\n' and '\n\n\n':
                sql = sql + """INSERT INTO Text (statement, name) VALUES ('""" + statement_date + """', '""" + text + """');"""
            if source != '':
                sql = sql + """INSERT INTO Source (statement, name) VALUES ('""" + statement_date + """', '""" + source + """');"""

            if concepts != []:
                for i in concepts:
                    sql = sql + """INSERT INTO Concept (statement, name) VALUES ('""" + statement_date + """', '""" + i + """');"""

            cur.executescript(sql)
            task_commit = print("\nYour statement was successfully entered in the database")
            cur.close()
            con.commit()
            con.close()
            return 'Ok'

        else:
            input_string = input_string.split(',')
            text = text.replace("'", '')
            concepts = []
            for i in input_string:
                concepts.append(i.strip())

            if concepts != []:
                for i in concepts:
                    sql = sql + """INSERT INTO Concept (statement, name) VALUES ('""" + statement_date + """', '""" + i + """');"""

            if text != '\n':
                sql = sql + """INSERT INTO Text (statement, name) VALUES ('""" + statement_date + """', '""" + text + """');"""
            if source != '':
                sql = sql + """INSERT INTO Source (statement, name) VALUES ('""" + statement_date + """', '""" + source + """');"""

            cur.executescript(sql)
            task_commit = print("\nYour statement was successfully entered in the database")
            cur.close()
            con.commit()
            con.close()
            return 'Ok'
