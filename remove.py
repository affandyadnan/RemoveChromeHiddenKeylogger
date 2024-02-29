import os
import shutil

def remove_chrome_extension(extension_id):
    # Path to Chrome's user data directory
    chrome_user_data_path = "C:/Users/affen/AppData/Local/Google/Chrome/User Data"
    
    # Path to the directory containing the extension
    extension_path = os.path.join(chrome_user_data_path, "Default", "Extensions", extension_id)
    
    # Check if the extension directory exists
    if os.path.exists(extension_path):
        # Remove the extension directory
        shutil.rmtree(extension_path)
        print(f"Extension with ID {extension_id} removed successfully.")
    else:
        print(f"Extension with ID {extension_id} not found.")

if __name__ == "__main__":
    # Replace <YourUsername> with your actual Windows username
    extension_id = input("Enter the extension ID you want to remove: ")
    remove_chrome_extension(extension_id)
