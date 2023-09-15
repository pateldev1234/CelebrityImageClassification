from flask import Flask ,request ,jsonify
import util
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/classify_image",methods = ['GET','POST'])
def classify_image():
    image_data = request.form['image_data']
    print("===================================================")
    response = util.classify_image(image_data)
    # print("--" * 4)
    print(response)
    # print("--" * 6)
    # if len(response) != 0:
    #     response = jsonify(response[0])
    # else: 
    #     response = {

    #     }
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin','*')
    print(response)
    print("##########################")
    return response
if __name__== "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)