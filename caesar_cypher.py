import sys

#ord() function converts a character to its ASCII value while chr() converts an ASCII value to its corresponding character
Z = ord("Z") 
A = ord("A")

def caesar_cypher(text, key):
    text = text.upper() # convert text to upper
    cyphered_text = ""
    char_counter = 0 # will track up to five characters
    block_counter = 0 # will track up to ten blocks
    for char in text:
        if (ord(char)>=A) and (ord(char)<=Z): 
            # if the character is a letter (not punctuation or a space, for example)
            new_char_ord = ord(char)+key # the ord value of the ciphered character
            if new_char_ord > Z: 
                # if adding the key goes out of the character range, subtract 26 (no. of letters in english alphabet)
                new_char_ord -= 26
            new_char = chr(new_char_ord) # convert to a character
            char_counter += 1 # increment counter by one
            print(new_char, end="") # print out character on the same line
            if char_counter==5: # when iterated through five character
                print(" ", end="") # start printing on a new line
                char_counter = 0; # reset char_counter
                block_counter += 1 #increment block_counter
            if block_counter == 10: # when iterated through ten blocks
                print() # start printing on a new line
                block_counter = 0 # reset block_counter

key = int(sys.argv[1])%26 # read the key for cyphering from the terminal, find its modulo%26 to ensure it is between 0-25

if __name__=="__main__":
    for line in sys.stdin:
        caesar_cypher(line, key)

