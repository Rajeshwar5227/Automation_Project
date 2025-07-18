import datetime
import xlwt
import json
import requests
from constants import api
from common.read_excel import *


class McaTimeSpentPerQuestion:
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
        self.inputFilePath = r"D:\Automation\API_Automation\Input\FIB_Candidate_Performance_TSPQ.xls"
        self.outputFilePath = r"D:\Automation\API_Automation\Output\FIB_Candidate_Performance_TSPQ.html"
        # Get the current script directory
        # script_dir = Path(__file__).resolve().parent
        # input_dir = script_dir.parent.parent.parent / 'Input'
        # output_dir = script_dir.parent.parent.parent / 'Output'
        # # Define the relative path to the input data
        # self.inputFilePath = input_dir / 'FIB_Candidate_Performance_TSPQ.xls'
        # self.outputFilePath = output_dir / 'FIB_Candidate_Performance_TSPQ.html'
        # self.inputFilePath = "D:\Automation\API_Automation\Input\FIB_Candidate_Performance_TSPQ.xls"
        # self.outputFilePath = "D:\Automation\API_Automation\Output\FIB_Candidate_Performance_TSPQ.html"
        self.outputSheetName = ""
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

    def mca_time_spent_per_question(self):
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
        self.ws = wb_result.add_sheet("TimeSpentPerQuestion", cell_overwrite_ok=True)
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
                    <h1>FIB Deep Dive - Candidate Performance By Time Spent Per Question</h1>
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

            self.testId = int(login_details.get('Test Id'))
            self.testUserId = int(login_details.get('Test User Id'))
            self.totalQuestions = int(login_details.get('Total Questions'))
            self.Q1_Id = int(login_details.get('Q1_Id'))
            self.Q1_DL = str(login_details.get('Q1_DL'))
            self.Q1_TS = int(login_details.get('Q1_TS'))
            self.Q1_Status = str(login_details.get('Q1_Status'))
            self.Q2_Id = int(login_details.get('Q2_Id'))
            self.Q2_DL = str(login_details.get('Q2_DL'))
            self.Q2_TS = int(login_details.get('Q2_TS'))
            self.Q2_Status = str(login_details.get('Q2_Status'))
            self.Q3_Id = int(login_details.get('Q3_Id'))
            self.Q3_DL = str(login_details.get('Q3_DL'))
            self.Q3_TS = int(login_details.get('Q3_TS'))
            self.Q3_Status = str(login_details.get('Q3_Status'))
            self.Q4_Id = int(login_details.get('Q4_Id'))
            self.Q4_DL = str(login_details.get('Q4_DL'))
            self.Q4_TS = int(login_details.get('Q4_TS'))
            self.Q4_Status = str(login_details.get('Q4_Status'))
            self.Q5_Id = int(login_details.get('Q5_Id'))
            self.Q5_DL = str(login_details.get('Q5_DL'))
            self.Q5_TS = int(login_details.get('Q5_TS'))
            self.Q5_Status = str(login_details.get('Q5_Status'))
            self.Q6_Id = int(login_details.get('Q6_Id'))
            self.Q6_DL = str(login_details.get('Q6_DL'))
            self.Q6_TS = int(login_details.get('Q6_TS'))
            self.Q6_Status = str(login_details.get('Q6_Status'))
            self.Q7_Id = int(login_details.get('Q7_Id'))
            self.Q7_DL = str(login_details.get('Q7_DL'))
            self.Q7_TS = int(login_details.get('Q7_TS'))
            self.Q7_Status = str(login_details.get('Q7_Status'))
            self.Q8_Id = int(login_details.get('Q8_Id'))
            self.Q8_DL = str(login_details.get('Q8_DL'))
            self.Q8_TS = int(login_details.get('Q8_TS'))
            self.Q8_Status = str(login_details.get('Q8_Status'))
            self.Q9_Id = int(login_details.get('Q9_Id'))
            self.Q9_DL = str(login_details.get('Q9_DL'))
            self.Q9_TS = int(login_details.get('Q9_TS'))
            self.Q9_Status = str(login_details.get('Q9_Status'))
            self.Q10_Id = int(login_details.get('Q10_Id'))
            self.Q10_DL = str(login_details.get('Q10_DL'))
            self.Q10_TS = int(login_details.get('Q10_TS'))
            self.Q10_Status = str(login_details.get('Q10_Status'))
            self.Q11_Id = int(login_details.get('Q11_Id'))
            self.Q11_DL = str(login_details.get('Q11_DL'))
            self.Q11_TS = int(login_details.get('Q11_TS'))
            self.Q11_Status = str(login_details.get('Q11_Status'))
            self.Q12_Id = int(login_details.get('Q12_Id'))
            self.Q12_DL = str(login_details.get('Q12_DL'))
            self.Q12_TS = int(login_details.get('Q12_TS'))
            self.Q12_Status = str(login_details.get('Q12_Status'))


            self.expected_data_dict = {self.Q1_Id: [self.Q1_DL, self.Q1_TS, self.Q1_Status],
                                       self.Q2_Id: [self.Q2_DL, self.Q2_TS, self.Q2_Status],
                                       self.Q3_Id: [self.Q3_DL, self.Q3_TS, self.Q3_Status],
                                       self.Q4_Id: [self.Q4_DL, self.Q4_TS, self.Q4_Status],
                                       self.Q5_Id: [self.Q5_DL, self.Q5_TS, self.Q5_Status],
                                       self.Q6_Id: [self.Q6_DL, self.Q6_TS, self.Q6_Status],
                                       self.Q7_Id: [self.Q7_DL, self.Q7_TS, self.Q7_Status],
                                       self.Q8_Id: [self.Q8_DL, self.Q8_TS, self.Q8_Status],
                                       self.Q9_Id: [self.Q9_DL, self.Q9_TS, self.Q9_Status],
                                       self.Q10_Id: [self.Q10_DL, self.Q10_TS, self.Q10_Status],
                                       self.Q11_Id: [self.Q11_DL, self.Q11_TS, self.Q11_Status],
                                       self.Q12_Id: [self.Q12_DL, self.Q12_TS, self.Q12_Status]}
            self.file.write("""<tr>
                            <td></td>
                            <td></td>
                            <td>""" + str(self.testId) + """</td>
                            <td>""" + str(self.testUserId) + """</td>
                            <td>""" + str(self.totalQuestions) + """</td>
                            <td>""" + str(self.Q1_Id) + """</td><td>""" + str(self.Q1_DL) + """</td>
                            <td>""" + str(self.Q1_TS) + """</td><td>""" + str(self.Q1_Status) + """</td>
                            <td>""" + str(self.Q2_Id) + """</td><td>""" + str(self.Q2_DL) + """</td>
                            <td>""" + str(self.Q2_TS) + """</td><td>""" + str(self.Q2_Status) + """</td>
                            <td>""" + str(self.Q3_Id) + """</td><td>""" + str(self.Q3_DL) + """</td>
                            <td>""" + str(self.Q3_TS) + """</td><td>""" + str(self.Q3_Status) + """</td>
                            <td>""" + str(self.Q4_Id) + """</td><td>""" + str(self.Q4_DL) + """</td>
                            <td>""" + str(self.Q4_TS) + """</td><td>""" + str(self.Q4_Status) + """</td>
                            <td>""" + str(self.Q5_Id) + """</td><td>""" + str(self.Q5_DL) + """</td>
                            <td>""" + str(self.Q5_TS) + """</td><td>""" + str(self.Q5_Status) + """</td>
                            <td>""" + str(self.Q6_Id) + """</td><td>""" + str(self.Q6_DL) + """</td>
                            <td>""" + str(self.Q6_TS) + """</td><td>""" + str(self.Q6_Status) + """</td>
                            <td>""" + str(self.Q7_Id) + """</td><td>""" + str(self.Q7_DL) + """</td>
                            <td>""" + str(self.Q7_TS) + """</td><td>""" + str(self.Q7_Status) + """</td>
                            <td>""" + str(self.Q8_Id) + """</td><td>""" + str(self.Q8_DL) + """</td>
                            <td>""" + str(self.Q8_TS) + """</td><td>""" + str(self.Q8_Status) + """</td>
                            <td>""" + str(self.Q9_Id) + """</td><td>""" + str(self.Q9_DL) + """</td>
                            <td>""" + str(self.Q9_TS) + """</td><td>""" + str(self.Q9_Status) + """</td>
                            <td>""" + str(self.Q10_Id) + """</td><td>""" + str(self.Q10_DL) + """</td>
                            <td>""" + str(self.Q10_TS) + """</td><td>""" + str(self.Q10_Status) + """</td>
                            <td>""" + str(self.Q11_Id) + """</td><td>""" + str(self.Q11_DL) + """</td>
                            <td>""" + str(self.Q11_TS) + """</td><td>""" + str(self.Q11_Status) + """</td>
                            <td>""" + str(self.Q12_Id) + """</td><td>""" + str(self.Q12_DL) + """</td>
                            <td>""" + str(self.Q12_TS) + """</td><td>""" + str(self.Q12_Status) + """</td>""")


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
        transcript_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName, "X-AUTH-TOKEN": self.NTokenVal}
        transcript_data = {"testId": self.testId, "testUserId": self.testUserId,
                           "reportFlags": {"eduWorkProfilesRequired": True, "testUsersScoreRequired": True,
                                           "fileContentRequired": False, "isProctroingDetailsRequired": True},
                           "print": False}
        transcript_request = requests.post("https://amsin.hirepro.in/py/assessment/report/api/v1/candidatetranscript/",
                                           headers=transcript_header, data=json.dumps(transcript_data), verify=True)
        transcript_response = transcript_request.json()
        testId = transcript_response['data']['assessment']['testId']

        mca_rtc_questionIds = transcript_response['data']['testResultQuestionIds']

        testUser_Id = transcript_response['data']['assessment']['id']
        FIB_question_Count = len(transcript_response['data']['fillInTheBlank'])
        Total_question_Count = FIB_question_Count
        question_ids = []
        actual_data_dict = dict()
        for i in range(len(transcript_response['data']['fillInTheBlank'])):
            question_ids.append(transcript_response['data']['fillInTheBlank'][i]['id'])
            qid = transcript_response['data']['fillInTheBlank'][i]['id']
            candidateAnswer = transcript_response['data']['fillInTheBlank'][i]['candidateAnswer']
            obtainedMark = transcript_response['data']['fillInTheBlank'][i]['obtainedMark']
            timeSpent = transcript_response['data']['fillInTheBlank'][i]['timeSpent']
            difficultyLevel = transcript_response['data']['fillInTheBlank'][i]['difficultyLevel']
            if difficultyLevel is 1:
                difficultyLevel = 'Low'
            elif difficultyLevel is 4:
                difficultyLevel = 'Medium'
            elif difficultyLevel is 3:
                difficultyLevel = 'High'
            else:
                difficultyLevel = "Other"
            if (candidateAnswer is None and obtainedMark == 0 and timeSpent == 0) or (
                    candidateAnswer is None and obtainedMark == 0 and timeSpent > 0):
                status = "Not attempted"
            elif candidateAnswer is not None and obtainedMark == 0 and timeSpent > 0:
                status = "Wrong answer"
            elif candidateAnswer is not None and (obtainedMark > 0 or obtainedMark < 0) and timeSpent > 0:
                status = "Correct answer"
            else:
                status = "NA"
            actual_data_dict[qid] = [difficultyLevel, timeSpent, status]


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

        for k, v in self.expected_data_dict.items():
            if k in actual_data_dict.keys():
                self.file.write("""<td class="td-pass">""" + str(k) + """</td>""")
                self.status.append("Pass")
                values = actual_data_dict[k]
                for indxx in range(len(v)):
                    if v[indxx] == values[indxx]:
                        self.file.write("""<td class="td-pass">""" + str(values[indxx]) + """</td>""")
                        self.status.append("Pass")
                    else:
                        self.file.write("""<td class="td-fail">""" + str(values[indxx]) + """</td>""")
                        self.status.append("Fail")
            else:
                self.file.write("""<td class="td-fail">""" + "NA" + """</td>""")
                self.status.append("Fail")
                for indxx in range(len(v)):
                    self.file.write("""<td class="td-fail">""" + "NA" + """</td>""")
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
        logout_request = requests.post(api.login_user, headers=crpo_logout_header, data=json.dumps(logout_data),
                                      verify=True)
        logout_response = logout_request.json()

if __name__ == "__main__":
    mcatspq = McaTimeSpentPerQuestion()
    mcatspq.mca_time_spent_per_question()
    mcatspq.login()
    mcatspq.reportData()
    mcatspq.logout()
