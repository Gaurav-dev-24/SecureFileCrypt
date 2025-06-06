# 🔐 SecureFileCrypt

SecureFileCrypt is a simple and secure file encryption/decryption web tool. Upload your file, encrypt it with a key, and keep your data safe.

## ✨ What It Does

- 🔒 Encrypts any file (PDF, TXT, DOCX, etc.) with a unique key
- 🔓 Decrypts previously encrypted files using the correct key
- 📂 Upload and download files securely from the browser
- 💡 Clean, minimal UI using Flask
- 🛡️ Keeps your data private — no cloud, no third-party access


---

## 📁 Project Structure

SecureFileCrypt/
├── main.py # Flask app – handles routes and runs the server
├── encryptor.py # Core encryption and decryption logic using Fernet
├── utils.py # Key generation and validation helpers
├── templates/
│ └── index.html # Frontend HTML template (upload UI)
├── uploads/ # Temporary file storage for encrypted/decrypted files
├── secret.key # Encryption key file (auto-generated)
├── requirements.txt # Python dependencies
├── .gitignore # Hides unnecessary files from Git
└── README.md # Project documentation


---

## 🧪 How to Run Locally

Follow these steps to run the project on your local machine:

### 1. Clone the repository

```bash
git clone https://github.com/Gaurav-dev-24/SecureFileCrypt.git
cd SecureFileCrypt


### 2. Create and activate virtual environment (for macOS/Linux)

```bash 
python3 -m venv venv
source venv/bin/activate


For Windows:
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies

```bash
pip install -r requirements.txt

### 5. Start the Flask server

```bash
python main.py


---

## 👤 Author

Made with ❤️ by **Gaurav Jangid**  
📫 Reach me on [GitHub](https://github.com/Gaurav-dev-24)
