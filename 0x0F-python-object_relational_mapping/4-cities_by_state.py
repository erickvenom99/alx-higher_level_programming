#!/usr/bin/python3
"""
Module display values of the state
"""

import MySQLdb
import sys


def fetch_allrow(cursor):
    """
    Fetch all rows from the cities and states tables.
    Args:
        cursor: MySQL cursor object.
    Returns:
        List of tuples containing (city_id, city_name, state_name).
    """
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)
    all_states = cursor.fetchall()
    return all_states


if __name__ == '__main__':
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            password=password,
            db=database
        )
        cursor = conn.cursor()
        rows = fetch_allrow(cursor)
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
