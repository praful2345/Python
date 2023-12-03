#import instaloader
#a  = instaloader.Instaloader()
#print(a)
#a.download_profile('praful.punde')"


#Generate OTP
#random --> get random numbers
#time --> time module to get time along
import random
import time
#help(time)
#a = random.randint(1,15)
#print(a)
#Wanted to repeat multiple time random numbers --> Control block -->  for loop
#'''
#for<loop_var> in collectn/range:
#statment(s)...'''
#for i in range(5):
#print(i)

#Number guessing game
##n = random.randint(1,10)
###lets take input
##guess = int(input("Enter the number"))
##print(guess)
##while n!= guess:
##    if guess < n:
##        print("Low number")
##        guess = int(input("Enter again"))
##        elif guess> n:
##            print("high number")
##            guess = int(input("Enter again"))
##            print("Yup got it")

##import pyqrcode
##import png
###lets give link
##link = "https://pypi.org/project/PyQRCode/"
##qr = pyqrcode.create(link)
###print(qr)
##qr.png("pypi.png",scale = 10)

# Text to speech conversion
import gtts
from gtts import gTTS
t = gTTS("Hope u are enjoy python",lang='fr')
print(t)
#finally save to audio file
t.save("pph1.mp3")


