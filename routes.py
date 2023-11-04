from app import app_func
from Open_AI import openai_prompt # open ai api prompt

from flask import Flask, render_template, request
app = Flask(__name__,template_folder="templates",static_folder="static")
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/')
def home():
   return render_template('index.html')







@app.route('/data', methods = ["GET", "POST"])
def gfg():
   if request.method == "POST":
      global value
      value = request.form.get("message")
      print(value)
      text_file = open("text.txt", "w")
      n = text_file.write(value)
      text_file.close()
      app_func()
   return render_template("index.html")


# combined both input and button so 
# they send together regardless
# still having using of words not saving correctly for openai prompt! Sometimes using old text instead of new.





if __name__ == '__main__':
   app.run(use_reloader=True)

