import sqlite3


def edit_link(statement):
    if statement.isdigit():
        con = sqlite3.connect("Knowledgebase.db")
        cur = con.cursor()
        sql_concepts = """SELECT name FROM Concept WHERE statement = """ + statement + """"""
        cur.execute(sql_concepts)
        concepts = cur.fetchall()
        concepts = [x[0] for x in concepts]
        sql_delete = """DELETE FROM Concept WHERE statement = """ + statement + """"""
        cur.execute(sql_delete)
        sql_context = """SELECT concept, name FROM Context WHERE statement = """ + statement + """"""
        cur.execute(sql_context)
        context = cur.fetchall()
        sql_delete = """DELETE FROM Context WHERE statement = """ + statement + """"""
        cur.execute(sql_delete)
        if context:
            links = context[0][0] + ', <' + context[0][1]
            for concept in concepts:
                if concept != context[0][0]:
                    links = links + ', ' + concept
        else:
            links = ''
            for concept in concepts:
                if links != '':
                    links = links + ', ' + concept
                else:
                    links = concept
        sql_text = """SELECT name FROM Text WHERE statement = """ + statement + """"""
        cur.execute(sql_text)
        text = cur.fetchall()
        if text:
            text = text[0][0]
        else:
            text = ''
        sql_delete = """DELETE FROM Text WHERE statement = """ + statement + """"""
        cur.execute(sql_delete)
        sql_source = """SELECT name FROM Source WHERE statement = """ + statement + """"""
        cur.execute(sql_source)
        source = cur.fetchall()
        if source:
            source = source[0][0]
        else:
            source = ''
        sql_delete = """DELETE FROM Source WHERE statement = """ + statement + """"""
        cur.execute(sql_delete)
        cur.close()
        con.commit()
        con.close()
        return links, text, source

        
        
