import datetime
import xlwt
import json
import requests
from hpro_automation.identity import credentials
from Utilities import excelRead
from hpro_automation.Config import outputFile
from hpro_automation.Config import inputFile
from hpro_automation import login


class McaSectionWiseQandAByCount(login.CommonLogin):
    def __init__(self):
        super().__init__()
        self.overall_Status = []
        now = datetime.datetime.now()
        self.__current_DateTime = now.strftime("%d/%m/%Y")
        self.appName = "crpo"
        self.isLambda = "true"
        self.inputFilePath = inputFile.assessment['MCA_SectionWise_QA_byCount']
        self.outputFilePath = outputFile.OUTPUT_PATH['MCA_SectionWise_QA_byCount']
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


    def mca_section_wise_q_and_a_by_count(self, server):
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
                    <h1>MCA Deep Dive - Candidate Performance SectionWise_QandA_byQuestionCount</h1>
                </div>
                </head>
                <body style="overflow: hidden; ">
                <div class="zui-wrapper">
                <div class="zui-scroller"><table class="zui-table"><thead><tr>""")
        for xls_headers in excel_reader.headers_available_in_excel:
            self.file.write(("""<th>""" + str(xls_headers) + """</th>"""))
            col_index += 1
        self.file.write("""<th class="zui-sticky-col">Status</th>""")
        self.file.write("""</tr></thead><tbody>""")
        self.login(server)
        self.rownum = 1

        for login_details in self.xls_values:
            self.expected_Data = []
            for v in login_details:
                if v != "Overall_Status":
                    if v != "Status":
                        self.expected_Data.append(login_details.get(v))
            self.grpVsSec = dict()
            j = 2
            totalGrps = int((len(self.expected_Data)) / 27)
            for i in range(0, int((len(self.expected_Data)) / 27)):
                self.grpVsSec[self.expected_Data[j]] = [self.expected_Data[j + 1], self.expected_Data[j + 10]]
                j += 27
            self.file.write("""<tr><td></td><td></td>""")
            for vv in self.expected_Data:
                self.file.write("""<td> """ + str(vv) + """ </td>""")
            self.testId = int(login_details.get('Test Id'))
            self.testUserId = int(login_details.get('Test User Id'))
            self.reportData(server)
            self.logout(server)

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

    def login(self, server):
        self.lambda_function('Loginto_CRPO', server)
        crpo_login_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName}
        login_data = credentials.login_details['crpo']
        login_request = requests.post(self.webapi, headers=crpo_login_header, data=json.dumps(login_data), verify=True)
        response = login_request.json()
        self.NTokenVal = response.get("Token")

    def reportData(self, server):
        self.lambda_function('candidate_transcript', server)
        transcript_header = {"content-type": "application/json", "X-APPLMA": self.isLambda, "APP-NAME": self.appName, "X-AUTH-TOKEN": self.NTokenVal}
        transcript_data = {"testId": self.testId, "testUserId": self.testUserId,
                           "reportFlags": {"eduWorkProfilesRequired": True, "testUsersScoreRequired": True,
                                           "fileContentRequired": False, "isProctroingDetailsRequired": True},
                           "print": False}
        transcript_request = requests.post(self.webapi, headers=transcript_header, data=json.dumps(transcript_data), verify=True)
        transcript_response = transcript_request.json()
        actual_testId = transcript_response['data']['assessment']['testId']
        actual_testUser_Id = transcript_response['data']['assessment']['id']
        groupAndSectionWiseMarks = transcript_response['data']['groupAndSectionWiseMarks']
        print(groupAndSectionWiseMarks)

        actual_Data = []
        actual_Data.append(actual_testId)
        actual_Data.append(actual_testUser_Id)
        for elem in self.grpVsSec:
            for elemm in groupAndSectionWiseMarks:
                groupQuestionCount = elemm.get('questionCount')
                if elem == elemm['name']:
                    actual_Data.append(elemm['name'])
                    grp_difficultWiseCount = elemm.get('difficultWiseCount')
                    for elemmm in self.grpVsSec[elem]:
                        for elemmmm in elemm['sectionInfo']:
                            if elemmm == elemmmm['sectionName']:
                                sec_difficultWiseCount = elemmmm.get('difficultWiseCount')
                                actual_Data.append(elemmmm['sectionName'])

                                if elemmmm['questionCount']['correct'] is None:
                                    sec_correct = 0
                                else:
                                    sec_correct = elemmmm['questionCount']['correct']
                                actual_Data.append(sec_correct)
                                if elemmmm['questionCount']['total'] is None:
                                    sec_total = 0
                                else:
                                    sec_total = elemmmm['questionCount']['total']
                                actual_Data.append(sec_total)

                                if sec_difficultWiseCount['low']['correct'] is None:
                                    sec_low_correct = 0
                                else:
                                    sec_low_correct = sec_difficultWiseCount['low']['correct']
                                actual_Data.append(sec_low_correct)
                                if sec_difficultWiseCount['low']['total'] is None:
                                    sec_low_total = 0
                                else:
                                    sec_low_total = sec_difficultWiseCount['low']['total']
                                actual_Data.append(sec_low_total)


                                if sec_difficultWiseCount['medium']['correct'] is None:
                                    sec_medium_correct = 0
                                else:
                                    sec_medium_correct = sec_difficultWiseCount['medium']['correct']
                                actual_Data.append(sec_medium_correct)
                                if sec_difficultWiseCount['medium']['total'] is None:
                                    sec_medium_total = 0
                                else:
                                    sec_medium_total = sec_difficultWiseCount['medium']['total']
                                actual_Data.append(sec_medium_total)

                                if sec_difficultWiseCount['high']['correct'] is None:
                                    sec_high_correct = 0
                                else:
                                    sec_high_correct = sec_difficultWiseCount['high']['correct']
                                actual_Data.append(sec_high_correct)
                                if sec_difficultWiseCount['high']['total'] is None:
                                    sec_high_total = 0
                                else:
                                    sec_high_total = sec_difficultWiseCount['high']['total']
                                actual_Data.append(sec_high_total)

                    if groupQuestionCount['correct'] is None:
                        grp_correct = 0
                    else:
                        grp_correct = groupQuestionCount['correct']
                    actual_Data.append(grp_correct)
                    if groupQuestionCount['total'] is None:
                        grp_total = 0
                    else:
                        grp_total = groupQuestionCount['total']
                    actual_Data.append(grp_total)


                    if grp_difficultWiseCount['low']['correct'] is None:
                        grp_low_correct = 0
                    else:
                        grp_low_correct = grp_difficultWiseCount['low']['correct']

                    actual_Data.append(grp_low_correct)
                    if grp_difficultWiseCount['low']['total'] is None:
                        grp_low_total = 0
                    else:
                        grp_low_total = grp_difficultWiseCount['low']['total']
                    actual_Data.append(grp_low_total)

                    if grp_difficultWiseCount['medium']['correct'] is None:
                        grp_medium_correct = 0
                    else:
                        grp_medium_correct = grp_difficultWiseCount['medium']['correct']

                    actual_Data.append(grp_medium_correct)
                    if grp_difficultWiseCount['medium']['total'] is None:
                        grp_medium_total = 0
                    else:
                        grp_medium_total = grp_difficultWiseCount['medium']['total']
                    actual_Data.append(grp_medium_total)

                    if grp_difficultWiseCount['high']['correct'] is None:
                        grp_high_correct = 0
                    else:
                        grp_high_correct = grp_difficultWiseCount['high']['correct']

                    actual_Data.append(grp_high_correct)
                    if grp_difficultWiseCount['high']['total'] is None:
                        grp_high_total = 0
                    else:
                        grp_high_total = grp_difficultWiseCount['high']['total']
                    actual_Data.append(grp_high_total)

        print("Exp", self.expected_Data)
        print("Act", actual_Data)
        self.status = []
        self.file.write("""<tr><td></td><td></td>""")
        for item_act in range(0, len(self.expected_Data)):
            if actual_Data[item_act] == 0 and self.expected_Data[item_act] == 'Empty':
                my_data = "Empty"
            else:
                my_data = actual_Data[item_act]
            if self.expected_Data[item_act] == my_data:
                self.file.write("""<td class="td-pass">""" + str(my_data) + """</td>""")
                self.status.append("Pass")
            else:
                self.file.write("""<td class="td-fail">""" + str(my_data) + """</td>""")
                self.status.append("Fail")
        if "Fail" in self.status:
            self.file.write("""<td class="zui-sticky-col-fail"><b>Fail</b></td>""")
            self.overall_Status.append("Fail")
        else:
            self.file.write("""<td class="zui-sticky-col-pass"><b>Pass</b></td>""")
            self.overall_Status.append("Pass")
        self.file.write("""</tr>""")

    def logout(self, server):
        self.lambda_function('Logoutfrom_CRPO', server)
        crpo_logout_header = {"content-type": "application/json"}
        logout_data = {}
        logout_request = requests.post(self.webapi, headers=crpo_logout_header, data=json.dumps(logout_data),
                                       verify=True)
        logout_response = logout_request.json()

