import pyttsx3
engine=pyttsx3
engine.speak("Please Enter the number ")
x=input("Enter the number ")
x=int(x)
if (x>=0):
    print("The number is positive")
    engine.speak("The given number is positive")
else:
    print("the given value is negative")
    engine.speak("the given number is negtive")