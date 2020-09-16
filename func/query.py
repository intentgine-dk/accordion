from func import db

cursor, connection = db.db_connect("aurora")

def get_max_date(schema, table):
    query = """
            select 
                max(delivery_date::date)
            from {0}.{1};
            """.format(schema, table)

    row = cursor.execute(query)
    rows = row.fetchone()

    for process_date in rows:
        print(process_date)
    
