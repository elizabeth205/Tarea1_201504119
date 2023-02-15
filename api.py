from flask import Flask, request, render_template
import time, json, socket
app= Flask(__name__)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
