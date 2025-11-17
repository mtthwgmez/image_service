# image_service
image microservice for CS361. It provides 1.upload 2.edit(rotate, resize, crop) 3.convert functions.

# Install dependencies
pip install -r requirements.txt

# start the service
python photo_app.py

api_endpoint =      `http://127.0.0.1:5001`

# upload function
Endpoint:           `POST /upload`
Request:            
            Form Data:
            {
                "image": <file>
            }
Response:           
            {
                "filename": "YOUR_IMAGE_FILE",
                "path": "./app.config['UPLOAD_FOLDER']/YOUR_IMAGE_FILE"
            }

# edit function
Endpoint:           `POST /edit`
Request:            
            {
                "filepath": "./uploads/YOUR_IMAGE_FILE",
                "operation": "rotate" | "resize" | "crop",
                "angle": 90,                                        // for rotate only
                "size": [200, 200],                                 // for resize only
                "box": [100, 100, 400, 400]                         // for crop only (left, top, right, bottom)
            }
Response:           
            {
                "edited_path": "./app.config['UPLOAD_FOLDER']/edited_YOUR_IMAGE_FILE"
            }

# convert function
Endpoint:           `POST /convert`
Request:            
            {
                "filepath": "./uploads/YOUR_IMAGE_FILE",
                "format": "PNG" | "JPEG" | "BMP" | "WEBP" | "GIF"
            }
Response:           
            {
                "converted_image": "./app.config['UPLOAD_FOLDER']/converted_YOUR_IMAGE_FILE.png",
                "format": "PNG"
            }

<img width="581" height="342" alt="Image_Service drawio" src="https://github.com/user-attachments/assets/0f5ba136-e9ac-4c5c-9bde-b6ac382a9aed" />






