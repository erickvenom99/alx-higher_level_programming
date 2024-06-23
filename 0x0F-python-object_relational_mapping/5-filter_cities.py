#!/usr/bin/python3
"""
Module  script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def fetch_allrow(cursor, state_name):
    """
    Fetch city names from the cities table based on the provided state name.
    Args:
        cursor: MySQL cursor object.
        state_name: Name of the state to filter by.
    Returns:
        List of city names.
    """
    cursor.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
    """, (state_name,))
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

        city_names = [row[0] for row in rows]
        print(*city_names, sep=", ")

    except MySQLdb.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
