from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/short-url', methods=['GET','POST'])
def short_url():
  if request.method == 'POST':
    urls = {}
    urls[request.form['code']] = {'url':request.form['url']}
    with open('urls.json', 'w') as url_file:
      json.dump(urls, url_file)
    return render_template('short_url.html', code = request.form['code'])
  else:
    return redirect(url_for('home'))
