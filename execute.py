from func import db
import os

def file_to_str(directory, file_name):
    file = directory + file_name
    string = open(file, 'r').read()

    return string

cursor, connection = db.rds_connect("aurora")
#contact_prod = file_to_str(os.getcwd() + "\\query\\import\\", "company.sql")

department_id = ["'43e2600c-d3fa-44a3-8679-507f0c16e1e4'", "'a837e79d-978b-49e8-b7a7-bcba1150b0b1'", "'f2f555ed-b8a6-4191-9d97-51b901c79792'", "'46f41c73-e34d-4a04-8fae-8b4e52ebbf19'", "'1fb191d0-c99d-4060-a72e-61f4d5644245'", "'c977f955-a7f6-4c35-8502-8125eea7c37c'", "'c910426a-5fa1-46f0-aa5f-864fa1ccf2ea'", "'2528fa2e-1a6b-424a-9c68-e5f9b66aba41'", "'b0f91fa1-d6b0-4ff0-adf3-bf209a2d1ab1'", "'76ea4a2b-b42f-4f90-b293-182c9e7fc443'", "'bb527e03-4ffe-401a-a9a0-adb2c13c3d6d'", "'1fab500a-b1fc-42fd-9249-f50aca33647d'", "'927f1777-8d40-473c-93f5-9188a62bd19b'", "'92adb43c-d107-4905-b666-4d79482cacfa'", "'a6d62dd9-d0f7-4b4b-bcb1-2204846a96cc'", "'b0570184-dbb4-499b-80f5-4802b48805d3'", "'63cefd41-2db3-4fc8-b491-512fbeed8dc9'"]
'''
for dpt in department_id:
    print("Processing {}.".format(dpt))
    try:
        res = cursor.execute(contact_prod.format(dpt))
        print(cursor.rowcount)
        connection.commit()
    except Exception as e:
        print(e)
        pass
'''

res = cursor.execute("select * from ig_master.department")
rows = cursor.fetchall()
for i in rows:
    print(i[0])
print(cursor.rowcount)