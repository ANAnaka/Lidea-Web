import firebase_admin
from firebase_admin import credentials, db

# Путь к JSON-файлу
cred = credentials.Certificate("C:/Users/annak/VS/Lidea/lidea/lidea/credentials/lidea-db.json")


# URL вашей Realtime Database
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://lidea-db-4508f-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
