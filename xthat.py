import ast
import random
from pathlib import Path

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
        f.write("\""+prompt+"\",\""+response+"\"")
    print("Response recorded.")
        

def main():
    line_list = load_lines(DICNAME)
    prompt = line_list[random.randrange(len(line_list)-1)].upper()
    print(prompt + " THAT")
    print("Enter a prompt")
    response = input()
    print("You said: " + response)
    save_prompt(prompt, response)




if __name__ == "__main__":
    main()
