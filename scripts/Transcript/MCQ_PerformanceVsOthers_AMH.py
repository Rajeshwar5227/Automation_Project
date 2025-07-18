import time
import unittest
import datetime
import xlwt
import json
import requests
from pathlib import Path
from constants import api
from common.read_excel import *


class McqPerformanceVsOthersAmh:
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
        # self.inputFilePath = input_dir / 'MCQ_Candidate_Performance_AMH.xls'
        # self.outputFilePath = output_dir / 'MCQ_Candidate_Performance_AMH.html'
        self.inputFilePath = r"D:\Automation\API_Automation\Input\MCQ_Candidate_Performance_AMH.xls"
        self.outputFilePath = r"D:\Automation\API_Automation\Output\MCQ_Candidate_Performance_AMH.html"
        self.outputSheetName = "PerformanceVsOther_AMH"
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

    def mcq_performance_vs_others_amh(self):
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
                    <h1>MCQ Deep Dive - Candidate Performance vs others</h1>
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
        self.rownum = 1


        for login_details in self.xls_values:

            self.testId = int(login_details.get('Test Id'))
            self.testUserId = int(login_details.get('Test User Id'))
            self.G1 = login_details.get('G1')
            self.G1_LS = login_details.get('G1_LS')
            self.G1_AS = login_details.get('G1_AS')
            self.G1_CS = login_details.get('G1_CS')
            self.G1_HS = login_details.get('G1_HS')
            self.G2 = login_details.get('G2')
            self.G2_LS = login_details.get('G2_LS')
            self.G2_AS = login_details.get('G2_AS')
            self.G2_CS = login_details.get('G2_CS')
            self.G2_HS = login_details.get('G2_HS')
            self.G3 = login_details.get('G3')
            self.G3_LS = login_details.get('G3_LS')
            self.G3_AS = login_details.get('G3_AS')
            self.G3_CS = login_details.get('G3_CS')
            self.G3_HS = login_details.get('G3_HS')
            self.G4 = login_details.get('G4')
            self.G4_LS = login_details.get('G4_LS')
            self.G4_AS = login_details.get('G4_AS')
            self.G4_CS = login_details.get('G4_CS')
            self.G4_HS = login_details.get('G4_HS')

            self.all_Groups = [self.G1, self.G2, self.G3, self.G4]
            self.expected = {self.G1: [self.G1_LS, self.G1_AS, self.G1_CS, self.G1_HS],
                             self.G2: [self.G2_LS, self.G2_AS, self.G2_CS, self.G2_HS],
                             self.G3: [self.G3_LS, self.G3_AS, self.G3_CS, self.G3_HS],
                             self.G4: [self.G4_LS, self.G4_AS, self.G4_CS, self.G4_HS]}

            self.file.write("""<tr>
                            <td></td>
                            <td></td>
                            <td>""" + str(self.testId) + """</td>
                            <td>""" + str(self.testUserId) + """</td>
                            <td>""" + str(self.G1) + """</td>
                            <td>""" + str(self.G1_LS) + """</td>
                            <td>""" + str(self.G1_AS) + """</td>
                            <td>""" + str(self.G1_CS) + """</td>
                            <td>""" + str(self.G1_HS) + """</td>
                            <td>""" + str(self.G2) + """</td>
                            <td>""" + str(self.G2_LS) + """</td>
                            <td>""" + str(self.G2_AS) + """</td>
                            <td>""" + str(self.G2_CS) + """</td>
                            <td>""" + str(self.G2_HS) + """</td>
                            <td>""" + str(self.G3) + """</td>
                            <td>""" + str(self.G3_LS) + """</td>
                            <td>""" + str(self.G3_AS) + """</td>
                            <td>""" + str(self.G3_CS) + """</td>
                            <td>""" + str(self.G3_HS) + """</td>
                            <td>""" + str(self.G4) + """</td>
                            <td>""" + str(self.G4_LS) + """</td>
                            <td>""" + str(self.G4_AS) + """</td>
                            <td>""" + str(self.G4_CS) + """</td>
                            <td>""" + str(self.G4_HS) + """</td>""")

            self.loginToTest()
            self.reportData()
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

    def loginToTest(self):
        crpo_login_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName}
        login_data = {"LoginName": self.loginId, "Password": self.password, "TenantAlias": self.tenantAlias, "UserName": self.userName}
        login_request = requests.post(api.login_user, headers=crpo_login_header, data=json.dumps(login_data), verify=True)
        self.TokenVal = login_request.json()
        self.NTokenVal = self.TokenVal.get("Token")

    def reportData(self):
        transcript_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName, "X-AUTH-TOKEN": self.NTokenVal}
        # transcript_data = {"testId":self.testId,"testUserId":self.testUserId,"reportFlags":{"eduWorkProfilesRequired":True,"testUsersScoreRequired":True,"fileContentRequired":False,"isProctroingDetailsRequired":True},"print":False}
        transcript_data = {"testId":self.testId,"testUserId":self.testUserId,"reportFlags":{"eduWorkProfilesRequired":True,"testUsersScoreRequired":True,"fileContentRequired":False,"isProctroingDetailsRequired":True},"print":False}
        transcript_request = requests.post("https://amsin.hirepro.in/py/assessment/report/api/v1/candidatetranscript/", headers=transcript_header, data=json.dumps(transcript_data), verify=True)
        transcript_response = transcript_request.json()
        # print(transcript_response)
        testId = transcript_response['data']['assessment']['testId']
        testUser_Id = transcript_response['data']['assessment']['id']
        groupSectionScoreSummary = transcript_response['data']['groupSectionScoreSummary']
        groupAndSectionWiseMarks = transcript_response['data']['groupAndSectionWiseMarks']

        groups_vs_LS = dict()
        groups_vs_AS = dict()
        groups_vs_HS = dict()
        for i in groupSectionScoreSummary:
            if "groupId" in i:
                LS = i.get("minMarks")
                if LS is None:
                    LS = 0.0
                AS = i.get("avgMarks")
                if AS is None:
                    AS = 0.0
                HS = i.get("maxMarks")
                if HS is None:
                    HS = 0.0
                for k, v in i.items():
                    if k == "groupId":
                        groups_vs_LS[v] = round(LS, 2)
                        groups_vs_AS[v] = round(AS, 2)
                        groups_vs_HS[v] = round(HS, 2)
                        LS = 0.0
                        AS = 0.0
                        HS = 0.0
        print("groups_vs_LS : ", groups_vs_LS)
        print("groups_vs_AS : ", groups_vs_AS)
        print("groups_vs_HS : ", groups_vs_HS)

        # groups_vs_MAM = dict()
        # val_list = []
        # for i in groupSectionScoreSummary:
        #     if "groupId" in i:
        #         val_list.append(i.get("minMarks"))
        #         val_list.append(i.get("avgMarks"))
        #         val_list.append(i.get("maxMarks"))
        #         for k, v in i.items():
        #             if k == "groupId":
        #                 groups_vs_MAM[v] = val_list
        #                 val_list = []

        groups_vs_CS = dict()
        for i in groupAndSectionWiseMarks:
            if "id" in i:
                candidate_Marks = i.get("obtainedMarks")
                if candidate_Marks is None:
                    candidate_Marks = 0.0
                for k, v in i.items():
                    if k == "id":
                        groups_vs_CS[v] = round(candidate_Marks, 2)
                        candidate_Marks = 0.0
        print("groups_vs_CS : ", groups_vs_CS)

        self.status = []
        self.file.write("""<tr><td></td><td></td>""")

        if self.testId == testId:
            self.file.write("""<td class="td-pass">""" + str(testId) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(testId) + """</td>""")
            self.status.append("Fail")

        if self.testUserId == testUser_Id:
            self.file.write("""<td class="td-pass">""" + str(testUser_Id) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(testUser_Id) + """</td>""")
            self.status.append("Fail")

        actual = dict()
        for i in self.all_Groups:
            if i in groups_vs_LS.keys() and groups_vs_AS.keys() and groups_vs_CS.keys() and groups_vs_HS.keys():
                actual[i] = [groups_vs_LS.get(i), groups_vs_AS.get(i), groups_vs_CS.get(i), groups_vs_HS.get(i)]

        for ii in self.expected:
            if ii in actual:
                self.file.write("""<td class="td-pass">""" + str(ii) + """</td>""")
                self.status.append("Pass")
                expected_values = self.expected.get(ii)
                actual_values = actual.get(ii)
                for i in range(len(expected_values)):
                    if round(expected_values[i], 2) == round(actual_values[i], 2):
                        self.file.write("""<td class="td-pass">""" + str(round(actual_values[i], 2)) + """</td>""")
                        self.status.append("Pass")
                    else:
                        self.file.write("""<td class="td-fail">""" + str(round(actual_values[i], 2)) + """</td>""")
                        self.status.append("Fail")
            else:
                self.file.write("""<td class="td-fail">""" + "NA" + """</td>""")
                self.status.append("Fail")
                self.file.write("""<td class="td-fail">""" + "NA" + """</td>""")
                self.status.append("Fail")
                self.file.write("""<td class="td-fail">""" + "NA" + """</td>""")
                self.status.append("Fail")
                self.file.write("""<td class="td-fail">""" + "NA" + """</td>""")
                self.status.append("Fail")
                self.file.write("""<td class="td-fail">""" + "NA" + """</td>""")
                self.status.append("Fail")


        if "Fail" in self.status:
            self.file.write("""<td class="zui-sticky-col-fail"><b>Fail</b></td>""")
            self.overall_Status.append("Fail")
        else:
            self.file.write("""<td class="zui-sticky-col-pass"><b>Pass</b></td>""")
            self.overall_Status.append("Pass")
        self.file.write("""</tr>""")

if __name__ == "__main__":
    mcqpvoamh = McqPerformanceVsOthersAmh()
    mcqpvoamh.mcq_performance_vs_others_amh()
    mcqpvoamh.loginToTest()
    mcqpvoamh.reportData()