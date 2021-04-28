from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return 'This is a URL shortener to test out Flask! It turns out Flask is surprisingly similar to Sinatra, but also has a few distinctions. Overall, it\'s clean and simple to use.'
