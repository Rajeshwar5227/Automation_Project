import pytest
from scripts.DML_Scripts.dataCleanup import DB_Cleanup

@pytest.mark.cleanup
def test_Db_Cleanup():
    dbc = DB_Cleanup()
    dbc.db_connection()