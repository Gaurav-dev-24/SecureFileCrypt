from flask import Flask, render_template, request, send_file
from Encryptor import encrypt_file, decrypt_file
import os

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


with open("secret.key", "rb") as f:
    key = f.read()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt_route():
    file = request.files['file']
    if file.filename == '':
        return "No file selected!", 400

    filename = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    with open(file_path, 'rb') as f:
        original_data = f.read()

    encrypted_data = encrypt_file(original_data, key)
    encrypted_path = file_path + ".enc"

    with open(encrypted_path, 'wb') as f:
        f.write(encrypted_data)

    return send_file(encrypted_path, as_attachment=True)

@app.route('/decrypt', methods=['POST'])
def decrypt_route():
    file = request.files['file']
    if file.filename == '':
        return "No file selected!", 400

    filename = file.filename
    if not filename.endswith(".enc"):
        return "Please upload a .enc file only!", 400

    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = decrypt_file(encrypted_data, key)
    decrypted_path = file_path.replace(".enc", ".dec")

    with open(decrypted_path, 'wb') as f:
        f.write(decrypted_data)

    return send_file(decrypted_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
