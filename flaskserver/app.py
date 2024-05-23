# from flask import Flask, request, jsonify
# import pickle
# import numpy as np
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# # Load the trained model once when the application starts
# model = None
# model_path = './rfc_model.pkl'
# try:
#     with open(model_path, 'rb') as file:
#         model = pickle.load(file)
# except FileNotFoundError:
#     print(f"Error: Model file not found at {model_path}")
# except EOFError:
#     print(f"Error: Model file is corrupted at {model_path}")

# @app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     features = [data['main_temp'], data['visibility'], data['wind_speed'], 985, 28, 966, 1014]
#     prediction = model.predict(np.array(features).reshape(1, -1))[0]
#     return jsonify({'prediction': int(prediction)})


# if __name__ == '__main__':
#     app.run(port=5000, debug=True)  # Set the port to 5000




from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model once when the application starts
model = None
model_path = './rfc_model.pkl'
try:
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    print(f"Error: Model file not found at {model_path}")
except EOFError:
    print(f"Error: Model file is corrupted at {model_path}")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        data['main_temp'],
        data['visibility'],
        data['wind_speed'],
        data['pressure'],
        data['humidity'],
        966,  # grnd_level
        1014  # sea_level
    ]
    prediction = model.predict(np.array(features).reshape(1, -1))[0]
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # Set the port to 5000
