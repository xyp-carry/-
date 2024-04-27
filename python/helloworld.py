from flask import Flask, request, jsonify
from flask_cors import CORS
from split_s import split_Chinese,split_history

app = Flask(__name__)
CORS(app)
@app.route('/api1/data', methods=['POST','GET'])
def receive_data():
    data = request.json
    if len(data['历史内容']) > 0:
        words = split_history(data['历史内容'])
    else:
        words = split_Chinese(data['当前内容']) # 仅对当前内容进行解析
    return jsonify({"message": words})

def process_data(data):
    # 这里处理数据，例如转换数据、计算等
    return {'processed': data}

if __name__ == '__main__':
    app.run()