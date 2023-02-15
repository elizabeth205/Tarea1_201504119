from flask import Flask, request, render_template
from numeros import numeros
import time, json, socket
app= Flask(__name__)

numeros = []
@app.route("/sumar", methods=['POST'])
def sumar_numeros():
    resultado = int(request.json['num1'])+ int(request.json['num2'])
    print(resultado)
    return str(resultado)
    
if __name__=="__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
