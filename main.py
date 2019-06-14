from flask import Flask, render_template, request, jsonify
from lib import predict

import inspect
import io

app = Flask(__name__)

@app.route('/', methods=['GET'])
def upload():
    return render_template('upload.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    image = request.files['image'].read()
    res = predict.get_prediction(image)
    dic = None

    if (len(res.payload) == 0):
        print('nothing')
    else:
        tmp = 0
        predict_class = None
        print(res)
        for result in res.payload:
            if (tmp < result.classification.score):
                tmp = result.classification.score
                predict_class = result
        dic = {
            'result': {
                'score': predict_class.classification.score,
                'name': predict_class.display_name
            }
        }

    return jsonify(dic)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)