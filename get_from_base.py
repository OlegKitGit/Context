import string
import re
import sqlite3


def get_from_base(input_string):

    if input_string != '':

        con = sqlite3.connect("Knowledgebase.db")
        cur = con.cursor()

        list_of_original_names = []

        pattern = r'^([-+0-9a-zа-я\s]+)$'
        p = re.compile(pattern)

        result = re.match(p, input_string)

        if result:
            sql = """SELECT name FROM Concept WHERE statement IN (SELECT statement FROM Concept WHERE name = '""" + result.group(1) + """')"""
            cur.execute(sql)
            list_of_names = cur.fetchall()
            for name in list_of_names:
                if name[0] != result.group(1):
                    list_of_original_names.append(name[0])
            cur.close()
            con.commit()
            con.close()
            return list_of_original_names
            
        pattern = r'^([-+0-9a-zа-я][-+0-9a-zа-я\s]+)\,\s\<([-+0-9a-zа-я\s]+)$'
        p = re.compile(pattern)

        result = re.match(p, input_string)

        if result:
            sql = """SELECT name FROM Concept WHERE statement IN (SELECT statement FROM Context WHERE concept = '""" + result.group(1) + """"' AND name = '""" + result.group(2) + """"')"""
            cur.execute(sql)
            list_of_names = cur.fetchall()
            print(list_of_names)
            for name in list_of_names:
                if name[1] != result.group(1):
                    list_of_original_names.append(name[1])
            cur.close()
            con.commit()
            con.close()
            return list_of_original_names

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
