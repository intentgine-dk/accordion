from func import db, gdrive
from datetime import date, timedelta

cursor, connection = db.rds_connect("aurora")
dir_id = db.load_conf("directory_id")
current_date = date.today()
g_auth = gdrive.google_auth()


def run_delivered_leads(g_auth, gdrive_dir, process_date):
    directory_id = dir_id[gdrive_dir.lower()]
    raw_files = gdrive.list_files(g_auth, directory_id, process_date)
    
    # Download files
    for raw_file in raw_files:
        
        try:
            gdrive.dl_file_name(g_auth, directory_id, raw_file)
        except Exception as e:
            print(e)
            pass
        
        # Get Campaign ID
        if gdrive_dir = 'TEST':
            campaign_id = str.replace('{', '').split(' ')[0]
        

run_delivered_leads(g_auth, 'TEST', current_date)
