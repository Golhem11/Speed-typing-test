import sys
import time
import random

def get_sentence():
    f = open('text.txt').read()
    text = f.split(".")
    text = random.choice(text)
    return text[1:]

def start():
    print("This is your sentence.")
    sentence = get_sentence() + "."
    print(sentence)
    input("Press enter to start the test.")
    start = time.time()
    user_input = input()
    end = time.time()
    print("TOTAL TIME : " + str(end - start))
    correct_chars = 0
    i = 0
    for char in user_input:
        if char == sentence[i]:
            correct_chars+=1
        i+=1
    accuracy = (correct_chars*100) / len(sentence)
    print("ACCURACY :  " + str(accuracy))
    
while True:
    start()
    input("Press enter to restart the test.")
