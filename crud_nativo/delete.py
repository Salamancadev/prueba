from db import load_data, save_data

def delete_user(user_id):
    users = load_data()
    updated_users = [user for user in users if user["id"] != user_id]
    if len(updated_users) == len(users):
        print("❌ Usuario no encontrado.")
    else:
        save_data(updated_users)
        print("✅ Usuario eliminado.")