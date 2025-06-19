from db import load_data, save_data

def create_user(name, email):
    users = load_data()
    user_id = users[-1]['id'] + 1 if users else 1
    new_user = {
        "id": user_id,
        "name": name,
        "email": email
    }
    users.append(new_user)
    save_data(users)
    print("✅ Usuario creado exitosamente.")