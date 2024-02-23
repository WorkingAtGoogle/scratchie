import random
import time
import pyttsx3

engine = pyttsx3.init()


class Scratch:
    def __init__(self):
        print("Running Scratch For Python!")
    def say(self, string):
        print(string)
    def ask(self, string):
        answer  = input(string + " ")
        return answer
    def pick_random(self, num1, num2):
        return random.randint(num1, num2)
    def join(self, str1, str2):
        return  str1 + str2
    def contains(self, string, char):
        if char in string:
            return True
        else:
            return False
    def  wait(self, secs):
        time.sleep(secs)
    def lengthof(self, string):
        return len(string)
    def letterof(self, num, string):
        return  string[num-1]
    def speak(self, text):
        engine.say(text)
        engine.runAndWait()




