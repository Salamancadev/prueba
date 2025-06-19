from create import create_user
from read import list_users
from update import update_user
from delete import delete_user

def main():
    while True:
        print("\n==== CRUD Nativo de Usuarios ====")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")

        option = input("Selecciona una opción: ").strip()

        if option == "1":
            name = input("Nombre: ")
            email = input("Email: ")
            create_user(name, email)

        elif option == "2":
            list_users()

        elif option == "3":
            try:
                user_id = int(input("ID del usuario a actualizar: "))
                name = input("Nuevo nombre: ")
                email = input("Nuevo email: ")
                update_user(user_id, name, email)
            except ValueError:
                print("❌ ID inválido.")

        elif option == "4":
            try:
                user_id = int(input("ID del usuario a eliminar: "))
                delete_user(user_id)
            except ValueError:
                print("❌ ID inválido.")

        elif option == "5":
            print("👋 Hasta pronto.")
            break

        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()