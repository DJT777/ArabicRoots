import sqlite3
import tqdm
connection = sqlite3.connect("DICTIONARY.db")

cursor = connection.cursor()

sql_command = "create_table.sql"


def open_and_execute_line_by_line(sqlfile):
    lines = [line for line in open(sqlfile, 'r')]
    for line in tqdm.tqdm(lines):
        print(line)
        cursor.execute(line)

def open_and_execute(sqlfile):
    lines = ''.join([line for line in open(sqlfile, 'r')])
    cursor.execute(lines)

open_and_execute("create_table.sql")
open_and_execute_line_by_line("dictionary.sql")
connection.commit()
connection.close()
