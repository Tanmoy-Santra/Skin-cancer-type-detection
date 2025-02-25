


# from flask import Flask, request, jsonify
# from flask_cors import CORS
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# import tensorflow as tf
# import io
# from PIL import Image
# import os
# import logging

# # Set up logging
# logging.basicConfig(level=logging.DEBUG)

# app = Flask(__name__)
# CORS(app, origins=["http://localhost:5173", "https://cancer-one.vercel.app"])

# # Load the saved model
# logging.debug("Loading model...")
# model = load_model('MobileNetV2.keras')
# logging.debug("Model loaded successfully.")

# # Define the target image size
# IMAGE_SIZE = (224, 224)

# # Class labels and their benign/malignant status
# CLASS_NAMES = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']
# CLASS_STATUS = {
#     'akiec': 'Malignant',
#     'bcc': 'Malignant',
#     'bkl': 'Benign',
#     'df': 'Benign',
#     'mel': 'Malignant',
#     'nv': 'Benign',
#     'vasc': 'Benign'
# }

# def load_and_preprocess_image(file):
#     try:
#         img = Image.open(io.BytesIO(file.read()))
#         img = img.resize(IMAGE_SIZE)
#         img_array = image.img_to_array(img)
#         img_array = np.expand_dims(img_array, axis=0)
#         img_array = img_array / 255.0
#         logging.debug("Image loaded and preprocessed successfully.")
#         return img_array
#     except Exception as e:
#         logging.error(f"Error processing image: {e}")
#         return None

# @tf.function
# def predict_class(img_array):
#     logging.debug("Starting prediction...")
#     predictions = model(img_array)
#     predicted_class_index = tf.argmax(predictions, axis=1)[0]
#     confidence_score = tf.reduce_max(predictions, axis=1)[0]
#     logging.debug(f"Prediction completed. Class index: {predicted_class_index}, Confidence score: {confidence_score}")
#     return predicted_class_index, confidence_score

# @app.route('/predict', methods=['POST'])
# def predict():
#     logging.debug("Received a request at /predict endpoint")
#     if 'file' not in request.files:
#         logging.error("No file part in the request.")
#         return jsonify({'error': 'No file uploaded'}), 400

#     file = request.files['file']
#     try:
#         img_array = load_and_preprocess_image(file)

#         if img_array is not None:
#             predicted_class_index, confidence_score = predict_class(img_array)
#             predicted_class = CLASS_NAMES[predicted_class_index.numpy()]
#             confidence_percentage = f"{round(float(confidence_score.numpy()) * 100, 2)}%"
#             status = CLASS_STATUS[predicted_class]
            
#             logging.debug(f"Predicted class: {predicted_class}, Confidence: {confidence_percentage}, Status: {status}")
#             return jsonify({
#                 'class': predicted_class,
#                 'confidence': confidence_percentage,
#                 'status': status 
#             }), 200
#         else:
#             logging.error("Image processing failed.")
#             return jsonify({'error': 'Image processing failed'}), 500
#     except Exception as e:
#         logging.error(f"Prediction error: {e}")
#         return jsonify({'error': 'Prediction failed'}), 500

# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host="0.0.0.0", port=port, debug=True)


from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf
import io
from PIL import Image
import os
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app, supports_credentials=True, origins=["http://localhost:5173", "https://skin-cancer-type-detection.vercel.app/"])

# Load the saved model
logging.debug("Loading model...")
model = load_model('MobileNetV2.keras')
logging.debug("Model loaded successfully.")

# Define the target image size
IMAGE_SIZE = (224, 224)

# Class labels with their full names and benign/malignant status
CLASS_NAMES = {
    'akiec': ('AKIEC', 'Actinic Keratosis'),
    'bcc': ('BCC', 'Basal Cell Carcinoma'),
    'bkl': ('BKL', 'Benign Keratosis'),
    'df': ('DF', 'Dermatofibroma'),
    'mel': ('MEL', 'Melanoma'),
    'nv': ('NV', 'Nevi'),
    'vasc': ('VASC', 'Vascular Lesion')
}

CLASS_STATUS = {
    'akiec': 'Malignant',
    'bcc': 'Malignant',
    'bkl': 'Benign',
    'df': 'Benign',
    'mel': 'Malignant',
    'nv': 'Benign',
    'vasc': 'Benign'
}

def load_and_preprocess_image(file):
    try:
        img = Image.open(io.BytesIO(file.read()))
        img = img.resize(IMAGE_SIZE)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0
        logging.debug("Image loaded and preprocessed successfully.")
        return img_array
    except Exception as e:
        logging.error(f"Error processing image: {e}")
        return None

@tf.function
def predict_class(img_array):
    logging.debug("Starting prediction...")
    predictions = model(img_array)
    predicted_class_index = tf.argmax(predictions, axis=1)[0]
    confidence_score = tf.reduce_max(predictions, axis=1)[0]
    logging.debug(f"Prediction completed. Class index: {predicted_class_index}, Confidence score: {confidence_score}")
    return predicted_class_index, confidence_score

@app.route('/', methods=['GET'])
def home():
    logging.debug("GET request received at the root endpoint")
    return jsonify({'message': 'Server is running'}), 200

@app.route('/predict', methods=['POST'])
def predict():
    logging.debug("Received a request at /predict endpoint")
    if 'file' not in request.files:
        logging.error("No file part in the request.")
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    try:
        img_array = load_and_preprocess_image(file)
        logging.debug(f"Image array shape: {img_array.shape if img_array is not None else 'None'}")

        if img_array is not None:
            predicted_class_index, confidence_score = predict_class(img_array)
            logging.debug(f"Predicted class index: {predicted_class_index.numpy()}, Confidence score: {confidence_score.numpy()}")
            
            predicted_class_key = list(CLASS_NAMES.keys())[predicted_class_index.numpy()]
            predicted_class, full_name = CLASS_NAMES[predicted_class_key]
            confidence_percentage = f"{round(float(confidence_score.numpy()) * 100, 2)}%"
            status = CLASS_STATUS[predicted_class_key]
            
            logging.debug(f"Predicted class: {predicted_class}, Full name: {full_name}, Confidence: {confidence_percentage}, Status: {status}")
            return jsonify({
                'class': f"{predicted_class} ({full_name})",
                'confidence': confidence_percentage,
                'status': status 
            }), 200
        else:
            logging.error("Image processing failed.")
            return jsonify({'error': 'Image processing failed'}), 500
    except Exception as e:
        logging.error(f"Prediction error: {e}")
        return jsonify({'error': 'Prediction failed'}), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
