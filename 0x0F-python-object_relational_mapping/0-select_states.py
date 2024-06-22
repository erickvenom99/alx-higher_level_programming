#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def fetch_allrow(cursor):
    """Fetch all rows from the 'states' table."""
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")
    all_states = cursor.fetchall()
    return all_states


def display_states(all_states):
    """Print the states in the format (id, 'name')."""
    for state in all_states:
        print("({}, '{}')".format(state[0], state[1]))


if __name__ == '__main__':
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset='utf8'
        )

        cursor = conn.cursor()
        all_states = fetch_allrow(cursor)
        display_states(all_states)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
