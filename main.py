#!/usr/bin/env python
#Arabic_Roots

#thanks for making the main python file I will work towards moving everything over to that file.

#This code needs to be revised so that there are 3 inputs from the user for each letter. Code will also be written to allow 2 or 4 letters in the future development.
#Furthermore this code need to take each input turn it into the arabic letter as a string, then cocatenate with the two other inputs to produce a word. Arabic is tricky on letter connection as those are unique characters when connecting individual letters.
#That word will be stored in an MySQL database as a primary key where the forms of that root I-XII are stored along with the meaning.

#Must developed a MySQL database of at least 5 arabic roots with their XII conjugated forms.

#Must learn to query database and search primary key column for the root, then when it is found print to the user in the terminal Forms I-XII as stored in the table.
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('sqlite:///arabicroots.db')
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()

def main():
    print('''
        Welcome to Arabic Roots. 
        This program is designed to return the meaning of a bi, tri, or quadrilateral arabic root. 
        You are provided with a key to input each root letter below.
        ''')
    print("Alif - 0627, Ba - 0628, Ta - 062A, Tha - 062B, Jeem - 062C, Ha - 062D, Kha - 062E, Dal - 062F, Dhal - 0630, Ra - 0631, Zay - 0632, Seen - 0633, Sheen - 0634, Sad - 0635, Dod - 0636, Tta - 0637, Ttha - 0638, Ain - 0639, Ghayn - 063A, Fa - 0641, Qaf - 0642, Kaf - 0643, Lam - 0644, Meem - 0645, Nun - 0646, Haa - 06D5, Waw - 0648, Ya - 064A");
    user_input = input("Enter an Arabic root:")
    letter_list = user_input.split(" ")
    arabic_letter_list = []
    for letter in letter_list:
        arabic_letter_list.append((chr(int(letter, 16))))
    arabic_letters_string = ' '.join(map(str, arabic_letter_list))
    #print(arabic_letters_string)

    class word(base):
        __tablename__ = 'arabic_roots'

        id = Column(Integer, primary_key=True)
        root = Column(String)
        form_1 = Column(String)
        form_2 = Column(String)
        form_3 = Column(String)
        form_4 = Column(String)
        form_5 = Column(String)
        form_6 = Column(String)
        form_7 = Column(String)
        form_8 = Column(String)
        form_9 = Column(String)
        form_10 = Column(String)
        form_11 = Column(String)
        form_12 = Column(String)

        def __repr__(self):
            return "<User(root='%s', form_1='%s', form_2='%s', form_3='%s', form_4='%s', form_5='%s', form_6='%s', form_7='%s', form_8='%s', form_9='%s', form_10='%s', form_11='%s', form_12='%s')>" % (
                                self.root, self.form_1, self.form_2, self.form_3, self.form_4, self.form_5, self.form_6, self.form_7, self.form_8, self.form_9, self.form_10, self.form_11, self.form_12)

    for instance in session.query(word):
        if instance.root == arabic_letters_string:
            print(instance)
        else:
            break


if __name__ == "__main__":
    main()
