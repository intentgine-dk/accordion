from func import db

cursor, connection = db.db_connect("aurora")

def get_max_date(schema, table):
    query = """
            select 
                max(delivery_date::date)
            from {0}.{1};
            """.format(schema, table)

    rows = cursor.execute(query)
    row = rows.fetchone()

    return row
    
def get_campaign_id(campaign, client):
    query = """
            select
                campaign_id
            from ig_business.campaign cmp
            where 
                trim(upper(campaign_name)) = trim(upper({0}))
                and client = {1}
            """.format(campaign, client)

    rows = cursor.execute(query)
    row = rows.fetchone()

    return row