import ast
import random
from pathlib import Path
#from ascii_magic import AsciiArt #converting images to Asciiart :D 
from art import *

DICNAME = "xthat.dic"
OUTFILE = "log.txt"

def load_lines(filename: str):
    with open(filename) as f:
        your_list = f.read().splitlines()
    return your_list

def save_prompt(prompt: str, response: str):
    #try and open file, create it if it doesn't exist
    #write the line to file in a tuple of {name:prompt}
    #close - maybe print writing successful, or there was an error
    with open(OUTFILE, "a") as f:
        ###check file exists and create a csv if not

        #write to the file
        f.write("\""+prompt+"\",\""+response+"\"")
    print("Response recorded.")
        

def main():
    print(text2art("Welcome \nto \nxThat."))
    print("xThat is a playful mini game generator for anyone looking to create their own mini game.\n\nTo make a game we will:\n1. provide you with a title for your game\n2. prompt you for a subtitle\n3. prompt you for 4 bullet points for game play.")
    #ask if they want an example - then show them screw that.
    line_list = load_lines(DICNAME)
    prompt = line_list[random.randrange(len(line_list)-1)].upper()
    print(text2art(prompt + " THAT", font="small"))
    print("Enter a subtitle")
    subtitle = input()
    print("Enter a prompt")
    response = input()
    print("You said: " + response)
    save_prompt(prompt, subtitle, response)




if __name__ == "__main__":
    main()
