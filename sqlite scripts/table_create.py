import sqlite3

conn = sqlite3.connect('root_table.db');
print("Opened database correctly!");

conn.execute('''CREATE TABLE ROOT_TABLE
        (ROOT TEXT PRIMARY KEY NOT NULL,
        FORM_1  TEXT NULL,
        FORM_2  TEXT NULL,
        FORM_3 TEXT NULL,
        FORM_4 TEXT NULL,
        FORM_5 TEXT NULL,
        FORM_6 TEXT NULL,
        FORM_7 TEXT NULL,
        FORM_8 TEXT NULL,
        FORM_9 TEXT NULL,
        FORM_10 TEXT NULL,
        FORM_11 TEXT NULL,
        FORM_12 TEXT NULL);''')

print("Table created succesfully");

conn.close
