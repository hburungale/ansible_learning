import requests
import os
import shutil
from FetchCyclopsData import get_json_data

def upload_attachment():
    json_data = get_json_data()
    Git_Branch = json_data["global"]["GIT_BRANCH"]
    print(Git_Branch)
    access_token = os.environ.get('Access_Token')
    ticket_id = os.environ.get('Jira_Ticket_Id')
    pdfname=os.environ.get('CTMS_URL')
    pirfilename = f"{pdfname}_PIR.pdf"
    irfilename = f"{pdfname}_PIR.pdf" 
    url = f"https://jira.mdsol.com/rest/api/2/issue/{ticket_id}/attachments"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, f"./reports/{irfilename}")
    file_path = os.path.join(script_directory, f"./reports/{pirfilename}")

    headers = {
    'X-Atlassian-Token': 'nocheck',
    'Authorization': f'Bearer {access_token}'
    }
    files = {"file": open(file_path, "rb")}
    response = requests.post(url, headers=headers, files=files)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    upload_attachment()