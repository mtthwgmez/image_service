import requests


# TEST 1: Upload Image
print("Uploading image to the service...")

# api endpoint for the service
upload_url = "http://127.0.0.1:5001/upload"

try:
    with open("./test_upload/Manchester_by_the_Sea.jpg", "rb") as img_file:
        files = {'image': img_file}
        response = requests.post(upload_url, files=files)

    print('Status code: ', response.status_code)
    print('Reponse JSON:', response.json())
    print("\n")

    uploaded_path = response.json().get('path')

except FileNotFoundError:
    print("Test image file not found. Please ensure the file exists at the specified path.")
    uploaded_path = None
except Exception as e:
    print(f"An error occurred during upload: {e}")
    uploaded_path = None

# TEST 2: Edit Image (Rotate)
if uploaded_path:
    print("\nEditing image (rotate)...")

    edit_url = "http://127.0.0.1:5001/edit"

    edit_input = {
        'operation': 'rotate',
        'filepath': uploaded_path,
        'angle': 45
    }

    response = requests.post(edit_url, json=edit_input)
    print('Status code: ', response.status_code)
    print('Reponse JSON:', response.json())
    print("\n")

# TEST 3: Edit Image (Resize)
if uploaded_path:
    print("\nResizing image...")

    edit_url = "http://127.0.0.1:5001/edit"

    edit_input = {
        'operation': 'resize',
        'filepath': uploaded_path,
        'size': (200, 200)
    }

    response = requests.post(edit_url, json=edit_input)
    print('Status code: ', response.status_code)   
    print('Reponse JSON:', response.json())
    print("\n")

# TEST 4: Edit Image (Crop)
if uploaded_path:
    print("\nCropping image...")

    edit_url = "http://127.0.0.1:5001/edit"

    edit_input = {
        'operation': 'crop',
        'filepath': uploaded_path,
        'box': (50, 50, 150, 150)
    }

    response = requests.post(edit_url, json=edit_input)
    print('Status code: ', response.status_code)
    print('Reponse JSON:', response.json())
    print("\n")

# TEST 5: Convert Image Format
if uploaded_path:
    print("\nConverting image format...")

    convert_url = edit_url = "http://127.0.0.1:5001/convert"

    convert_input = {
        'filepath': uploaded_path,
        'format': 'PNG'                                             # Convert to PNG
    }

    response = requests.post(convert_url, json=convert_input)
    print('Status code: ', response.status_code)
    print('Reponse JSON:', response.json())
    print("\n")


print("\nAll tests completed.")