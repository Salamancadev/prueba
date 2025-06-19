from db import load_data, save_data

def update_user(user_id, new_name, new_email):
    users = load_data()
    for user in users:
        if user["id"] == user_id:
            user["name"] = new_name
            user["email"] = new_email
            save_data(users)
            print("✅ Usuario actualizado.")
            return
    print("❌ Usuario no encontrado.")