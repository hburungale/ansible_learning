import requests

def upload_attachment():
    url = "https://jira.mdsol.com/rest/api/2/issue/IH-454862/attachments"
    username = ""
    password = ""
    file_path = "/reports"
    
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