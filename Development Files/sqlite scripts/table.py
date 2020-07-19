import sqlite3

conn = sqlite3.connect('root_table.db');
print("Opened database correctly!");

conn.execute('''CREATE TABLE ROOT_TABLE
        (ID TEXT PRIMARY KEY NOT NULL,
        ROOT    TEXT NOT NULL,
        FORM_1  TEXT NOT NULL,
        FORM_2  TEXT NOT NULL,
        FORM_3 TEXT NOT NULL,
        FORM_4 TEXT NOT NULL,
        FORM_5 TEXT NOT NULL,
        FORM_6 TEXT NOT NULL,
        FORM_7 TEXT NOT NULL,
        FORM_8 TEXT NOT NULL,
        FORM_9 TEXT NOT NULL,
        FORM_10 TEXT NOT NULL,
        FORM_11 TEXT NOT NULL,
        FORM_12 TEXT NOT NULL);''')

print("Table created succesfully");

conn.close
