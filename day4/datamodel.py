import sqlite3
import csv


class SqliteManager:
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def query_version(self):
        query = 'select sqlite_version()'
        self.cursor.execute(query)
        print(self.cursor.fetchone())

    def create_model(self):
        query = """
        create table if not exists  passwd (
            login varchar(32),
            pwd varchar(4),
            uid int,
            gid int, 
            gecos varchar(128),
            home varchar(48),
            shell varchar(24)
        )
        """
        self.cursor.execute(query)

    def dump_rows(self, rows):
        query = 'insert into passwd values (?, ?, ?, ?, ?, ?, ?)'
        self.cursor.executemany(query, rows)
        self.conn.commit()

    def select_rows(self):
        query = 'select * from passwd'
        self.cursor.execute(query)

        for row in self.cursor.fetchall():
            print(row)


    def __del__(self):
        self.conn.close()


# sqlite = SqliteManager('july07.sqlite')
# sqlite.create_model()
# sqlite.select_rows()


class CSV2DB:
    def __init__(self, csv_file, database):
        self.db = SqliteManager(database)
        self.csv_file = csv_file
        self.dump_it()

    def dump_it(self):
        with open(self.csv_file) as fp:
            rows = csv.reader(fp, delimiter=':')
            self.db.dump_rows(rows)


# CSV2DB('passwd.txt', 'july07.sqlite')
