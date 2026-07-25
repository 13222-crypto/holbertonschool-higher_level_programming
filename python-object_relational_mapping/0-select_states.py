#!/usr/bin/python3
"""
This module connects to a MySQL database using MySQLdb and fetches
all records from the 'states' table sorted in ascending order by id.
"""
import sys
import MySQLdb


def select_states():
    """
    Connects to a MySQL database using command line arguments
    and lists all states sorted by states.id ASC.
    """
    if len(sys.argv) < 4:
        return

    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_passwd,
        db=db_name,
        charset="utf8"
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    select_states()
