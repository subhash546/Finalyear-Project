import sqlite3
print('HIIIIII')
class example:
    def __init__(self):
        conn = sqlite3.connect('database.db')
        print ("Opened database successfully");
        conn.execute('INSERT INTO students(name,college) values("DP", "AEC")')
        print ("INSERTED successfully");
        conn.commit()
        conn.close()
        
ex=example()
print('byeeeee')