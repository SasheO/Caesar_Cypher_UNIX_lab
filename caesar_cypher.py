import sys

Z = ord("Z")
A = ord("A")

def caesar_cypher(text):
    text = text.upper()
    cyphered_text = ""
    counter = 0
    block = 0
    for char in text:
        if (ord(char)>=A) and (ord(char)<=Z):
            new_char_ord = ord(char)+n
            if new_char_ord > Z:
                new_char_ord -= 26
            new_char = chr(new_char_ord)
            counter += 1
            print(new_char, end="")
            if counter==5:
                counter = 0;
                block += 1
                print(" ", end="")
            if block == 10:
                print()
                block = 0

n = int(sys.argv[1])%26

if __name__=="__main__":
    for line in sys.stdin:
        caesar_cypher(line)

