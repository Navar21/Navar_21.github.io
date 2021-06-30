# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:17:30 2021

@author: mrbar
"""
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route('/EdwinNavar.com')
def Resume():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))

if __name__ == '__main__':
    app.run(port = 5000)