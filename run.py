"""
    Run the flask application, either in local or live mode.
"""
import argparse
from flask import Flask
from waitress import serve
from app.routes import webapp

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Help Message", 
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("-e", "--env",  help="running environment",  required=True)

    args = parser.parse_args()
    env = args.env
    if env == 'local':
        webapp.run(host='0.0.0.0', port=5000, debug=True)
    else:
        serve(webapp, host='0.0.0.0', port=5000)

