from user import create_user, get_user
def main():
    while True:
        action = input("Would you like to 'get' a user or 'create' a user? (type 'exit' to quit): ").strip().lower()
        if action == 'exit':
            break
        elif action == 'get':
            user_data, status_code = get_user(int(input("Enter user ID: "))) # reduced unneccesory lines of code
            print(f"Response: {user_data} (Status Code: {status_code})")
        elif action == 'create':
            user_data, status_code = create_user(input("Enter user name: "), int(input("Enter user age: "))) # reduced unneccesory lines of code
            print(f"Response: {user_data} (Status Code: {status_code})")
        else:
            print("Invalid action. Please type 'get' or 'create'.")
if __name__ == '__main__':
    main()