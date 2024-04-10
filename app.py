import json
from common.Token import*
from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/', methods=["GET"])
def obtenertoken():
    datatoken = generar_token('Martin', '123')
    var_token = datatoken['token']
    response = {
        "statusCode":200,
        "body":json.dumps(var_token)
    }
    return jsonify(response)


@app.route('/verificaciontoken', methods=["GET"])
def verificaciontoken():
    token=request.headers['Authorization']
    token=token.replace('Bearer',"")
    token=token.replace("","")
    vf=verificar_token(token)
    print(f"vf=>{vf}")



    return jsonify(vf)


if __name__ == "__main__":
    app.run(debug=True)