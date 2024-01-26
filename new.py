import os
import requests

def get_auth_credentials():
    username = os.environ.get('Key1')
    password = os.environ.get('Key2')
    return (username, password)

def construct_file_path():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_directory, "../reports/IR_automation.py")

def upload_attachment():
    url = "https://jira.mdsol.com/rest/api/2/issue/IH-518298/attachments"
    
    # Get authentication credentials
    auth = get_auth_credentials()

    # Construct the correct file path
    file_path = construct_file_path()

    # Prepare the headers
    headers = {"X-Atlassian-Token": "nocheck"}

    # Prepare the file payload
    files = {"file": open(file_path, "rb")}

    try:
        # Make the HTTP POST request
        response = requests.post(url, auth=auth, headers=headers, files=files)

        # Check if the request was successful
        if response.status_code == 200:
            print("Attachment uploaded successfully.")
        else:
            print(f"Failed to upload attachment. Status code: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    upload_attachment()
