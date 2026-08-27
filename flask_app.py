import os
from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder=os.path.abspath('templates'),
    static_folder=os.path.abspath('static'),
)

