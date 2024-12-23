# My Phone is No Snitch

## Overview

**My Phone is No Snitch** is a script designed to enhance personal privacy by deleting all files from specific directories on your Android device when a secret unlock code is entered. It works alongside **Termux** and **Tasker** to integrate functionality with the Android lock screen.

> ⚠️ **WARNING**: This script is destructive by design. Ensure you understand its behaviour and use it responsibly. Accidental activation will result in loss of files.

---

## Features

- Deletes all files in specified directories upon incorrect code entry.
- Integrates with **Termux** for execution and customization.
- Automation using **Tasker** to trigger the script upon specific events, like unlock attempts.
- Lightweight and simple to configure.

---

## Requirements

1. **Termux**: Terminal emulator and Linux environment for Android.  
   [Download Termux](https://f-droid.org/packages/com.termux/)

2. **Tasker**: Automation tool for Android.  
   [Download Tasker](https://play.google.com/store/apps/details?id=net.dinglisch.android.taskerm)

3. **Python**: Installed within Termux.

---

## Installation

### 1. Install Termux and Python
   - Open Termux and run:
     ```bash
     pkg update && pkg upgrade
     pkg install python
     ```

### 2. Download the Script
   - Save the script file as `anti_snitch.py` in your Termux home directory.

### 3. Configure the Script
   - Open the script and edit the following variables to suit your needs:
     ```python
     SECRET_CODE = "1993"  # Replace with your custom code.
     PATHS_TO_DELETE = [
         "/sdcard/Documents",
         "/sdcard/Downloads",
         "/sdcard/DCIM",
     ]  # Add or modify directories to delete.
     ```

### 4. Test the Script
   - In Termux, run:
     ```bash
     python anti_snitch.py
     ```
   - Enter the unlock code to test behavior.

---

## Integration with Tasker

### 1. Create a Tasker Profile
   - Open Tasker and create a new profile:
     - Trigger: **Event** > **Display** > **Display Unlocked**.

### 2. Add a Task to Run the Script
   - In the new profile, add a task with the following steps:
     1. **Action**: **Run Shell**
        - Command: `python /data/data/com.termux/files/home/anti_snitch.py`
        - Enable **Use Root** (if root access is needed).

### 3. Test the Task
   - Lock and unlock your device to trigger the profile.

---

## Usage

1. Open your phone’s lock screen.
2. Enter the configured secret unlock code.
3. If the code is incorrect, the script deletes all files in the specified directories.

---

## License

This project is licensed under the MIT License.

---

## Disclaimer

The developer assumes no responsibility for any data loss or misuse of this script. Use it at your own risk.
