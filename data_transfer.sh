#!/bin/bash

# Function to disable USB data
disable_usb_data() {
    echo "Disabling USB data exchange..."
    # Command to disable USB data
    echo 0 > /sys/class/android_usb/android0/enable
    echo "USB data exchange blocked."
}

# Function to re-enable USB data (if needed)
enable_usb_data() {
    echo "Re-enabling USB data exchange..."
    echo 1 > /sys/class/android_usb/android0/enable
    echo "USB data exchange enabled."
}

# Monitor USB connections
monitor_usb() {
    echo "Monitoring USB connections..."
    while true; do
        # Check for active USB devices
        usb_status=$(lsusb)
        if [ -n "$usb_status" ]; then
            echo "USB device detected:"
            echo "$usb_status"
            disable_usb_data
        fi
        # Wait for a second before checking again
        sleep 1
    done
}

# Main script logic
if [ "$(id -u)" -ne 0 ]; then
    echo "This script requires root privileges. Please run as root."
    exit 1
fi

monitor_usb
