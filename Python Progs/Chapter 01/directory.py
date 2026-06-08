import os

def list_directory_contents(directory_path):
    try:
        # List all files and directories in the given directory path
        contents = os.listdir(directory_path)
        print(f"Contents of the directory '{directory_path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied to access the directory '{directory_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Replace this path with the directory you want to list
    directory_path = '.'  # Current directory
    list_directory_contents(directory_path)
