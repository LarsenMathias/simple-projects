import pyttsx3
engine=pyttsx3
engine.speak("Please Enter the first value ")
a=int(input("Enter the first number "))
engine.speak("Please Enter the second value ")
b=int(input("Enter the second numbber "))
engine.speak("Enter the third value ")
c=int(input("Enter the third number "))
x=(a+b+c)/3
engine.speak("The average of the three numbers is")
engine.speak(x)
print("The average of the three numbers is",x)

