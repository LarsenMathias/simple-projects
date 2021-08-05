import pyttsx3
engine=pyttsx3
engine.speak("Enter the first value ")
a=int(input("Enter the first number "))
engine.speak("Enter the second value ")
b=int(input("Enter the second number "))
engine.speak("Enter the third value ")
c=int(input("Enter the third number "))
if (b<=c) and (a<=c):
    biggest=c
elif (c<=a) and (b<=a):
    biggest=a
else:
    biggest=b
engine.speak("The biggest value is ")
print("The biggest value is ",biggest)
engine.speak(biggest)
