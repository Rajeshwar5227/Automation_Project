import time

import mysql
from mysql import connector
from mysql.connector import errorcode


class DB_Cleanup():
    def __init__(self):
        # Client Question Randomization - 7590 - AT Tenant amsin server
        # Coding evaluation - 8581 - Automation Tenant amsin server
        # Server Question Randomization - 7528 - AT tenant amsin server
        # Static QP evaluation - 5282 - Automation Tenant amsin server
        # Random QP evaluation - 5365 - Automation Tenant amsin server
        # Timer verification - 7518 - AT tenant amsin server
        # [7590, 8581, 7528, 5282, 5365, 7518]
        # [5282, 7528, 5365, 7518, 8581, 7590]
        # test_ids = [5282, 7528, 5365, 7518, 8581, 7590]
        # test_ids = [5282, 7528, 5365, 7518, 8581, 7590, 22019]
        self.test_ids = [5282, 7528, 5365, 7518, 8581, 7590, 22019]
        self.host_ip = '35.154.36.218'  # Master DB
        # host_ip = '35.154.213.175'    #Replica DB
        self.db_name = "appserver_core"
        self.login_name = "qauser"
        self.pwd = "qauser"

    def db_connection(self):
        conn = mysql.connector.connect(host=self.host_ip, database=self.db_name, user=self.login_name,
                                       password=self.pwd)
        my_cursor = conn.cursor()
        try:
            for i in self.test_ids:
                i = str(i)
                my_cursor.execute(
                    'delete from test_result_infos where testresult_id in (select id from test_results where testuser_id in (select id from test_users where test_id = ' + i + ' and login_time is not null));')
                conn.commit()
                print("Test Result Info Deleted", i)
                my_cursor.execute(
                    'delete from test_results where testuser_id in (select id from test_users where test_id = ' + i + ' and login_time is not null);')
                conn.commit()
                print('Test result deleted ', i)
                my_cursor.execute(
                    'delete from candidate_scores where testuser_id in (select id from test_users where test_id = ' + i + ' and login_time is not null);')
                conn.commit()
                print('Candidate score deleted ', i)
                my_cursor.execute(
                    'delete from test_user_login_infos where testuser_id in (select id from test_users where test_id = ' + i + ' and login_time is not null);')
                conn.commit()
                print('Test user login info deleted ', i)
                my_cursor.execute(
                    "update test_users set login_time = NULL, log_out_time = NULL, status = 0, client_system_info = NULL, time_spent = NULL, is_password_disabled = 0,config = NULL, client_system_info = NULL, total_score = NULL, percentage = NULL, eval_on = NULL, eval_by = NULL, eval_status = 'NotEvaluated', eval_task_id = NULL where test_id = '" + i + "';")
                conn.commit()
                print('Test user login time reset ', i)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        my_cursor.close()
        print('Connection closed')
        print('Executed')

if __name__ == "__main__":
    dbc = DB_Cleanup()
    dbc.db_connection()