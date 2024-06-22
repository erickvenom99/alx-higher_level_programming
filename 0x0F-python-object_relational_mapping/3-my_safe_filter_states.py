#!/usr/bin/python3
import MySQLdb
import sys

def fetch_allrow(cursor, state_name):
    """
    """
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql_query, (state_name,))
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