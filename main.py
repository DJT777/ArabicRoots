#!/usr/bin/env python
#Arabic_Roots



#Arabic Roots is a program I have written to help me study different texts in Arabic.
#The Arabic language is based on a three letter root system.
#Some words have up to 12 meanings based on their forms, all of which are distinct.
#This program allows a user to enter a root and retrieve the meanings of each form from a database of roots


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
# engine = create_engine('sqlite:///home/dylan/Documents/projects/ArabicRoots/ArabicRoots/DICTIONARY.db')
engine = create_engine('sqlite:///DICTIONARY.db')
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
    # user_input = input("Enter an Arabic root:")
    # letter_list = user_input.split(" ")
    letter_list = ['0633', '0631', '062F']
    arabic_letter_list = []
    for letter in letter_list:
        arabic_letter_list.append((chr(int(letter, 16))))
    arabic_letters_string = ''.join(map(str, reversed(arabic_letter_list)))
    print(arabic_letters_string)

    class word(base):
        __tablename__ = 'DICTIONARY'

        id = Column(Integer, primary_key=True)
        word = Column(String)
        definition = Column(String)
        is_root = Column(Boolean)
        #parent_id = Column(Integer, ForeignKey('word.word'))

        def __repr__(self):
            return "id='%s'\nword='%s'\ndefinition='%s'\nis_root='%s'\n" \
            % (str(self.id), self.word, self.definition, self.is_root)

    for instance in session.query(word).all():
        # print(instance.word, " ", arabic_letters_string)
        if instance.word == arabic_letters_string:
            print(instance)
        else:
            continue


if __name__ == "__main__":
    main()
