import os
import sys
import openai





def openai_prompt(): #generates openai prompt for picture
    my_file = open("text.txt","rt")

    contents = my_file.read()
    my_file.close()

    target = contents

    openai.api_key = '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'
    prompt = (f"Make a short detailed Image idea for {target}")

    

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages =[{"role":"user","content":prompt}]
        )
    x = f"{response}"
    f = open("Prompt.txt","r+")
    f.truncate(0)
    f.write(x)
    f.close()
    
  

def prompt_cleaner(): #cuts up prompt for only main content
    my_file = open("Prompt.txt","rt")

    contents = my_file.read()
    my_file.close()

    x = contents.find("Title")
    y = contents.find("finish_reason")
    data = contents[x:y]

    f = open("Prompt_cut.txt","r+")
    f.truncate(0)
    f.write(data)
    f.close()




