from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
import json

def create_app(configfile=None):
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        layers = {}
        arguments = {}
        with open('layers.json') as data_file:    
            layers = json.load(data_file)
        with open('arguments.json') as data_file:    
            arguments = json.load(data_file)
        return render_template('index.html', layers = layers, arguments=arguments)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
