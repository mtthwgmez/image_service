from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads'                           # your upload folder path

@app.route('/upload', methods=['POST'])
def upload_image():

    # if no such file
    if 'image' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['image']
    filename = secure_filename(file.filename)                       # for security
    filepath = f"{app.config['UPLOAD_FOLDER']}/{filename}"
    file.save(filepath)
    
    return {'filename': filename, 'path': filepath}, 200

@app.route('/edit', methods=['POST'])
def edit_image():
    # get operation and filepath from request
    operation = request.json.get('operation')
    filepath = request.json.get('filepath')

    img = Image.open(filepath)

    if operation == 'rotate':
        angle = request.json.get('angle', 90)
        img = img.rotate(angle, expand=True)                        # expand to fit the whole rotated image
    elif operation == 'resize':
        size = request.json.get('size', (800, 600))
        img = img.resize(size)
    elif operation == 'crop':
        box = request.json.get('box')
        img = img.crop(box)

    filename = os.path.basename(filepath) 
    output_name = f"edited_{filename}"
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_name)
    img.save(output_path)
    return {'edited_path': output_path}, 200

@app.route('/convert', methods=['POST'])
def convert_format():
    try:
        filepath = request.json.get('filepath')
        target_format = request.json.get('format', 'JPEG').upper()              # default to JPG

        img = Image.open(filepath)
        filename = os.path.basename(filepath)
        filename_no_ext = os.path.splitext(filename)[0]
        output_name = f"converted_{filename_no_ext}.{target_format.lower()}"
        output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_name)

        # transparency handling for PNG to JPEG conversion
        if target_format.upper() == 'JPEG' and img.mode == 'RGBA':
            img = img.convert('RGB')
        
        img.save(output_path, target_format.upper())
        return {'converted_image': output_path, 'format': target_format}, 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(host='127.0.0.1', port=5001, debug=True)