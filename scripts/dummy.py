import datetime
import xlwt
import json
import requests
from hpro_automation.identity import credentials
from Utilities import excelRead
from hpro_automation.Config import outputFile
from hpro_automation.Config import inputFile
from hpro_automation import login
# from common.read_excel import *


class CodingPerformance(login.CommonLogin):

    def __init__(self):
        super().__init__()
        self.overall_Status = []
        now = datetime.datetime.now()
        self.__current_DateTime = now.strftime("%d/%m/%Y")
        self.appName = "crpo"
        self.isLambda = "true"
        self.inputFilePath = inputFile.assessment['Coding_Performance_Transcript']
        self.outputFilePath = outputFile.OUTPUT_PATH['Coding_Performance_Transcript']
        self.outputSheetName = "Coding_Performance"
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

    def coding_performance(self, server):
        # --------------------------------------------------------------------------------------------------------------
        # Read from Excel
        # --------------------------------------------------------------------------------------------------------------
        excel_reader = excelRead.ExcelRead()
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
                    <h1>Transcript - Coding Performance Report</h1>
                </div>
                </head>
                <body style="overflow: hidden;">
                <div class="zui-wrapper">
                <div class="zui-scroller"><table class="zui-table"><thead><tr>""")
        for xls_headers in excel_reader.headers_available_in_excel:
            self.ws.write(0, col_index, xls_headers, self.__style0)
            self.file.write(("""<th>""" + str(xls_headers) + """</th>"""))
            col_index += 1
        self.file.write("""<th class="zui-sticky-col">Status</th></tr></thead><tbody>""")
        self.rownum = 1


        for login_details in self.xls_values:

            self.testId = int(login_details.get('Test Id'))
            self.testUserId = int(login_details.get('Test User Id'))
            self.Ranking = login_details.get('Ranking')
            self.Ranking_OutOf = login_details.get('Ranking_OutOf')
            # self.percentile = login_details.get('Percentile')
            self.Marks = login_details.get('Marks')
            self.Marks_OutOf = login_details.get('Marks_OutOf')
            self.percentage = login_details.get('Percentage')
            self.Avg_Score = login_details.get('Avg_Score')
            self.Highest_Score = login_details.get('Highest_Score')
            self.Q1_Total_Marks = login_details.get('Q1_Total_Marks')
            self.Q1_Marks = login_details.get('Q1_Marks')
            self.Q2_Total_Marks = login_details.get('Q2_Total_Marks')
            self.Q2_Marks = login_details.get('Q2_Marks')
            self.Q3_Total_Marks = login_details.get('Q3_Total_Marks')
            self.Q3_Marks = login_details.get('Q3_Marks')
            self.Q4_Total_Marks = login_details.get('Q4_Total_Marks')
            self.Q4_Marks = login_details.get('Q4_Marks')
            self.Total_Marks = [self.Q1_Total_Marks, self.Q2_Total_Marks, self.Q3_Total_Marks, self.Q4_Total_Marks]
            self.Obt_Marks = [self.Q1_Marks, self.Q2_Marks, self.Q3_Marks, self.Q4_Marks]

            self.file.write("""<tr>
                            <td></td>
                            <td></td>
                            <td>""" + str(self.testId) + """</td>
                            <td>""" + str(self.testUserId) + """</td>
                            <td>""" + str(self.Ranking) + """</td>
                            <td>""" + str(self.Ranking_OutOf) + """</td>
                            <td>""" + str(self.Marks) + """</td>
                            <td>""" + str(self.Marks_OutOf) + """</td>
                            <td>""" + str(self.percentage) + """</td>
                            <td>""" + str(self.Avg_Score) + """</td>
                            <td>""" + str(self.Highest_Score) + """</td>
                            <td>""" + str(self.Q1_Total_Marks) + """</td>
                            <td>""" + str(self.Q1_Marks) + """</td>
                            <td>""" + str(self.Q2_Total_Marks) + """</td>
                            <td>""" + str(self.Q2_Marks) + """</td>
                            <td>""" + str(self.Q3_Total_Marks) + """</td>
                            <td>""" + str(self.Q3_Marks) + """</td>
                            <td>""" + str(self.Q4_Total_Marks) + """</td>
                            <td>""" + str(self.Q4_Marks) + """</td>""")

            self.loginToTest(server)
            self.cp_reportData(server)
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


    def loginToTest(self, server):
        self.lambda_function('Loginto_CRPO', server)
        crpo_login_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName}
        login_data = credentials.login_details['crpo']
        login_request = requests.post(self.webapi, headers=crpo_login_header, data=json.dumps(login_data), verify=True)
        self.TokenVal = login_request.json()
        self.NTokenVal = self.TokenVal.get("Token")


    def cp_reportData(self, server):
        self.lambda_function('candidate_transcript', server)
        transcript_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName, "X-AUTH-TOKEN": self.NTokenVal}
        transcript_data = {"testId":self.testId,"testUserId":self.testUserId,"reportFlags":{"eduWorkProfilesRequired":True,"testUsersScoreRequired":True,"fileContentRequired":False,"isProctroingDetailsRequired":True},"print":False}
        transcript_request = requests.post(self.webapi, headers=transcript_header, data=json.dumps(transcript_data), verify=True)
        transcript_response = transcript_request.json()
        # print(transcript_response)
        testId = transcript_response['data']['assessment']['testId']
        testUser_Id = transcript_response['data']['assessment']['id']

        CandidateRank = transcript_response['data']['questionTypeWiseOverall']['coding']['rank']
        RankOutOf = transcript_response['data']['assessment']['testUsersWithScore']
        marksObtained = transcript_response['data']['questionTypeWiseOverall']['coding']['marks']
        marksOutOf = transcript_response['data']['questionTypeWiseOverall']['coding']['totalMarks']
        percentage = transcript_response['data']['questionTypeWiseOverall']['coding']['percentage']
        averageScore = transcript_response['data']['questionTypeWiseOverall']['coding']['averageMarks']
        highestScore = transcript_response['data']['questionTypeWiseOverall']['coding']['highestMarks']

        question_Total = []
        question_obtained = []
        for i in transcript_response['data']['coding']:
            question_Total.append(i["mark"])
            if i["obtainedMark"] is None:
                question_obtained.append(0)
            else:
                question_obtained.append(i["obtainedMark"])
        print(question_Total)
        print(question_obtained)

        self.status = []
        self.file.write("""<tr><td></td><td></td>""")

        if int(self.testId) == int(testId):
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

        if self.Ranking == CandidateRank:
            self.file.write("""<td class="td-pass">""" + str(CandidateRank) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(CandidateRank) + """</td>""")
            self.status.append("Fail")

        if self.Ranking_OutOf == RankOutOf:
            self.file.write("""<td class="td-pass">""" + str(RankOutOf) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(RankOutOf) + """</td>""")
            self.status.append("Fail")

        if self.Marks == marksObtained:
            self.file.write("""<td class="td-pass">""" + str(marksObtained) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(marksObtained) + """</td>""")
            self.status.append("Fail")

        if self.Marks_OutOf == marksOutOf:
            self.file.write("""<td class="td-pass">""" + str(marksOutOf) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(marksOutOf) + """</td>""")
            self.status.append("Fail")

        if round(self.percentage, 2) == round(percentage, 2):
            self.file.write("""<td class="td-pass">""" + str(percentage) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(percentage) + """</td>""")
            self.status.append("Fail")

        if round(self.Avg_Score, 2) == round(averageScore, 2):
            self.file.write("""<td class="td-pass">""" + str(averageScore) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(averageScore) + """</td>""")
            self.status.append("Fail")

        if self.Highest_Score == highestScore:
            self.file.write("""<td class="td-pass">""" + str(highestScore) + """</td>""")
            self.status.append("Pass")
        else:
            self.file.write("""<td class="td-fail">""" + str(highestScore) + """</td>""")
            self.status.append("Fail")


        for i in range(0, len(question_Total)):
            if self.Total_Marks[i] == question_Total[i]:
                self.file.write("""<td class="td-pass">""" + str(question_Total[i]) + """</td>""")
                self.status.append("Pass")
            else:
                self.file.write("""<td class="td-fail">""" + str(question_Total[i]) + """</td>""")
                self.status.append("Fail")

            if self.Obt_Marks[i] == question_obtained[i]:
                self.file.write("""<td class="td-pass">""" + str(question_obtained[i]) + """</td>""")
                self.status.append("Pass")
            else:
                self.file.write("""<td class="td-fail">""" + str(question_obtained[i]) + """</td>""")
                self.status.append("Fail")

        if "Fail" in self.status:
            self.file.write("""<td class="zui-sticky-col-fail"><b>Fail</b></td>""")
            self.overall_Status.append("Fail")
        else:
            self.file.write("""<td class="zui-sticky-col-pass"><b>Pass</b></td>""")
            self.overall_Status.append("Pass")

        self.file.write("""</tr>""")

    def file_close(self):
        self.file.close()


# if __name__ == "__main__":
#     trans = CodingPerformance()
#     trans.coding_performance()
#     trans.loginToTest()
#     trans.cp_reportData()
#     trans.file_close()