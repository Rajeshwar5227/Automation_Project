import pytest
from scripts.Randomization.Server_Question import ServerQuestionRandomization
from scripts.DML_Scripts.dataCleanup import DB_Cleanup

@pytest.mark.randomization
def test_Db_Cleanup():
    dbc = DB_Cleanup()
    dbc.db_connection()

@pytest.mark.randomization
def test_Server_Question_Randomization():
    sqr = ServerQuestionRandomization()
    sqr.server_question_randomization()

