import math
import unittest
import re
import datetime
import xlwt
import json
import requests
from pathlib import Path
from constants import api
from common.read_excel import *


class SubjectivePerformance:
    def __init__(self):
        self.overall_Status = []
        now = datetime.datetime.now()
        self.__current_DateTime = now.strftime("%d/%m/%Y")
        self.appName = "crpo"
        self.isLambda = "true"
        self.tenantAlias = "automation"
        self.userName = "admin"
        self.loginId = "admin"
        self.password = "4LWS-0671"
        # Get the current script directory
        # script_dir = Path(__file__).resolve().parent
        # input_dir = script_dir.parent.parent.parent / 'Input'
        # output_dir = script_dir.parent.parent.parent / 'Output'
        # # Define the relative path to the input data
        # self.inputFilePath = input_dir / 'Subjective_Performance.xls'
        # self.outputFilePath = output_dir / 'Subjective_Performance.html'
        self.inputFilePath = r"D:\Automation\API_Automation\Input\Subjective_Performance.xls"
        self.outputFilePath = r"D:\Automation\API_Automation\Output\Subjective_Performance.html"
        self.outputSheetName = "Subjective_Performance"
        # --------------------------------------------------------------------------------------------------------------
        # CSS to differentiate Correct and Wrong data in Excel
        # --------------------------------------------------------------------------------------------------------------
        self.__style0 = xlwt.easyxf(
            'font: name Times New Roman, color-index black, bold on; pattern: pattern solid, fore-colour gold; border: left thin,right thin,top thin,bottom thin')
        self.__style1 = xlwt.easyxf(
            'font: name Times New Roman, color-index black, bold off; border: left thin,right thin,top thin,bottom thin')
        self.__style2 = xlwt.easyxf(
            'font: name Times New Roman, color-index red, bold on; border: left thin,right thin,top thin,bottom thin')
        self.__style3 = xlwt.easyxf(
            'font: name Times New Roman, color-index green, bold on; border: left thin,right thin,top thin,bottom thin')
        self.__style4 = xlwt.easyxf(
            'font: name Times New Roman, color-index black, bold off; pattern: pattern solid, fore-colour light_yellow; border: left thin,right thin,top thin,bottom thin')
        self.__style5 = xlwt.easyxf(
            'font: name Times New Roman, color-index black, bold off; pattern: pattern solid, fore-colour yellow; border: left thin,right thin,top thin,bottom thin')

    def subjective_performance(self):
        # mycursor.execute('delete from test_result_infos where testresult_id in (select id from test_results where testuser_id in (select id from test_users where test_id = '+i+' and login_time is not null));')
        # --------------------------------------------------------------------------------------------------------------
        # Read from Excel
        # --------------------------------------------------------------------------------------------------------------
        excel_reader = ExcelRead()
        excel_reader.excel_read(self.inputFilePath, 0)
        self.xls_values = excel_reader.details
        # excel_read_obj.excel_read(self.inputFilePath, 0)
        # self.xls_values = excel_read_obj.details
        wb_result = xlwt.Workbook()
        self.ws = wb_result.add_sheet(self.outputSheetName, cell_overwrite_ok=True)
        col_index = 0
        self.file = open(self.outputFilePath, "wt")
        self.file.write("""<html>
                <head>
                <title>Automation Results</title>
                <style>
                h1 {
                    color: #0e8eab;
                    text-align: left;
                    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                }
                .div-h1 {
                    position: absolute;
                    overflow: hidden;
                    top: 0;
                    width: auto;
                    height: 100px;
                    text-align: center;
                }
                .div-overalldata {
                    position: absolute;
                    top: 60px;
                    width: 600px;
                    height: auto;
                    text-align: left;
                    font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                }
                .label {
                    color: #0e8eab;
                    font-family: Arial;
                    font-size: 14pt;
                    font-weight: bold;
                }
                .value {
                    color: black;
                    font-family: Arial;
                    font-size: 14pt;
                }
                .valuePass {
                    color: green;
                    font-family: Arial;
                    animation: blinkingTextPass 0.8s infinite;
                    font-weight: bold;
                    font-size: 20pt;
                }       
                @keyframes blinkingTextPass{
                    0%{     color: green; font-size: 0pt;  }
                    50%{    color: lightgreen; }
                    100%{   color: green; font-size: 14pt; } 
                }
                .valueFail {
                    color: red;
                    font-family: Arial;
                    animation: blinkingTextFail 0.8s infinite;
                    font-weight: bold;
                    font-size: 20px;
                }
                @keyframes blinkingTextFail{
                    0%{     color: red; font-size: 0pt;   }
                    50%{    color: orange; }
                    100%{   color: red; font-size: 14pt;  }
                }
                .zui-table {
                    border: none;
                    border-right: solid 1px #DDEFEF;
                    border-collapse: separate;
                    border-spacing: 0;
                    font: normal 13px Arial, sans-serif;
                    width: 100%
                }
                .zui-table thead th {
                    border-left: solid 1px white;
                    border-bottom: solid 1px #DDEFEF;
                    background-color: #0e8eab;
                    color: white;
                    padding: 10px;
                    text-align: left;
                    white-space: nowrap;
                }
                .zui-table tbody td {
                    border-left: solid 1px #DDEFEF;
                    border-right: solid 1px #DDEFEF;
                    border-bottom: solid 1px #DDEFEF;
                    padding: 10px;
                    white-space: nowrap;
                }
                .td-pass {
                    color: green;
                    font-weight: bold;
                }
                .td-fail {
                    color: red;
                    font-weight: bold;
                }
                @media all{
                    table tr th:nth-child(1),
                    table tr td:nth-child(1),
                    table tr th:nth-child(2),
                    table tr td:nth-child(2){
                        display: none;
                    }
                }
                tr:nth-child(odd){background-color: #f2f2f2;}

                tr:hover {background-color: #ddd; border-collapse: collapse;}
                .zui-wrapper {
                    position: relative;
                    top: 100px;
                    width: 100%;
                    height: 100%;
                }
                .zui-scroller {
                    margin-left: 141px;
                    overflow-x: scroll;
                    overflow-y: visible;
                    padding-bottom: 5px;
                }
                .zui-table .zui-sticky-col {
                    border-left: solid 1px #DDEFEF;
                    border-right: solid 1px #DDEFEF;
                    left: 0;
                    position: absolute;
                    top: auto;
                    width: 120px;
                }
                .zui-table .zui-sticky-col-pass {
                    border-left: solid 1px #DDEFEF;
                    border-right: solid 1px #DDEFEF;
                    left: 0;
                    position: absolute;
                    top: auto;
                    width: 120px;
                    color:green;
                    font-weight: bold;
                }
                .zui-table .zui-sticky-col-fail {
                    border-left: solid 1px #DDEFEF;
                    border-right: solid 1px #DDEFEF;
                    left: 0;
                    position: absolute;
                    top: auto;
                    width: 120px;
                    color:red;
                    font-weight: bold;
                }
                </style>
                <div class="div-h2">
                    <h1>Subjective Deep Dive - Subjective Performance</h1>
                </div>
                </head>
                <body style="overflow: hidden;">
                <div class="zui-wrapper">
                <div class="zui-scroller"><table class="zui-table"><thead><tr>""")
        for xls_headers in excel_reader.headers_available_in_excel:
            self.ws.write(0, col_index, xls_headers, self.__style0)
            self.file.write(("""<th>""" + str(xls_headers) + """</th>"""))
            col_index += 1
        self.file.write("""<th class="zui-sticky-col">Status</th>""")
        self.file.write("""</tr></thead><tbody>""")
        self.login()
        self.rownum = 1

        for login_details in self.xls_values:
            self.expected_Data = []
            for v in login_details:
                if v != "Overall_Status":
                    if v != "Status":
                        self.expected_Data.append(login_details.get(v))
            self.expected_question_data = dict()

            j = 2
            totalQue = int((len(self.expected_Data)) / 7)
            print(totalQue)
            for i in range(0, int((len(self.expected_Data)) / 7)):
                self.expected_question_data[self.expected_Data[j]] = [self.expected_Data[j + 1], self.expected_Data[j + 2], self.expected_Data[j + 3], self.expected_Data[j + 4], self.expected_Data[j + 5], self.expected_Data[j + 6]]
                j += 7
            print("expected_question_data", self.expected_question_data)

            self.file.write("""<tr><td></td><td></td>""")
            for vv in self.expected_Data:
                self.file.write("""<td> """ + str(vv) + """ </td>""")
            self.testId = int(login_details.get('Test Id'))
            self.testUserId = int(login_details.get('Test User Id'))
            self.reportData()
            self.logout()

        self.file.write(
            """</tbody></table></div></div></body><div class="div-overalldata"><span class="label">Execution Date:&nbsp;&nbsp;</span><span class="lable value">""" + str(
                self.__current_DateTime) + """</span></br></br>""")
        if ("Fail" in self.overall_Status):
            self.file.write(
                """<span class="label">Overall Status:&nbsp;&nbsp;</span><span class="lable valueFail">FAIL</span>""")
        else:
            self.file.write(
                """<span class="label">Overall Status:&nbsp;&nbsp;</span><span class="lable valuePass">PASS</span>""")
        self.file.write("""</div>""")

    def login(self):
        crpo_login_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName}
        login_data = {"LoginName": self.loginId, "Password": self.password, "TenantAlias": self.tenantAlias, "UserName": self.userName}
        login_request = requests.post(api.login_user, headers=crpo_login_header, data=json.dumps(login_data),
                                      verify=True)
        response = login_request.json()
        self.NTokenVal = response.get("Token")

    def reportData(self):
        transcript_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName ,"X-AUTH-TOKEN": self.NTokenVal}
        transcript_data = {"testId": self.testId, "testUserId": self.testUserId,
                           "reportFlags": {"eduWorkProfilesRequired": True, "testUsersScoreRequired": True,
                                           "fileContentRequired": False, "isProctroingDetailsRequired": True},
                           "print": False}
        transcript_request = requests.post("https://amsin.hirepro.in/py/assessment/report/api/v1/candidatetranscript/",
                                           headers=transcript_header, data=json.dumps(transcript_data), verify=True)
        transcript_response = transcript_request.json()
        actual_testId = transcript_response['data']['assessment']['testId']
        actual_testUser_Id = transcript_response['data']['assessment']['id']
        qaQuestions = transcript_response['data']['qa']

        actual_question_data = dict()
        q_data =  []
        for d in qaQuestions:
            candidate_Ans = d.get('candidateAnswer')
            totalMarks = int(d.get('mark'))
            timeSpent = int(d.get('timeSpent'))
            obtainedMarks = d.get('obtainedMark')
            if d.get('candidateAnswer') is None:
                q_data.append("Skipped")
                q_data.append(timeSpent)
                candidate_Ans = "NA"
                wordCount = "Empty"
                q_data.append(wordCount)
                if obtainedMarks is None:
                    q_data.append("Not Scored")
                elif obtainedMarks == 0:
                    score = ("0/" + str(totalMarks))
                    q_data.append(score)
                else:
                    fractional, whole = math.modf(obtainedMarks)
                    if fractional > 0:
                        score = (str(obtainedMarks) + '/' + str(totalMarks))
                        q_data.append(score)
                    else:
                        obtainedMarks = int(obtainedMarks)
                        score = (str(obtainedMarks) + '/' + str(totalMarks))
                        q_data.append(score)
                q_data.append(d.get('questionString'))
                q_data.append(candidate_Ans)
            else:
                q_data.append("Answered")
                q_data.append(timeSpent)
                wordCount = len(re.findall(r'\w+', candidate_Ans))
                q_data.append(wordCount)
                if d.get('obtainedMark') is None:
                    q_data.append("Not Scored")
                elif obtainedMarks == 0:
                    score = ("0/" + str(totalMarks))
                    q_data.append(score)
                else:
                    fractionall, whole = math.modf(obtainedMarks)
                    if fractionall > 0:
                        score = (str(obtainedMarks) + '/' + str(totalMarks))
                        q_data.append(score)
                    else:
                        obtainedMarks = int(obtainedMarks)
                        score = (str(obtainedMarks) + '/' + str(totalMarks))
                        q_data.append(score)
                q_data.append(d.get('questionString'))
                q_data.append(candidate_Ans)
            actual_question_data[d.get('id')] = q_data
            q_data = []
        print("actual_question_data", actual_question_data)

        actual_Data = []
        actual_Data.append(actual_testId)
        actual_Data.append(actual_testUser_Id)
        for val_comp in self.expected_question_data:
            if val_comp in actual_question_data:
                actual_Data.append(val_comp)
                for sub_val in actual_question_data.get(val_comp):
                    actual_Data.append(sub_val)
        print("Expected Data - ", len(self.expected_Data))
        print("Actual Data   - ", len(actual_Data))
        self.status = []
        self.file.write("""<tr><td></td><td></td>""")
        for iter in range(0, len(self.expected_Data)):
            if self.expected_Data[iter] == actual_Data[iter]:
                self.file.write("""<td class="td-pass">""" + str(actual_Data[iter]) + """</td>""")
                self.status.append("Pass")
            else:
                self.file.write("""<td class="td-fail">""" + str(actual_Data[iter]) + """</td>""")
                self.status.append("Fail")

        if "Fail" in self.status:
            self.file.write("""<td class="zui-sticky-col-fail"><b>Fail</b></td>""")
            self.overall_Status.append("Fail")
        else:
            self.file.write("""<td class="zui-sticky-col-pass"><b>Pass</b></td>""")
            self.overall_Status.append("Pass")
        self.file.write("""</tr>""")
    def logout(self):
        crpo_logout_header = {"content-type": "application/json"}
        logout_data = {}
        logout_request = requests.post(api.login_user, headers=crpo_logout_header, data=json.dumps(logout_data), verify=True)
        logout_response = logout_request.json()


if __name__ == "__main__":
    sp = SubjectivePerformance()
    sp.subjective_performance()
    sp.login()
    sp.reportData()
    sp.logout()