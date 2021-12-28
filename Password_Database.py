import sqlite3

connectivity = sqlite3.connect('Master.db')

cursor = connectivity.cursor()

#cursor.execute("""CREATE TABLE Master_Password(
       #Master_pass text     
 #)""")

connectivity.commit()
connectivity.close()
