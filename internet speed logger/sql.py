import sqlite3


class SQL:
    def __init__(self, DB_Name):
        self.conn = sqlite3.connect(f'{DB_Name}.db')
    # record table creation

    def CreateRecordTable(self):
        self.conn.execute('''CREATE TABLE record
                (ID         INTEGER     PRIMARY KEY     AUTOINCREMENT,
                up          INTEGER     NOT NULL,
                down        INTEGER     NOT NULL,
                ping        INTEGER     NOT NULL,
                tStamp      INTEGER     NOT NULL);''')
        print("Record table created successfully")
        self.Commit()

    # comparision table creation
    def SqlAddDet(self, up, down, ping, tstamp):
        self.conn.execute("INSERT INTO record (up,down,ping,tStamp) VALUES ({0},{1}, {2}, {3})".format(
            up, down, ping, tstamp))
        self.Commit()

    # quarying table
    def QuaryRecordMaster(self):
        SUB = self.SqlQuaryExec("""select up,down,ping,tStamp
                                from record;""")
        return SUB

    # Mics
    def SqlQuaryExec(self, quary):
        c = self.conn.cursor()
        c.execute(quary)
        return(c.fetchall())

    def Commit(self):
        self.conn.commit()


if __name__=="__main__":
    SQL("database").CreateRecordTable()