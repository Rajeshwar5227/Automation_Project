#################################### Api Collection ####################################
api_collection = {
    'getApplicantInfo': {
        'api_url': 'https://' + 'acnrecruitment.staging.accenture.com' + '/py/crpo/applicant/api/v1/getApplicantsInfo/',
        'defaultPayload': {"CandidateIds": [111111], "isApplicantHistoryRequired": True,
                           "isAssessmentInfoRequired": False, "isCustomPropertiesRequired": True,
                           "isApplicantAttachmentRequired": True}
    },
    'getScreenData': {
        'api_url': 'https://' + 'acnrecruitment.staging.accenture.com' + '/py/crpo/candidate/api/v1/getScreenData/',
        'defaultPayload': {"candidateId": 111111}
    },
    'get_all_candidates': {
        'api_url': 'https://' + 'acnrecruitment.staging.accenture.com' + '/py/rpo/get_all_candidates/',
        'defaultPayload': {"CandidateFilters": {'ThirdPartyId': [11111]}}
    },
    'getAll': {
        'api_url': 'https://' + 'amsin.hirepro.in' + '/py/crpo/hackathon/admin/api/v1/getAll/',
        'defaultPayload': {"search": {"name": " "}}
    },
    'get': {
        'api_url': 'https://' + 'amsin.hirepro.in' + '/py/crpo/hackathon/admin/api/v1/get/',
        'defaultPayload': {"id": 11111}
    },
    'create':{
        'api_url': 'https://' + 'amsin.hirepro.in' + '/py/crpo/hackathon/admin/api/v1/create/',
        'defaultPayload': {  "name": "Testcase_Hackathon",
  "categoryId": 45394,
  "locationType": "1",
  "locations": [
    25177
  ],
  "tags": [
    20,
    19,
    21
  ],
  "skills": [
    2495,
    2391,
    48876
  ],
  "modeId": 45397,
  "description": "<div>testcase challenge details</div>",
  "personas": [
    45403,
    45402,
    45401
  ],
  "isJobConfidential": True,
  "isTeamBased": True,
  "teamSize": 10,
  "teamMinSize": 5,
  "alterTeamTimeFrom": "2025-01-02 00:00:00",
  "alterTeamTimeTo": "2025-01-08 00:00:00",
  "jobDetails": {
    "experienceInMonths": {
      "min": 12,
      "max": 24
    },
    "ctcInLakhs": {
      "min": 5,
      "max": 10
    },
    "noOfOpenings": 5,
    "companyId": 2708,
    "reqTypeId": 43962,
    "designationId": 1573,
    "jobTitle": "Developer/SE"
  },
  "eventDetails": {
    "address": "testcase address",
    "cityId": 25095,
    "provinceId": 25047,
    "startTime": "2025-01-02 00:00:00",
    "endTime": "2025-01-06 00:00:00"
  },
  "requirementDetails": {
    "id": 2083
  },
  "otherDetails": {
    "companyDetails": {
      "logo": "https://s3-ap-southeast-1.amazonaws.com/testhirepro-content/accenturetest/hackathonlogos/8cc17e5a-0e53-4c99-afc5-5477a8634040Profile-PNG.png",
      "about": "<div>testcase about company</div>",
      "website": "https://www.google.com/"
    },
    "miscDetails": {
      "rules": "<div>testcase rule</div>",
      "prizes": "<div>testcase prizes</div>",
      "rewards": "<div>Testcase rewards</div>",
      "faq": [
        {
          "question": "testcase question",
          "answer": "<div>testcase answer</div>"
        }
      ],
      "diversityInfo": "testcase additional info",
      "overview": "<div>testcase overview</div>",
      "whyParticipate": "<div>testcase why participate</div>",
      "leadersOrWinners": "<div>testcase leaders/winners</div>",
      "milestone": "<div>testcase milestone</div>",
      "bannerImages": [
        {

        }
      ]
    },
    "registrationConfig": {
      "defaultPageId": "433"
    }
  },
  "externalHackathonDetails": {

  }
}
    },
    'getAllEvent': {
        'api_url': 'https://' + 'amsin.hirepro.in' + '/py/crpo/event/api/v1/getAllEvent/',
        'defaultPayload': {"Paging": {"MaxResults": 20, "PageNumber": 1},
                            "isAllEventRequired": True,
                              "Search": {"Name": "Testcase2_Hackathon"}, "Status": 1}}}

login_user = "https://amsin.hirepro.in/py/common/user/login_user/"
GetAllRequirement = "https://amsin.hirepro.in/HirePro.AppServer.UnsecureHost/RestCampusManagementService.svc/GetAllRequirement"
GetAllJobRole = "https://amsin.hirepro.in/HirePro.AppServer.UnsecureHost/RestCampusManagementService.svc/GetAllJobRole"
PartialUpdateSubJob = "https://amsin.hirepro.in/amsweb/JSONServices/JSONCampusManagementService.svc/PartialUpdateSubJob"
PartialGetSubJobById = "https://amsin.hirepro.in/amsweb/JSONServices/JSONCampusManagementService.svc/PartialGetSubJobById"
GetAllEventByTypes = "https://amsin.hirepro.in/amsweb/JSONServices/JSONCampusManagementService.svc/GetAllEventByTypes"
GetAllRecruitEvent = "https://amsin.hirepro.in/HirePro.AppServer.UnsecureHost/RestCampusManagementService.svc/GetAllRecruitEvent"
tagCandidatesToEventJobRoleTests = "https://amsin.hirepro.in/py/crpo/applicant/api/v1/tagCandidatesToEventJobRoleTests/"
applicantStatusChange = "https://amsin.hirepro.in/py/crpo/applicant/api/v1/applicantStatusChange/"
createUser = "https://amsin.hirepro.in/py/common/user/create_user/"
updateUser = "https://amsin.hirepro.in/py/common/user/update_user/"
addSkillToUsers = "https://amsin.hirepro.in/py/crpo/interviewer_nomination/api/v1/add_user_skills/"
bulkUploadCandidates = "https://amsin.hirepro.in/amsweb/JSONServices/JSONCampusManagementService.svc/CreateBulkCandidates"
createJR = "https://amsin.hirepro.in/py/rpo/create_req/"
createRequirement = "https://amsin.hirepro.in/py/crpo/requirement/api/v1/createRequirement/"
createEvent = "https://amsin.hirepro.in/py/crpo/event/api/v1/createEvent/"
interviewFeedback = "https://amsin.hirepro.in/py/crpo/api/v1/interview/givefeedback/"
createCandidate = "https://amsin.hirepro.in/py/rpo/create_candidate/"
createQuestion = "https://amsin.hirepro.in/py/assessment/authoring/api/v1/createQuestion/"
test = "https://amsin.hirepro.in/py/common/filehandler/api/v2/upload/.png,.jpg,.jpeg,.gif,/1500/"



tagJRtoReq = "https://amsin.hirepro.in/amsweb/JSONServices/JSONCampusManagementService.svc/UpdatePartialCampusHiringConfig"




live_accenturetest_Login = "https://indiacampus.ciostage.accenture.com/py/common/user/login_user/"
live_accenturetest_CreateUser = "https://indiacampus.ciostage.accenture.com/py/common/user/create_user/"
live_accenturetest_AddSkills = "https://indiacampus.ciostage.accenture.com/py/crpo/interviewer_nomination/api/v1/add_user_skills/"


accenture_live_Login = "https://indiacampus.accenture.com/py/common/user/login_user/"
accenture_live_CreateUser = "https://indiacampus.accenture.com/py/common/user/create_user/"
accenture_live_AddSkills = "https://indiacampus.accenture.com/py/crpo/interviewer_nomination/api/v1/add_user_skills/"


Atos_Login = "https://ams.hirepro.in/py/common/user/login_user/"
Atos_CreateUser = "https://ams.hirepro.in/py/common/user/create_user/"


Wings_Login = "https://ams.hirepro.in/py/common/user/login_user/"
Wings_CreateUser = "https://ams.hirepro.in/py/common/user/create_user/"