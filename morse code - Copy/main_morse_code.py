from morse_code_logo import intro, exit
from morse_code_list_conversion import dict1
import time
print(intro)
print("\n")
print("""NOTE:\n1.While encoding, enter the message continuously as a single sentence.\n2.While decoding use space between letters in the word""")
print("\n")

def convert_to_morse_code():
    message = input("enter the sentence: \n").upper()
    encoded_message = ""
    for letter in message:
        for key in dict1: 
            if letter == key:
                encoded_message = encoded_message + dict1[letter] + " "
    if letter not in dict1:
        print("Sorry! morse code does not exist for the input.")
    print(encoded_message)
#convert_to_morse_code()


def convert_from_morse_code():
    list1 = []
    decoded_code = ''
    code = input("enter the message to be decoded:\n")
    list1 = code.split(" ") 
    # print(list1)
    for i in list1:
        for keys in dict1:
            if i == dict1[keys]:
                decoded_code += keys
                #print(decoded_code)
    if i not in dict1[keys]:
        print("Invalid input")
    print(decoded_code)
#convert_from_morse_code()


still_continue = True
while still_continue:
    choose = input(
        "enter whether you want to encode or decode the message otherwise enter stop: ").lower()
    if choose == "encode":
        convert_to_morse_code()
    elif choose == "decode":
        convert_from_morse_code()
    elif choose == "stop":
        print(exit)
        time.sleep(3)
        still_continue = False
    else:
        print("try again")
