"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
        <title></title>
      </head>
      <body>
      Hi! This is the home page.
      <a href="/hello">Hello</a>
      </body>
    </html>
    """


@app.route('/hello', methods=["GET"])
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit"><br>
          Select your compliment:<br>
          <input type="radio" name="awesomeness" value="awesome">AWESOME</input><br>
          <input type="radio" name="awesomeness" value="terrific">TERRIFIC</input><br>
          <input type="radio" name="awesomeness" value="fantastic">FANTASTIC</input><br>
          <input type="radio" name="awesomeness" value="neato">NEATO</input><br>
          <input type="radio" name="awesomeness" value="oh-so-not-meh">OH-SO-NOT-MEH</input><br>
          <input type="radio" name="awesomeness" value="ducky">DUCKY</input><br>
          <input type="radio" name="awesomeness" value="coolio">COOLIO</input><br>
        </form>
        <br>Or choose:<br>
        <form action="diss_person">
          What's your name <input type="text" name="person">
          <input type="submit" value="Submit"><br>
          Select your insult:<br>
          <input type="radio" name="insults" value="bald">BALD</input><br>
          <input type="radio" name="insults" value="smelly">SMELLY</input><br>
          <input type="radio" name="insults" value="illiterate">ILLITERATE</input><br>
          <input type="radio" name="insults" value="pig">PIG</input><br>
          <input type="radio" name="insults" value="oh-so-meh">OH-SO-MEH</input><br>
          <input type="radio" name="insults" value="lame">LAME</input><br>
          <input type="radio" name="insults" value="boring">BORING</input>
        </form>
      </body>
    </html>
    """


@app.route('/greet', methods=["GET"])
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    # compliment = awesomeness
    awesomeness = request.args.get('awesomeness')

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {awesomeness}!
      </body>
    </html>
    """.format(player=player, awesomeness=awesomeness)
      # , compliment=compliment)


@app.route('/diss_person', methods=["GET"])
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    insults = request.args.get('insults')

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {insults}!
      </body>
    </html>
    """.format(player=player, insults=insults)
      # , compliment=compliment)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
