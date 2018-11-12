import string
import re
import sqlite3
from itertools import groupby


def get_from_base(input_string):

    if input_string != '':

        con = sqlite3.connect("Knowledgebase.db")
        cur = con.cursor()

        list_of_original_names = []
        list_of_original_names_sort = []

        pattern = r'^([-+0-9a-zа-я\s]+)$'
        p = re.compile(pattern)

        result = re.match(p, input_string)

        if result:
            sql = """SELECT statement, name FROM Concept WHERE statement IN (SELECT statement FROM Concept WHERE name = '""" + result.group(1) + """')"""
            cur.execute(sql)
            list_of_names = cur.fetchall()
            link_name = []
            links = []
            for i in list_of_names:
                    link_name.append(i[1])
                    for j in list_of_names[:]:
                            if i != j:
                                    if i[0] == j[0]:
                                            link_name[list_of_names.index(i)] = link_name[list_of_names.index(i)] + ", " + j[1]
                                            list_of_names.remove(j)
                    links.append((i[0], link_name[list_of_names.index(i)]))
            sql = """SELECT statement, name FROM Text WHERE statement IN (SELECT statement FROM Concept WHERE name = '""" + result.group(1) + """')"""
            cur.execute(sql)
            list_of_names = cur.fetchall()
            for name in list_of_names:
                list_of_names[list_of_names.index(name)] = (name[0], '\n' + name[1][:-1])  #----------------------------------------
            links = links + list_of_names
            #k = 0
            list_of_links = []
            for i in links:
                list_of_links.append('----------------------------------------')
                list_of_links.append(i[1])
                for j in links[:]:
                    if i != j:
                        if i[0] == j[0]:
                           list_of_links.append(j[1])
                           #k += 1
                           links.remove(j)
                           #if k > 0:
                           #    list_of_links.remove(i[1])
                           #    k = 0
            list_of_original_names = list_of_links
            cur.close()
            con.commit()
            con.close()
            return list_of_original_names
            
        pattern = r'^([-+0-9a-zа-я][-+0-9a-zа-я\s]+)\,\s\<([-+0-9a-zа-я\s]+)$'
        p = re.compile(pattern)

        result = re.match(p, input_string)

        if result:
            sql = """SELECT name FROM Concept WHERE statement IN (SELECT statement FROM Context WHERE concept = '""" + result.group(1) + """' AND name = '""" + result.group(2) + """')"""
            cur.execute(sql)
            list_of_names = cur.fetchall()
            for name in list_of_names:
                if name[0] != result.group(1):
                    list_of_original_names.append(name[0])
            cur.close()
            con.commit()
            con.close()
            return list_of_original_names

        else:
            input_string = input_string.split(',')
            concepts = []
            for i in input_string:
                concepts.append(i.strip())
            counter = 0
            if concepts != []:
                for concept in concepts:
                    if counter > 0: 
                        sql = sql + """ AND statement IN (SELECT statement FROM Concept WHERE name = '""" + concept + """')"""
                        sql_text = sql_text + """ AND statement IN (SELECT statement FROM Concept WHERE name = '""" + concept + """')"""
                        sql_source = sql_source + """ AND statement IN (SELECT statement FROM Concept WHERE name = '""" + concept + """')"""
                    else:
                        sql = """SELECT statement, name FROM Concept WHERE (statement IN (SELECT statement FROM Concept WHERE name = '""" + concept + """')"""
                        sql_text = """SELECT statement,name FROM Text WHERE (statement IN (SELECT statement FROM Concept WHERE name = '""" + concept + """')"""
                        sql_source = """SELECT statement,name FROM Source WHERE (statement IN (SELECT statement FROM Concept WHERE name = '""" + concept + """')"""
                        counter = 1
                sql = sql + """)"""
                sql_text = sql_text + """)"""
                sql_source = sql_source + """)"""
                cur.execute(sql)
                list_of_names = cur.fetchall()
                cur.execute(sql_text)
                list_of_texts = cur.fetchall()
                cur.execute(sql_source)
                list_of_sources = cur.fetchall()
                link_name = []
                links = []
                for i in list_of_names:
                    link_name.append(i[1])
                    for j in list_of_names[:]:
                        if i != j:
                            if i[0] == j[0]:
                                link_name[list_of_names.index(i)] = link_name[list_of_names.index(i)] + ", " + j[1]
                                list_of_names.remove(j)
                    links.append((i[0], link_name[0]))
                links = links + list_of_texts + list_of_sources
                list_of_links = []
                for i in links:
                    list_of_links.append(str(i[0]))
                    list_of_links.append('----------------------------------')
                    list_of_links.append(i[1])
                    list_of_links.append('----------------------------------')
                    for j in links[:]:
                        if i != j:
                            if i[0] == j[0]:
                               list_of_links.append(j[1])
                               list_of_links.append('----------------------------------')
                               links.remove(j)                     
                cur.close()
                con.commit()
                con.close()
                return list_of_links
