import pyttsx3
engine=pyttsx3
engine.speak("Enter the first value ")
a=int(input("Enter the first number " ))
engine.speak("Enter the second value ")
b=int(input("Enter the second number "))
engine.speak("Enter the third value ")
c=int(input("Enter the third number "))
engine.speak("Enter the fourth value ")
d=int(input("Enter the fourth number "))
if a<b and a<c and a<d:
    print("The smallest number is ",a)
    engine.speak("The smallest value is ")
    engine.speak(a)
if b<a and b<c and b<d:
    print("The smallest NUmber is ",b)
    engine.speak("The smallest value is ")
    engine.speak(b)
if c<a and c<b and c<d:
    print("The samllest number is ",c)
    engine.speak("The smallest value is ")
    engine.speak(c)
if d<a and d<b and d<c:
    print("The smallest number is ",d)
    engine.speak("The smallest value is ")
    engine.speak(d)
