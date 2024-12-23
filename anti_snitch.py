import os
import shutil
import sys
from datetime import datetime

# Define the specific unlock code
SECRET_CODE = "1993"

# Paths to wipe (modify these paths as needed)
PATHS_TO_DELETE = [
    "/sdcard/Documents",
    "/sdcard/Downloads",
    "/sdcard/DCIM",
]

# Log file for Tasker
LOG_FILE = "/sdcard/tasker_script.log"

def log_event(message):
    """Log events to a file for Tasker."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.now()}: {message}\n")

def delete_files(paths):
    """Delete specified files or directories."""
    for path in paths:
        if os.path.exists(path):
            if os.path.isfile(path):
                os.remove(path)
                log_event(f"Deleted file: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                log_event(f"Deleted directory: {path}")
        else:
            log_event(f"Path not found: {path}")

def main():
    """Main function to handle unlock logic."""
    # Check for input from Tasker
    if len(sys.argv) > 1:
        code = sys.argv[1].strip()
    else:
        log_event("No unlock code provided by Tasker.")
        sys.exit("Error: No unlock code provided.")

    # Validate the code
    if code == SECRET_CODE:
        log_event("Incorrect code entered. Wiping files...")
        delete_files(PATHS_TO_DELETE)
    else:
        log_event("Correct code entered. Access granted.")

if __name__ == "__main__":
    main()
