#type: ignore
import board #pins library
import digitalio #led library
import time #delay library

led = digitalio.DigitalInOut(board.GP0) #led delcaration
led.direction = digitalio.Direction.OUTPUT #led as output

MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}

while True:
    print("Enter your message or -q to quit")
    message = input().upper() #takes uppercase input
    morse = ""
    if message == "-Q": #uppercase exit test
        break
    for letter in message: #for each character in message
        if letter == " ": #breaks word if space
            morse = morse + ("/ ")
        else: #adds morse code for letter to morse translation
            morse = morse + (MORSE_CODE[letter] + " ")
    print(f"Translation:{morse}") #prints translation
    for character in morse: #blinks morse code
            if character == ".": #blinks for dot
                led.value = True
                time.sleep(.25)
                led.value = False
                time.sleep(.25)
            if character == "-": #blinks longer for dash
                led.value = True
                time.sleep(.75)
                led.value = False
                time.sleep(.25)
            if character == "/": #waits for space
                time.sleep(1.75)
