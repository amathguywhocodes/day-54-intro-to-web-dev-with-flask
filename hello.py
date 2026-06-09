
# save this as hello.py
from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)


@app.route("/")   # "/" says go to homepage
def hello():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Bye!"

#if the __name__ belongs to the file that's being run (it's not imported)
if __name__ == '__main__': # __main__ denotes the file that's being run
    # does the same thing we did on Terminal (by writing
    # "export FLASK_APP=hello.py" and "flask run" to the Terminal)
    app.run()

