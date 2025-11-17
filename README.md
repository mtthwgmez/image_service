# image_service
A Flask-based microservice for CS361 that provides image processing capabilities including upload, edit (rotate, resize, crop), and format conversion functions.

# Install dependencies
pip install -r requirements.txt

# start the service
python photo_app.py
The service will run at: `http://127.0.0.1:5001`

# Communication Contract
## upload function
Endpoint:           `POST /upload`  

How to REQUEST Data: Send a POST request with the image file as multipart/form-data.     
Form Data:
            {
                "image": <file>
            }  

How to RECEIVE Data: The service returns a JSON response with the saved file path.
Response (JSON):           
            {
                "filename": "YOUR_IMAGE_FILE",
                "path": "./app.config['UPLOAD_FOLDER']/YOUR_IMAGE_FILE"
            }  

### upload request example
```
import requests

# Upload an image file
upload_url = "http://127.0.0.1:5001/upload"
with open("path/to/your/image.jpg", "rb") as img_file:
    files = {'image': img_file}
    response = requests.post(upload_url, files=files)
```


## edit function
Endpoint:           `POST /edit`  
How to REQUEST Data: Send a POST request with JSON data specifying the operation and parameters.
Request (JSON):            
            {
                "filepath": "./uploads/YOUR_IMAGE_FILE",
                "operation": "rotate" | "resize" | "crop",
                "angle": 90,                                        // for rotate only
                "size": [200, 200],                                 // for resize only
                "box": [100, 100, 400, 400]                         // for crop only (left, top, right, bottom)
            }  

How to RECEIVE Data: The service returns a JSON response with the edited file path.
Response (JSON):           
            {
                "edited_path": "./app.config['UPLOAD_FOLDER']/edited_YOUR_IMAGE_FILE"
            }

### edit request example (Rotate)
```
import requests

edit_url = "http://127.0.0.1:5001/edit"

edit_data = {
    'operation': 'rotate',
    'filepath': './uploads/your_image.jpg',
    'angle': 45
}

response = requests.post(edit_url, json=edit_data)
```  

### edit request example (Resize)
```
import requests

edit_url = "http://127.0.0.1:5001/edit"

edit_data = {
    'operation': 'resize',
    'filepath': './uploads/your_image.jpg',
    'size': [800, 600]
}

response = requests.post(edit_url, json=edit_data)
```  

### edit request example (Crop)
```
import requests

edit_url = "http://127.0.0.1:5001/edit"

edit_data = {
    'operation': 'crop',
    'filepath': './uploads/your_image.jpg',
    'box': [100, 100, 400, 400]
}

response = requests.post(edit_url, json=edit_data)
```  

## convert function
Endpoint:           `POST /convert`  
How to REQUEST Data: Send a POST request with JSON data specifying the file path and target format.
Request (JSON):            
            {
                "filepath": "./uploads/YOUR_IMAGE_FILE",
                "format": "PNG" | "JPEG" | "BMP" | "WEBP" | "GIF"
            }  

How to RECEIVE Data: The service returns a JSON response with the converted file path and format.
Response (JSON):           
            {
                "converted_image": "./app.config['UPLOAD_FOLDER']/converted_YOUR_IMAGE_FILE.png",
                "format": "PNG"
            }  

### convert request example
```
import requests

convert_url = "http://127.0.0.1:5001/convert"

convert_data = {
    'filepath': './uploads/your_image.jpg',
    'format': 'PNG'
}

try:
    response = requests.post(convert_url, json=convert_data)

    if response.status_code == 200:
        result = response.json()
        converted_path = result['converted_image']
        format_used = result['format']
        print(f"Success! Converted to {format_used}")
        print(f"New file location: {converted_path}")
    else:
        error = response.json().get('error')
        print(f"Error: {error}")

except requests.exceptions.RequestException as e:
    print(f"Connection error: {e}")
```  

# UML
<img width="581" height="342" alt="Image_Service drawio" src="https://github.com/user-attachments/assets/0f5ba136-e9ac-4c5c-9bde-b6ac382a9aed" />






