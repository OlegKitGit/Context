import string
import re
import sqlite3


def get_from_base(input_string):

    if input_string != '':

        con = sqlite3.connect("Knowledgebase.db")
        cur = con.cursor()

        list_of_original_names = []

        pattern = r'^([-+0-9a-zа-я\s]+)'
        p = re.compile(pattern)

        result = re.match(p, input_string)

        if result:
            result.group(1)
            sql = """SELECT statement,name FROM Concept WHERE statement IN (SELECT statement FROM Concept WHERE name = '""" + result.group(1) + """')"""
            cur.execute(sql)
            list_of_names = cur.fetchall()
            for name in list_of_names:
                if name[1] != result.group(1):
                    list_of_original_names.append(name[1])
            cur.close()
            con.commit()
            con.close()
            return list_of_original_names
            
        pattern = r'([-+0-9a-zа-я][-+0-9a-zа-я\s]+)\,\s\<([-+0-9a-zа-я\s]+)'
        p = re.compile(pattern)

        result = re.match(p, input_string)

        if result:
            result.group(1) 
            result.group(2)

            input_string = input_string.split(',')
            concepts = []
            for i in input_string:
                if result.group(1) != i.strip() and '<' + result.group(2) != i.strip():
                    concepts.append(i.strip())

            sql = sql + """INSERT INTO Context (statement, name, concept) VALUES ('""" + statement_date + """', '""" + result.group(1) + """', '""" + result.group(2) + """');"""
            if text != '\n':
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
