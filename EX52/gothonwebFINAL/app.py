from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map1

app = Flask(__name__)

@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map1.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene)
    else:
        # The user doesn't have a session...
        # What should your code do in response?
        return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    if 'scene' in session:
        if userinput is None:
            # Weird, a POST request to /game with no user input... what should your code do?
            return render_template('you_died.html')
        else:
            currentscene = map1.SCENES[session['scene']]
            nextscene = currentscene.go(userinput)
            if nextscene is None:
                # There's no transition for that user input.
                # what should your code do in response?
                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene)
    else:
        # There's no session, how could the user get here?
        # What should your code do in response?
        return render_template('you_died.html')

# This URL initializes the session with starting values
@app.route('/')
def index():
    session['scene'] = map1.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get

app.secret_key = '\xd0Oi\x9d\x9e\xcd\xfb\xe4\x9f{h\xb8\x89Mo7d\x90\x14\xe6\x95\xc7\xa6|'

if __name__ == "__main__":
    app.run()
