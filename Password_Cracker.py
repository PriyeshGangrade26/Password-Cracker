import random # pip install Random
import pyautogui # pip install pyautogui

# All the charcter or number are present in the password 
char = "abcdefghijklmnopqrstuvwxyz0123456789"
# Converting All this character in the list 
char_list = list(char)

# on the place of enter Your password you can enter any sample passWord. 
password = pyautogui.password("Enter a password: ")

# initializing a String Guess
guess = ""

# using While loop keep comparing All the possible outcomes until We get the Right one 
while (guess!=password):
#      Defining the value of guess
    guess = random.choices(char_list, k=len(password))
    print("<============"+ str(guess) +"============>")
#     by adding this statement if our guess match with the password this if statement exectute and we come out of the while loop because of that break statement  
    if(guess == list(password)):
        print("Your password is: "+ "".join(guess))
        break