# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 13:17:30 2021

@author: mrbar
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/resume')
def Resume():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(port = 5000)