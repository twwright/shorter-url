from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
app.secret_key = "crossfit"

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/short-url', methods=['GET','POST'])
def short_url():
  if request.method == 'POST':
    urls = {}

    if os.path.exists('urls.json'):
      with open('urls.json') as url_file:
        urls = json.load(url_file)

    if request.form['code'] in urls.keys():
      flash('Sorry, that short name has already been taken. Try again.')
      return redirect(url_for('home'))

    urls[request.form['code']] = {'url':request.form['url']}
    with open('urls.json', 'w') as url_file:
      json.dump(urls, url_file)
    return render_template('short_url.html', code = request.form['code'])
  else:
    return redirect(url_for('home'))
