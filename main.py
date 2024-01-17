def create_fake_error():
    print("Welcome to the Fake Error Creator")


    error_type = input("Enter the type of error to simulate (e.g., ValueError, NameError): ")
    error_message = input("Enter the error message: ")

    print("\nSimulated Error:")
    print(f"\033[91m{error_type}: {error_message}\033[0m")

def stop():
    tostop = input("Type anything to stop the program: ")

if __name__ == "__main__":
    create_fake_error()
    stop()
