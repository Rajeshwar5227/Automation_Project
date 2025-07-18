import pandas as pd
import requests
import json
import math
from openpyxl import load_workbook
from openpyxl.styles import Font

class ATS_Legato:
    INPUT_PATH = "D:/Automation/API_Automation/Input/legato.xls"
    CLIENT_ID = "90970363-f584-45ac-b427-889206625be4"
    CLIENT_SECRET = "5WyWHPBDlJx01HZmpjIGxYok7ff4rOUx"
    TOKEN_URL = "https://amsin.hirepro.in/py/oauth2/fdc7590d5d0c494796365ae1963f10d2/access_token/"

    def __init__(self):
        self.token = None
        self.input_data = []
        self.actual_data = []

    def get_token(self):
        header = {"content-type": "application/json"}
        data = {
            "client_id": self.CLIENT_ID,
            "client_secret": self.CLIENT_SECRET
        }
        request = requests.post(self.TOKEN_URL, headers=header, data=json.dumps(data), verify=True)
        response = request.json()
        self.token = response.get("access_token")
        print("\n\n")
        print(f"Legato Token: {self.token}")

    def get_data(self):
        df = pd.read_excel(self.INPUT_PATH, engine="xlrd")
        df = df.where(pd.notnull(df), None)
        self.input_data = df.to_dict('records')
        print(f"Input data - {self.input_data}")

    def registerAndTagCandidateToTest(self):
        for item in self.input_data:
            header = {"content-type": "application/json", "Authorization": "bearer " + self.token}
            # if math.isnan(item["Test Id"]):
            #     test_id = 0  # or any default value
            # else:
            #     test_id = int(item["Test Id"])
            data = {
                "testId": "test_id",
                "firstName": f"{item["First Name"]}",
                "middleName": f"{item["Middle Name"]}",
                "lastName": f"{item["Last Name"]}",
                "remoteCandidateId": item["Remote Candidate Id"],
                "primaryEmail": f"{item["Primary Email"]}",
                "workDayRequisitionId": f"{item["Workday Requisition Id"]}",
                "workDayJobApplicationId": f"{item["Workday Job Application Id"]}",
                "workDayAssessmentTestId": f"{item["Workday Assessment Test Id"]}",
                "workDayAssessmentStatusId": f"{item["Workday Assessment Status Id"]}"
            }
            request = requests.post("https://amsin.hirepro.in/py/ats/legato/registerAndTagCandidateToTest/",
                                    headers=header, data=json.dumps(data), verify=True)
            response = request.json()
            # print(f"Response - {response}")
            if 'error' in response and response['error']:
                response_msg = response['error'].get('errorDescription', 'No error description provided')
                item["Actual"] = response_msg
            elif 'data' in response and response['data']:
                response_msg = response['data'].get('message', 'No message provided')

                item["Actual"] = response_msg
            else:
                response_msg = 'No relevant information found'
                item["Actual"] = response_msg
            print(f"Response message - {response_msg}")


