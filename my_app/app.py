#!/usr/bin/python3

from flask import Flask
import socket
app = Flask(__name__)

hostn = socket.gethostname()

@app.route("/")
def index():
    return """
      Sample app to demo Azure DevOps for VMSS. You are currently on the Home page. <br /><br />
      <a href="/page1">Navigate to page1</a>
      <a href="/page2">Navigate to Page2</a>
      """

@app.route("/hostr")
def hostr():
    return f'Running on hostname {hostn}'

@app.route("/page1")
def page1():
    return """
      Sample app to demo Azure DevOps for VMSS. You are currently on Page1. <br /><br />
      <a href="/">Navigate to Home</a>
      <a href="/page2">Navigate to Page2</a>
      """

@app.route("/page2")
def page2():
    return """
      Sample app to demo Azure DevOps for VMSS. You are currently on Page2. <br /><br />
      <a href="/">Navigate to Home</a>
      <a href="/page1">Navigate to Page1</a>
      """



if __name__ == '__main__':
# Will make the server available externally as well
     app.run(host='0.0.0.0')
