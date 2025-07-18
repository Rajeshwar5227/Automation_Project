import pytest
from scripts.Evaluation.Coding_Evaluation import CodingQpEvaluation
from scripts.Evaluation.Coding_Evaluation_1 import CodingQpEvaluation
from scripts.Evaluation.Static_Randon_QP import StaticRandomQpEvaluation
from scripts.Evaluation.Static_QP import StaticQpEvaluation
from scripts.DML_Scripts.dataCleanup import DB_Cleanup

@pytest.mark.evaluation_all
@pytest.mark.evaluation_coding
@pytest.mark.evaluation_noncoding
def test_Db_Cleanup():
    dbc = DB_Cleanup()
    dbc.db_connection()

@pytest.mark.evaluation_all
@pytest.mark.evaluation_coding
def test_Coding_Evaluation():
    cqpe = CodingQpEvaluation()
    cqpe.crpo_login()
    cqpe.fetch_input_expected()
    cqpe.attend_evaluate()
    cqpe.evaluate()
    cqpe.fetch_actual()
    cqpe.compare_write()

@pytest.mark.evaluation_all
@pytest.mark.evaluation_coding
def test_coding_Evaluation_1():
    cqpe1 = CodingQpEvaluation()
    cqpe1.crpo_login()
    cqpe1.fetch_input_expected()
    cqpe1.attend_evaluate()
    cqpe1.evaluate()
    cqpe1.fetch_actual()
    cqpe1.compare_write()

@pytest.mark.evaluation_all
@pytest.mark.evaluation_noncoding
def test_Static_Random_QP_Evaluation():
    srqpe = StaticRandomQpEvaluation()
    srqpe.static_random_qp_evaluation()

@pytest.mark.all_evaluation
@pytest.mark.evaluation_noncoding
def test_Static_QP_Evaluation():
    sqpe = StaticQpEvaluation()
    sqpe.static_qp_evaluation()