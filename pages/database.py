import sqlite3
import os
from datetime import datetime


class Database:

    DATABASE_FILE = "vpn.db"
    logger = None

    @classmethod
    def empty_db(cls, conn):
        cur = conn.cursor()
        cur.execute("CREATE TABLE status (country text, status text, lp_date text, lp_time text)")
        cur.execute("CREATE TABLE history (id INTEGER PRIMARY KEY, date text, time text, country text, status text)")
        cur.execute(
            '''CREATE TABLE performance
            (id INTEGER PRIMARY KEY, date text, time text, run_id text, country text, link text, load_time text)'''
        )
        conn.commit()

    def get_db_conn(self):
        if not os.path.exists(self.DATABASE_FILE):
            conn = sqlite3.connect(self.DATABASE_FILE)
            self.empty_db(conn)
            return conn
        else:
            return sqlite3.connect(self.DATABASE_FILE)

    def update_status(self, country, status):
        db_conn = self.get_db_conn()
        try:
            cur = db_conn.cursor()
            date = datetime.now().date().__str__()
            time = datetime.now().time().replace(microsecond=0).__str__()
            cur.execute("SELECT * FROM status WHERE country = ?", (country,))
            old_data = cur.fetchone()
            if old_data:
                cur.execute("UPDATE status SET status = ? WHERE country = ?", (status, country))
            else:
                cur.execute(
                    "INSERT INTO status(country, status, lp_date, lp_time) VALUES (?, ?, ?, ?)",
                    (country, status, "-", "-")
                )
            if status:
                cur.execute(
                    "UPDATE status SET lp_date = ?, lp_time = ? WHERE country = ?", (date, time, country))
            cur.execute(
                "INSERT INTO history(date, time, country, status) VALUES (?, ?, ?, ?)",
                (date, time, country, status)
            )
            db_conn.commit()
        except Exception as db_err:
            self.logger.error(db_err)
        finally:
            db_conn.close()

    def add_perf_result(self, run_id, country, link, load_time):
        db_conn = self.get_db_conn()
        try:
            cur = db_conn.cursor()
            date = datetime.now().date().__str__()
            time = datetime.now().time().replace(microsecond=0).__str__()
            cur.execute(
                "INSERT INTO performance (date, time, run_id, country, link, load_time) VALUES (?, ?, ?, ?, ?, ?)",
                (date, time, run_id, country, link, load_time)
            )
            db_conn.commit()
        except Exception as db_err:
            self.logger.error(db_err)
        finally:
            db_conn.close()
