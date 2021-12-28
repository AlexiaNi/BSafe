import sqlite3

connectivity = sqlite3.connect('Pass.db')
cursor = connectivity.cursor()

#cursor.execute("""CREATE TABLE Passes(
#       Platform text,
#       URL text,
#       Password text     


#  )""")

connectivity.commit()
connectivity.close()