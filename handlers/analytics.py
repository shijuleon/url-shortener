import sqlite3
import datetime

class URLAnalytics():
    # a relational database would be better for this task
    # Schema
    # id, added_on, hits

    def __init__(self):
        self.conn = sqlite3.connect("analytics.db")

    def initDB(self):
        self.conn.execute('''CREATE TABLE analytics
         (ID INT PRIMARY KEY     NOT NULL,
         short_token TEXT NOT NULL,
         date_added           TEXT    NOT NULL,
         hits           INT    NOT NULL''')

    def insert(self, short_token):
        timeNow = datetime.datetime.now()
        hits = 0
        self.conn.execute("INSERT INTO analytics (short_token, date_added, hits) \
      VALUES ('{0}', '{1}', {2})".format(short_token, timeNow, hits))

    def getHits(self, short_token):
        cursor = self.conn.execute("SELECT hits from analytics where short_token={0}".format(short_token))
        for row in cursor:
            return row[0]