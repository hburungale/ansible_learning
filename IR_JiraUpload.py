import requests
import os
import shutil

def upload_attachment():
    access_token = os.environ.get('Access_Token')
    ticket_id = os.environ.get('Jira_Ticket_Id')
    url = f"https://jira.mdsol.com/rest/api/2/issue/{ticket_id}/attachments"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, "../reports/IR.pdf")#check
    # file_path = os.path.join(script_directory, "../reports/Distro_PIR.pdf")
    file_path = os.path.join(script_directory, f"../reports/{pdffilename}")

    headers = {
    'X-Atlassian-Token': 'nocheck',
    'Authorization': f'Bearer {access_token}'
    }
    files = {"file": open(file_path, "rb")}
    response = requests.post(url, headers=headers, files=files)
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    pdfname=os.environ.get('CTMS_URL')
    pdffilename = f"{pdfname}_PIR.pdf" 
    destination_folder = "../reports/"
    destination_path = os.path.join(destination_folder, pdffilename)
    shutil.copy(pdffilename, destination_path)
    upload_attachment()