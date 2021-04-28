from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/short-url', methods=['GET','POST'])
def short_url():
  if request.method == 'POST':
    return render_template('short_url.html', code = request.form['code'])
  else:
    return 'This is not valid, yet.'
