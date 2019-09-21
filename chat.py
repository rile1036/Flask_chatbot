import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/keyboard')
def Keyboard():
	dataSend = {
		"type" : "buttons",
		"buttons" : ["인사말", "버전"]
	}
	return jsonify(dataSend)

@app.route('/message', methods = ['POST'])
def Message():
	dataReceive = request.get_json()
	content = dataReceive['content']

	if content == u"인사말":
		dataSend ={
			"message" : {
				"text" : "안녕하세요! 반갑습니다."
		}
	}
	elif content == u"버전":
		dataSend ={
			"message" : {
				"text" : "아직 프로토타입입니다."
		}
	}

	return jsonify(dataSend)

if __name__ == "__main__":
	app.run(host = '172.31.40.197', port = 5050, debug = True)
