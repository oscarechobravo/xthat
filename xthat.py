import ast
import random
from pathlib import Path

DICNAME = "xthat.dic"

def load_lines(filename: str):
    with open(filename) as f:
        your_list = f.read().splitlines()
    return your_list

def save_prompt(prompt: str):
    #try and open file, create it if it doesn't exist
    #write the line to file in a tuple of {name:prompt}
    #close - maybe print writing successful, or there was an error

def main():
    line_list = load_lines(DICNAME)
    print(line_list[random.randrange(len(line_list)-1)].upper() + " THAT")
    print("Enter a prompt")
    prompt = input()
    print("You said: " + prompt)




if __name__ == "__main__":
    main()
