import requests
import os
import shutil

def upload_attachment():
    access_token = ""
    ticket_id = "IH-515876"
    url = f"https://jira.mdsol.com/rest/api/2/issue/{ticket_id}/attachments"
    # script_directory = os.path.dirname(os.path.abspath(__file__))
    # file_path = os.path.join(script_directory, "../reports/IR.pdf")#check
    # # file_path = os.path.join(script_directory, "../reports/Distro_PIR.pdf")
    # file_path = os.path.join(script_directory, f"../reports/{pdffilename}")
    file_path ="/Users/hburungale/Desktop/Hrithik/IR_automation/ansible_learning/IR.pdf"


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