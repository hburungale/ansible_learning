import requests
import os

def upload_attachment():
    url = "https://jira.mdsol.com/rest/api/2/issue/IH-518298/attachments"
    username = os.environ.get('Key1')
    password = os.environ.get('Key2')
    script_directory = os.path.dirname(os.path.abspath(__file__))
    secret_key = os.environ.get('Key1')
    print(secret_key)
    
    # Construct the correct file path
    file_path = os.path.join(script_directory, "../reports/IR_automation.py")
    
    # Prepare the authentication credentials
    auth = (username, password)

    # Prepare the headers
    headers = {"X-Atlassian-Token": "nocheck"}

    # Prepare the file payload
    files = {"file": open(file_path, "rb")}

    # Make the HTTP POST request
    response = requests.post(url, auth=auth, headers=headers, files=files)

    # Print the response
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    upload_attachment()