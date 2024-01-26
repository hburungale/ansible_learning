import requests
import os

def upload_attachment():
    url = "https://jira.mdsol.com/rest/api/2/issue/IH-454862/attachments"
    access_token = os.environ.get('Bearer')
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "../reports/IR_automation.py")
    headers = {
    'X-Atlassian-Token': 'nocheck',
    'Authorization': f'Bearer {access_token}'
    }

    # Prepare the file payload
    files = {"file": open(file_path, "rb")}

    # Make the HTTP POST request
    response = requests.post(url, headers=headers, files=files)

    # Print the response
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    upload_attachment()