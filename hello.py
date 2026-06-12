import functools

# save this as hello.py
from flask import Flask
import random

app = Flask(__name__)

print(random.__name__)
print(__name__)

def default_decorator_skeleton(func):
    # copies the original function's __name__, __doc__, and other
    # metadata onto wrapper_function
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        # Do sth before
        result = func(*args, **kwargs)
        # Do sth after
        return result
    return wrapper_function


# <b>Text</b>
def make_bold(func):
    # copies the original function's __name__, __doc__, and other
    # metadata onto wrapper_function
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        # Do sth before
        result = func(*args, **kwargs)
        # Do sth after
        return f"<b>{result}</b>"
    return wrapper_function


# <em>Text</em>
def make_emphasis(func):
    # copies the original function's __name__, __doc__, and other
    # metadata onto wrapper_function
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        # Do sth before
        result = func(*args, **kwargs)
        # Do sth after
        return f"<em>{result}</em>"
    return wrapper_function


# <u>Text</u>
def make_underlined(func):
    # copies the original function's __name__, __doc__, and other
    # metadata onto wrapper_function
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        # Do sth before
        result = func(*args, **kwargs)
        # Do sth after
        return f"<u>{result}</u>"
    return wrapper_function


@app.route("/")   # "/" says go to homepage
def hello():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph</p>')
            # '<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqyAJk3im_aL3MPsgLtLceerEFjr-3r8Jtv7hq1XpI2Q&s=10">')


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    """returns Bye!"""
    return "Bye!"

# @app.route("/username/<name>")
# @app.route("/username/<path:name>")
# @app.route("/username/<path:name>")
# @app.route("/developerdefined/<path:name>")
# @app.route("/username/<string:name>")
@app.route('/post/<int:post_id>')
def post(post_id):
    return f"Here is the post_id:{post_id}"

@app.route("/username/<path:name>")
@make_bold
@make_emphasis
@make_underlined
def greet(name):
    # return f"Hello there {name + 12}!"
    return f"Hello there {name}!"

#if the __name__ belongs to the file that's being run (it's not imported)
if __name__ == '__main__': # __main__ denotes the file that's being run
    # does the same thing we did on Terminal (by writing
    # "export FLASK_APP=hello.py" and "flask run" to the Terminal)
    app.run(debug=True)

