from flask import Flask, render_template
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', the_title='Index')

@app.route('/login')
def login():
    return render_template('login.html', the_title='Login')

@app.route('/register')
def register():
    return render_template('register.html', the_title='Register')

if __name__ == '__main__':
    app.run(debug=True)
