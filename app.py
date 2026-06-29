from flask import Flask
app =Flask(__name__)
@app.route()
def home():
  return "welcome to sound_detection"
home()
app.run(Dubug =True)
