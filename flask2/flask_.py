from flask import *

app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template("webshop_main page.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/catalog')
def catalog():
    return render_template("catalog.html")

@app.route('/kos')
def kos():
    return render_template("kos.html")

@app.route('/towel')
def towel():
    return render_template("towel.html")

@app.route('/hello')
def hello():
    return '''
        <html>
            <body>
                <h1>Здесь HTML разметка</h1>
                <p>Немного тектса тут и там</p>
            </body>
        </html>'''

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)


if __name__ == '__main__':
    app.run(debug=True) 