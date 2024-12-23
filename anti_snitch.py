import os
import shutil

# Define the specific unlock code
SECRET_CODE = "1993"

# Paths to wipe (modify these paths as needed)
PATHS_TO_DELETE = [
    "/sdcard/Documents",
    "/sdcard/Downloads",
    "/sdcard/DCIM",
]

def delete_files(paths):
    for path in paths:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
                print(f"Deleted file: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Deleted directory: {path}")
        else:
            print(f"Path not found: {path}")

def main():
    print("Enter your unlock code:")
    code = input().strip()
    
    if code == SECRET_CODE:
        print("Incorrect code! Wiping files...")
        delete_files(PATHS_TO_DELETE)
    else:
        print("Access granted.")

if __name__ == "__main__":
    main()
