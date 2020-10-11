import username_gen
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('index.html')



@app.route('/username/')
def give_username():
    username = username_gen.generate_username()
    return render_template('username_giver.html', username=username)

if __name__ == "__main__":
    app.run()