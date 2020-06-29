#Arabic_Roots


print("Welcome to Arabic Roots. This program is designed to return the meaning of a bi, tri, or quadrilateral arabic root. You are provided with a key to input each root letter below.");
print("Alif - 0627, Ba - 0628, Ta - 062A, Tha - 062B, Jeem - 062C, Ha - 062D, Kha - 062E, Dal - 062F, Dhal - 0630, Ra - 0631, Zay - 0632, Seen - 0633, Sheen - 0634, Sad - 0635, Dod - 0636, Tta - 0637, Ttha - 0638, Ain - 0639, Ghayn - 063A, Fa - 0641, Qaf - 0642, Kaf - 0643, Lam - 0644, Meem - 0645, Nun - 0646, Haa - 06D5, Waw - 0648, Ya - 064A");
user_input = input("Enter an Arabic root:");
letter_list = user_input.split(" ");
arabic_letter_list = [];
for letter in letter_list:
    arabic_letter_list.append((chr(int(letter, 16))))
print(arabic_letter_list);

#code needs a check to see if letters are correct.
#check_1 = input("Are these the correct letters? y or n.")
#if check_1 == 'n':

for word in dictionary:
    if word = arabic_word:
        print(word[0:])
    else
        print("That word is not in the dicionary yet.")
