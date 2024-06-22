#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa
"""

import MySQLdb
import sys


def fetch_allrow(cursor, state_name):
    """Fetch all rows from the 'states' table \
    where the name matches the given state_name.
    """
    sql_query = "SELECT * FROM states WHERE name = '{}'".format(state_name)
    cursor.execute(sql_query)
    all_states = cursor.fetchall()
    return all_states


if __name__ == '__main__':
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            password=password,
            db=database
        )

        cursor = conn.cursor()
        rows = fetch_allrow(cursor, state_name)
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        cursor.close()
        conn.close()
