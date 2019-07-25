"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():

    player_answer = request.args.get("response")


    if player_answer == "no":
        return render_template("goodbye.html")

    else:
        return render_template("game.html")

@app.route('/madlib')
def show_madlib():

    madlibs_list = ["madlib.html", "madlib2.html"]
    random_lst = choice(madlibs_list)

    person_name = request.args.get("people")
    choice_color = request.args.get("color")
    choice_noun = request.args.get("noun")
    choice_adjective = request.args.get("adjective")
    choice_noun_2 = request.args.get("noun2")
    choice_verb = request.args.get("verb")

    return render_template(random_lst, color=choice_color, noun=choice_noun,
                           person=person_name, adjective=choice_adjective, 
                           noun2=choice_noun_2, verb=choice_verb)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
