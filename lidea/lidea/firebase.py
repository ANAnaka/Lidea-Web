import firebase_admin
from firebase_admin import credentials, db
import os

# Путь к JSON-файлу (относительный путь)
cred_path = os.path.join(os.path.dirname(__file__), 'credentials', 'lidea-db.json')
cred = credentials.Certificate(cred_path)

# URL вашей Realtime Database
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://lidea-db-4508f-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
