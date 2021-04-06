dictionary = {
    'A': ".-",
    'B': "-...",
    'C': "-.-.",
    'D': "-..",
    'E': ".",
    'F': "..-.",
    'G': "--.",
    'H': "....",
    'I': "..",
    'J': ".---",
    'K': "-.-",
    'L': ".-..",
    'M': "--",
    'N': "-.",
    'O': "---",
    'P': ".--.",
    'Q': "--.-",
    'R': ".-.",
    'S': "...",
    'T': "-",
    'U': "..-",
    'V': "...-",
    'W': ".--",
    'X': "-..-",
    'Y': "-.--",
    'Z': "--..",
    '1': ".----",
    '2': "..---",
    '3': "...--",
    '4': "....-",
    '5': ".....",
    '6': "-....",
    '7': "--...",
    '8': "---..",
    '9': "----.",
    '0': "-----",
    '.': ".-.-.-",
    ',': "--..--",
    '?': "..--..",
    " ": " ",
}

#Input message from user
Message = input()
#Dictonary is in upercase so converts string characters to upers
Upercase = Message.upper()

MorseCode = ""
#goes through every letter in the morse code dictonary to see if it contains it and adds to string
try:
    for letter in Upercase:
    
        #adds to the string morsecode if letter is in it
        MorseCode += dictionary[letter]

    print(MorseCode)

except:
    print("Opps! You have entered somthing which is not apart of the morse code")

