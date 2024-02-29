import os
import psutil

def check_chrome_processes():
    chrome_processes = []
    for proc in psutil.process_iter(['pid', 'name']):
        if "chrome" in proc.info['name'].lower():
            chrome_processes.append(proc.info)
    return chrome_processes

def check_chrome_extensions():
    # Path to Chrome's user data directory
    chrome_user_data_path = "C:/Users/affen/AppData/Local/Google/Chrome/User Data"
    # Check for installed extensions
    extensions_path = f"{chrome_user_data_path}/Default/Extensions"
    installed_extensions = [ext for ext in os.listdir(extensions_path) if os.path.isdir(os.path.join(extensions_path, ext))]
    return installed_extensions

if __name__ == "__main__":
    chrome_processes = check_chrome_processes()
    if chrome_processes:
        print("Chrome processes found:")
        for proc in chrome_processes:
            print(f"PID: {proc['pid']}, Name: {proc['name']}")
    else:
        print("No Chrome processes found.")

    installed_extensions = check_chrome_extensions()
    if installed_extensions:
        print("Installed Chrome extensions found:")
        for ext in installed_extensions:
            print(ext)
    else:
        print("No installed Chrome extensions found.")
