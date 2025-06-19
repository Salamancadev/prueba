from db import load_data

def list_users():
    users = load_data()
    if not users:
        print("No hay usuarios registrados.")
    else:
        for user in users:
            print(f"ID: {user['id']}, Nombre: {user['name']}, Email: {user['email']}")