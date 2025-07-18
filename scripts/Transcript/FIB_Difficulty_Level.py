import time
import unittest
import datetime
import xlwt
import json
import requests
from pathlib import Path
from constants import api
from common.read_excel import *


class FibDifficultyLevel:
    def __init__(self):
        self.overall_Statua = []
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
        # Define the relative path to the input data
        self.inputFilePath = "D:\\Automation\\API_Automation\\Input\\FIB_Candidate_Performance_DL.xls"
        self.outputFilePath = "D:\\Automation\\API_Automation\\Output\\FIB_Candidate_Performance_DL.html"
        # self.inputFilePath = "D:\Automation\API_Automation\Input\FIB_Candidate_Performance_DL.xls"
        # self.outputFilePath = "D:\Automation\API_Automation\Output\FIB_Candidate_Performance_DL.html"
        self.outputSheetName = "FIB_DL_Transcript"
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

    def fib_difficulty_level(self):
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
                    <h1>FIB Deep Dive - Candidate Performance By Difficulty Level</h1>
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
            myList = []
            self.input_Data1 = dict()
            for k in login_details:
                myList.append(login_details[k])

            self.testId = int(login_details.get('Test Id'))
            self.testUserId = int(login_details.get('Test User Id'))
            self.totalQuestions = int(login_details.get('Total Questions'))

            self.lowDifficulty = login_details.get('L Difficulty')
            self.lowCorrect = int(login_details.get('L Correct'))
            self.lowIncorrect = int(login_details.get('L Incorrect'))
            self.lowSkipped = int(login_details.get('L Skipped'))

            self.mediumDifficulty = login_details.get('M Difficulty')
            self.mediumCorrect = int(login_details.get('M Correct'))
            self.mediumIncorrect = int(login_details.get('M Incorrect'))
            self.mediumSkipped = int(login_details.get('M Skipped'))

            self.highDifficulty = login_details.get('H Difficulty')
            self.highCorrect = int(login_details.get('H Correct'))
            self.highIncorrect = int(login_details.get('H Incorrect'))
            self.highSkipped = int(login_details.get('H Skipped'))

            self.input_Data = {self.lowDifficulty: [self.lowCorrect, self.lowIncorrect, self.lowSkipped],
                               self.mediumDifficulty: [self.mediumCorrect, self.mediumIncorrect, self.mediumSkipped],
                               self.highDifficulty: [self.highCorrect, self.highIncorrect, self.highSkipped]}

            print("Expected : ", self.input_Data)

            self.file.write("""<tr>
                            <td></td>
                            <td></td>
                            <td>""" + str(self.testId) + """</td>
                            <td>""" + str(self.testUserId) + """</td>
                            <td>""" + str(self.totalQuestions) + """</td>
                            <td>""" + str(self.lowDifficulty) + """</td>
                            <td>""" + str(self.lowCorrect) + """</td>
                            <td>""" + str(self.lowIncorrect) + """</td>
                            <td>""" + str(self.lowSkipped) + """</td>
                            <td>""" + str(self.mediumDifficulty) + """</td>
                            <td>""" + str(self.mediumCorrect) + """</td>
                            <td>""" + str(self.mediumIncorrect) + """</td>
                            <td>""" + str(self.mediumSkipped) + """</td>
                            <td>""" + str(self.highDifficulty) + """</td>
                            <td>""" + str(self.highCorrect) + """</td>
                            <td>""" + str(self.highIncorrect) + """</td>
                            <td>""" + str(self.highSkipped) + """</td>""")

            self.loginToTest()
            self.reportData()
        self.file.write(
            """</tbody></table></div></div></body><div class="div-overalldata"><span class="label">Execution Date:&nbsp;&nbsp;</span><span class="lable value">""" + str(
                self.__current_DateTime) + """</span></br></br>""")
        if ("Fail" in self.overall_Statua):
            self.file.write(
                """<span class="label">Overall Status:&nbsp;&nbsp;</span><span class="lable valueFail">FAIL</span>""")
        else:
            self.file.write(
                """<span class="label">Overall Status:&nbsp;&nbsp;</span><span class="lable valuePass">PASS</span>""")
        self.file.write("""</div>""")

    def loginToTest(self):
        crpo_login_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName}
        login_data = {"LoginName": self.loginId, "Password": self.password, "TenantAlias": self.tenantAlias, "UserName": self.userName}
        login_request = requests.post(api.login_user, headers=crpo_login_header, data=json.dumps(login_data),
                                      verify=True)
        self.TokenVal = login_request.json()
        self.NTokenVal = self.TokenVal.get("Token")

    def reportData(self):
        transcript_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName,
                             "X-AUTH-TOKEN": self.NTokenVal}
        transcript_data = {"testId": self.testId, "testUserId": self.testUserId,
                           "reportFlags": {"eduWorkProfilesRequired": True, "testUsersScoreRequired": True,
                                           "fileContentRequired": False, "isProctroingDetailsRequired": True},
                           "print": False}
        transcript_request = requests.post("https://amsin.hirepro.in/py/assessment/report/api/v1/candidatetranscript/",
                                           headers=transcript_header, data=json.dumps(transcript_data), verify=True)
        transcript_response = transcript_request.json()
        testId = transcript_response['data']['assessment']['testId']
        testUser_Id = transcript_response['data']['assessment']['id']
        FIB_question_Count = len(transcript_response['data']['fillInTheBlank'])
        Total_question_Count = FIB_question_Count
        groupAndSectionWiseMarks = transcript_response['data']['groupAndSectionWiseMarks']

        fib_CIS = dict()
        fib_Low_Incorrect = 0
        fib_Low_Correct = 0
        fib_Low_Skipped = 0
        fib_High_Incorrect = 0
        fib_High_Correct = 0
        fib_High_Skipped = 0
        fib_Medium_Incorret = 0
        fib_Medium_Correct = 0
        fib_Medium_Skipped = 0
        for i in range(len(groupAndSectionWiseMarks)):
            for j in range(len(groupAndSectionWiseMarks[i]['sectionInfo'])):
                if groupAndSectionWiseMarks[i]['sectionInfo'][j]['questionType'] == "FillInTheBlank" or \
                        groupAndSectionWiseMarks[i]['sectionInfo'][j]['questionType'] == "ReferenceToContext":
                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['low'][
                        'inCorrect'] is not None:
                        fib_Low_Incorrect = fib_Low_Incorrect + \
                                            groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['low'][
                                                'inCorrect']
                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['low'][
                        'correct'] is not None:
                        fib_Low_Correct = fib_Low_Correct + \
                                          groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['low'][
                                              'correct']
                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['low'][
                        'skipped'] is not None:
                        fib_Low_Skipped = fib_Low_Skipped + \
                                          groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['low'][
                                              'skipped']

                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['medium'][
                        'inCorrect'] is not None:
                        fib_Medium_Incorret = fib_Medium_Incorret + \
                                              groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount'][
                                                  'medium']['inCorrect']
                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['medium'][
                        'correct'] is not None:
                        fib_Medium_Correct = fib_Medium_Correct + \
                                             groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount'][
                                                 'medium']['correct']
                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['medium'][
                        'skipped'] is not None:
                        fib_Medium_Skipped = fib_Medium_Skipped + \
                                             groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount'][
                                                 'medium']['skipped']

                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['high'][
                        'inCorrect'] is not None:
                        fib_High_Incorrect = fib_High_Incorrect + \
                                             groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount'][
                                                 'high']['inCorrect']
                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['high'][
                        'correct'] is not None:
                        fib_High_Correct = fib_High_Correct + \
                                           groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['high'][
                                               'correct']
                    if groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['high'][
                        'skipped'] is not None:
                        fib_High_Skipped = fib_High_Skipped + \
                                           groupAndSectionWiseMarks[i]['sectionInfo'][j]['difficultWiseCount']['high'][
                                               'skipped']

            fib_CIS['Low'] = [fib_Low_Correct, fib_Low_Incorrect, fib_Low_Skipped]
            fib_CIS['Medium'] = [fib_Medium_Correct, fib_Medium_Incorret, fib_Medium_Skipped]
            fib_CIS['High'] = [fib_High_Correct, fib_High_Incorrect, fib_High_Skipped]

        print("Actual : ", fib_CIS)

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

        if self.totalQuestions == Total_question_Count:
            self.file.write("""<td class="td-pass">""" + str(Total_question_Count) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(Total_question_Count) + """</td>""")
            self.status.append("Fail")

        for i in self.input_Data:
            if i in fib_CIS:
                self.file.write("""<td class="td-pass">""" + str(i) + """</td>""")
                self.status.append("Pass")
                for j in range(len(fib_CIS[i])):
                    if self.input_Data[i][j] == fib_CIS[i][j]:
                        self.file.write("""<td class="td-pass">""" + str(fib_CIS[i][j]) + """</td>""")
                        self.status.append("Pass")
                    else:
                        self.file.write("""<td class="td-fail">""" + str(fib_CIS[i][j]) + """</td>""")
                        self.status.append("Fail")
            else:
                self.file.write("""<td class="td-pass">""" + str(i) + """</td>""")
                self.status.append("Pass")

        if "Fail" in self.status:
            self.file.write("""<td class="zui-sticky-col-fail"><b>Fail</b></td>""")
            self.overall_Statua.append("Fail")
        else:
            self.file.write("""<td class="zui-sticky-col-pass"><b>Pass</b></td>""")
            self.overall_Statua.append("Pass")
        self.file.write("""</tr>""")

if __name__ == "__main__":
    trans = FibDifficultyLevel()
    trans.fib_difficulty_level()
    trans.loginToTest()
    trans.reportData()
