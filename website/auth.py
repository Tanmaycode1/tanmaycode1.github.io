from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user
import sqlite3
import random
import os
import subprocess as sp

auth = Blueprint('auth', __name__)



@auth.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@auth.route('/run', methods=['GET', 'POST'])
def run():
    import detection as d
    d.main()
    return redirect(url_for("auth.home"))

@auth.route('/stop', methods=['GET', 'POST'])
def stop():
    p = sp.Popen(["python","detection.py"], stdout=sp.PIPE)
    p.terminate()
    return redirect(url_for("auth.yoga"))

