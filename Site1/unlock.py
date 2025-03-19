from ppadb.client import Client as AdbClient

def is_rooted(device):
    try:
        output = device.shell("which su")
        return "not found" not in output
    except:
        return False

def remove_lock_screen():
    # Initialize ADB client
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    
    if not devices:
        print("No Android devices connected via ADB.")
        return
    
    device = devices[0]  # Use the first connected device
    
    # First, try to disable lock screen using locksettings command
    try:
        output = device.shell("locksettings set-disabled true")
        if "success" in output.lower():
            print("Lock screen disabled successfully using locksettings command.")
            return
        else:
            print("Failed to disable lock screen using locksettings command.")
    except Exception as e:
        print(f"Error executing locksettings command: {e}")
    
    # If locksettings fails, try settings put command
    try:
        output = device.shell("settings put secure lockscreen_disabled 1")
        if "success" in output.lower():
            print("Lock screen disabled successfully using settings put command.")
            return
        else:
            print("Failed to disable lock screen using settings put command.")
    except Exception as e:
        print(f"Error executing settings put command: {e}")
    
    # Check if device is rooted for advanced method
    if is_rooted(device):
        try:
            # Move locksettings.db and reboot
            device.shell('su -c "mv /data/system/locksettings.db /data/system/locksettings.db.backup"')
            device.shell("reboot")
            print("Lock screen should be disabled after reboot.")
        except Exception as e:
            print(f"Error moving locksettings.db: {e}")
    else:
        print("Device is not rooted. Cannot perform advanced operations.")

if __name__ == "__main__":
    remove_lock_screen()