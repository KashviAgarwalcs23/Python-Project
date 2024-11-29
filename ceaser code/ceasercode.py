alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from ceaser_art import logo
print(logo)
def ceaser(start_text,shift_amount,cypher_direction):
    end_text=""
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            if cypher_direction=="encode":
                #oR
                #shift_amount *= -1 with this there is no need for else statement but use if in starting before the for loop
                new_position=position+shift_amount
            else:
                new_position=position-shift_amount
            new_letter=alphabet[new_position]
            end_text += new_letter
        else :
            end_text += char
    print(f"The {direction}d text is {end_text}")
still_continue=True
while still_continue == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceaser(text,shift,direction)
    result = input("Type yes if you want to continue otherwise no\n").lower()
    if result=="no":
        still_continue=False
        print("Goodbye")