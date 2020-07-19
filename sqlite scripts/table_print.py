import sqlite3

conn = sqlite3.connect('root_table.db')
print('Opened database succesfully!')

#conn.execute(''' INSERT INTO ROOT_TABLE (ROOT, FORM_1) VALUES (' \u0633 \u0631 \u062F ', 'Form 1 - To study')''');

#conn.commit()
#print('Inserted new word succesfully')

cursor = conn.execute("SELECT * from ROOT_TABLE")
for row in cursor:
    print("ROOT = ", row[0])
    print("FORM_1 = ", row[1])

print("Operation done succesfully!")

#, FORM_2, FORM_3, FORM_4, FORM_5, FORM_6, FORM_7, FORM_8, FORM_9, FORM_10, FORM_11, FORM_12)

# 'Form 2 - To teach', 'Form 3 - to study together with something', 'Form 4: ', 'Form 5: ', 'Form 6: to study carefully together', 'Form 7: to become or be wiped out, blotted out, extinguished, 'Form 8:', 'Form 9: ', 'Form 10: ', 'Form 11: ', 'Form 12: ')
