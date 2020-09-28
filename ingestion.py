import os
import json
import pandas as pd
from datetime import date, timedelta, datetime
from func import db, gdrive, tools, query, date_func, notif


current_date = date.today()
g_auth = gdrive.google_auth()
cols = db.load_conf("client_column")
dir_id = db.load_conf("directory_id")
cursor, connection = db.db_connect("aurora")


def run_delivered_leads(gdrive_dir):
    df = pd.DataFrame()
    directory_id = dir_id[gdrive_dir.lower()]
    #max_date = query.get_max_date('ig_test', 'delivered_tci')
    max_date = '2020-09-21'
    start_date = datetime.strptime(max_date, '%Y-%m-%d').date()
    
    for process_date in date_func.daterange(start_date, current_date):
        print("Processing {}".format(process_date))

        raw_files = gdrive.list_files(g_auth, directory_id, process_date)
        for raw_file in raw_files:
            try:
                gdrive.dl_file_name(g_auth, directory_id, raw_file)
            except Exception as e:
                notif.ingestion_mail("GDrive Download Error", "Error downloading {}".format(raw_file))
                pass

            df = tools.file_to_df(raw_file)
            df.columns = map(str.lower, df.columns)
            df_cols = json.loads(cols[gdrive_dir.lower()])
            for key, value in df_cols.items():
                df.rename(columns = {key: value}, inplace = True)

            for key in df.columns:
                if key not in df_cols.values():
                    del df[key]

            for key in df.columns:
                if len(df[key].value_counts()) == 0:
                    del df[key]

            df['source_file'] = raw_file
            df['delivery_date'] = process_date
            df['client_id'] = gdrive_dir
            #df['campaign_id'] = query.get_campaign_id(df['campaign'], df['client_id'])
            df['campaign_id'] = '1234'

            df.to_sql('delivered_leads', connection, schema='ig_test', if_exists='append', index=False, index_label=None)

            os.remove(raw_file)
        

run_delivered_leads('GreenLeads001')