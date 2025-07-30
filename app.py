
from flask import Flask, request, jsonify
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    image = Image.open(request.files['image'].stream)
    text = pytesseract.image_to_string(image, lang='ita')
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
