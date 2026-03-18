from flask import Flask, request, jsonify
import model

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    file_name = data.get("file", "")

    result = model.detect(file_name)

    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)