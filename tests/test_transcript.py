import pytest
from scripts.Transcript.Coding_Performance import CodingPerformance
from scripts.Transcript.Coding_Performance_TC_Summary import CodingPerformanceTcSummary
from scripts.Transcript.Coding_QA_Performance import CodingQAPerformance
from scripts.Transcript.FIB_Comprehensive import FibComprehensive
from scripts.Transcript.FIB_Difficulty_Level import FibDifficultyLevel
from scripts.Transcript.FIB_PerformanceVsOthers_AMH import FibPerformanceVsOthersAmh
from scripts.Transcript.FIB_SectionWise_QandA_byCount import FibSectionWiseQandAByCount
from scripts.Transcript.FIB_SectionWise_QandA_byScore import FibSectionWiseQandAByScore
from scripts.Transcript.FIB_TimeSpentPerQuestion import FibTimeSpentPerQuestion
from scripts.Transcript.MCA_Comprehensive import McaComprehensive
from scripts.Transcript.MCA_DifficultyLevel import McaDifficultyLevel
from scripts.Transcript.MCA_PerformanceVsOthers_AMH import McaPerformanceVsOthersAmh
from scripts.Transcript.MCA_SectionWise_QandA_byCount import McaSectionWiseQandAByCount
from scripts.Transcript.MCA_SectionWise_QandA_byScore import McaSectionWiseQandAByScore
from scripts.Transcript.MCA_TimeSpentPerQuestion import McaTimeSpentPerQuestion
from scripts.Transcript.MCQ_Comprehensive import McqComprehensive
from scripts.Transcript.MCQ_DifficultyLevel import McqDifficultyLevel
from scripts.Transcript.MCQ_Performance import McqPerformance
from scripts.Transcript.MCQ_PerformanceVsOthers_AMH import McqPerformanceVsOthersAmh
from scripts.Transcript.MCQ_SectionWise_QandA_byCount import McqSectionWiseQandAByCount
from scripts.Transcript.MCQ_SectionWise_QandA_byScore import McqSectionWiseQandAByScore
from scripts.Transcript.MCQ_TimeSpentPerQuestion import McqTimeSpentPerQuestion
from scripts.Transcript.MCQW_Comprehensive import McqwComprehensive
from scripts.Transcript.MCQW_DifficultyLevel import McqwDifficultyLevel
from scripts.Transcript.MCQW_PerformanceVsOthers_AMH import McqwPerformanceVsOthersAmh
from scripts.Transcript.MCQW_SectionWise_QandA_byCount import McqwSectionWiseQandAByCount
from scripts.Transcript.MCQW_SectionWise_QandA_byScore import McqwSectionWiseQandAByScore
from scripts.Transcript.MCQW_TimeSpentPerQuestion import McqwTimeSpentPerQuestion
from scripts.Transcript.Overall_Performance import OverallPerformance
from scripts.Transcript.Subjective_Performance import SubjectivePerformance


@pytest.mark.transcript
def test_Coding_Performance():
    cp_trans = CodingPerformance()
    cp_trans.coding_performance()
    cp_trans.loginToTest()
    cp_trans.cp_reportData()
    cp_trans.file_close()

@pytest.mark.transcript
@pytest.mark.change
def test_Coding_Performance_TC_Summary():
    cptcs_trans = CodingPerformanceTcSummary()
    cptcs_trans.coding_performance_tc_summary()
    cptcs_trans.login()
    cptcs_trans.report_data()

@pytest.mark.transcript
def test_Coding_QA_Performance():
    cqap = CodingQAPerformance()
    cqap.coding_qa_performance()
    cqap.login()
    cqap.reportData()
    cqap.logout()

@pytest.mark.transcript
def test_FIB_Comprehensive():
    fc = FibComprehensive()
    fc.fib_comprehensive()
    fc.login()
    fc.reportData()
    fc.logout()

@pytest.mark.transcript
def test_FIB_Difficulty_Level():
    fdl = FibDifficultyLevel()
    fdl.fib_difficulty_level()
    fdl.loginToTest()
    fdl.reportData()

@pytest.mark.transcript
def test_FIB_PerformanceVsOthers_AMH():
    fpvsoamh = FibPerformanceVsOthersAmh()
    fpvsoamh.fib_performance_vs_others_amh()
    fpvsoamh.loginToTest()
    fpvsoamh.reportData()

@pytest.mark.transcript
def test_FIB_SectionWise_QandA_byCount():
    fswqabc = FibSectionWiseQandAByCount()
    fswqabc.fib_section_wise_q_and_a_by_count()
    fswqabc.login()
    fswqabc.reportData()
    fswqabc.logout()

@pytest.mark.transcript
def test_FIB_SectionWise_QandA_byScore():
    fswqabs = FibSectionWiseQandAByScore()
    fswqabs.fib_section_wise_q_and_a_by_score()
    fswqabs.login()
    fswqabs.reportData()
    fswqabs.logout()

@pytest.mark.transcript
def test_FIB_Time_Spent_Per_Quetsion():
    ftspq = FibTimeSpentPerQuestion()
    ftspq.fib_time_spent_per_question()
    ftspq.login()
    ftspq.reportData()
    ftspq.logout()

@pytest.mark.transcript
def test_MCA_Comprehensive():
    mc = McaComprehensive()
    mc.mca_comprehensive()
    mc.login()
    mc.reportData()
    mc.logout()

@pytest.mark.transcript
def test_MCA_Difficulty_Level():
    mdl = McaDifficultyLevel()
    mdl.mca_difficulty_level()
    mdl.loginToTest()
    mdl.reportData()

@pytest.mark.transcript
def test_MCA_PerformanceVsOthers_AMH():
    mcapvsoamh = McaPerformanceVsOthersAmh()
    mcapvsoamh.mca_performance_vs_others_amh()
    mcapvsoamh.loginToTest()
    mcapvsoamh.reportData()

@pytest.mark.transcript
def test_MCA_SectionWise_QandA_byCount():
    mswqabc = McaSectionWiseQandAByCount()
    mswqabc.mca_section_wise_q_and_a_by_count()
    mswqabc.login()
    mswqabc.reportData()
    mswqabc.logout()

@pytest.mark.transcript
def test_MCA_SectionWise_QandA_byScore():
    mcaswqabs = McaSectionWiseQandAByScore()
    mcaswqabs.mca_section_wise_q_and_a_by_score()
    mcaswqabs.login()
    mcaswqabs.reportData()
    mcaswqabs.logout()

@pytest.mark.transcript
def test_MCA_TimeSpentPerQuestion():
    mcatspq = McaTimeSpentPerQuestion()
    mcatspq.mca_time_spent_per_question()
    mcatspq.login()
    mcatspq.reportData()
    mcatspq.logout()

@pytest.mark.transcript
def test_MCQ_Comprehensive():
    mcqc = McqComprehensive()
    mcqc.mcq_comprehensive()
    mcqc.login()
    mcqc.reportData()
    mcqc.logout()

@pytest.mark.transcript
def test_MCQ_DifficultyLevel():
    mcqdl = McqDifficultyLevel()
    mcqdl.mcq_difficulty_level()
    mcqdl.loginToTest()
    mcqdl.reportData()

@pytest.mark.transcript
def test_MCQ_Performance():
    mcqp = McqPerformance()
    mcqp.mcq_performance()
    mcqp.loginToTest()
    mcqp.reportData()

@pytest.mark.transcript
def test_MCQ_PerformanceVsOthers_AMH():
    mcqpvoamh = McqPerformanceVsOthersAmh()
    mcqpvoamh.mcq_performance_vs_others_amh()
    mcqpvoamh.loginToTest()
    mcqpvoamh.reportData()

@pytest.mark.transcript
def test_MCQ_SectionWise_QandA_byCount():
    mcqswqabc = McqSectionWiseQandAByCount()
    mcqswqabc.mcq_section_wise_q_and_a_by_count()
    mcqswqabc.login()
    mcqswqabc.reportData()
    mcqswqabc.logout()

@pytest.mark.transcript
def test_MCQ_SectionWise_QandA_byScore():
    mcqswqabs = McqSectionWiseQandAByScore()
    mcqswqabs.mcq_section_wise_q_and_a_by_score()
    mcqswqabs.login()
    mcqswqabs.reportData()
    mcqswqabs.logout()

@pytest.mark.transcript
def test_MCQ_TimeSpentPerQuestion():
    mcqtspq = McqTimeSpentPerQuestion()
    mcqtspq.mcq_time_spent_per_question()
    mcqtspq.login()
    mcqtspq.reportData()
    mcqtspq.logout()

@pytest.mark.transcript
def test_MCQW_Comprehensive():
    mcqwc = McqwComprehensive()
    mcqwc.mcqw_comprehensive()
    mcqwc.login()
    mcqwc.reportData()
    mcqwc.logout()

@pytest.mark.transcript
def test_MCQW_DifficultyLevel():
    mcqwdl = McqwDifficultyLevel()
    mcqwdl.mcqw_difficulty_level()
    mcqwdl.loginToTest()
    mcqwdl.reportData()

@pytest.mark.transcript
def test_MCQW_PerformanceVsOthers_AMH():
    mcqwpvoamh = McqwPerformanceVsOthersAmh()
    mcqwpvoamh.mcqw_performance_vs_others_amh()
    mcqwpvoamh.loginToTest()
    mcqwpvoamh.reportData()

@pytest.mark.transcript
def test_MCQW_SectionWise_QandA_byCount():
    mcqwswqabc = McqwSectionWiseQandAByCount()
    mcqwswqabc.mcqw_section_wise_q_and_a_by_count()
    mcqwswqabc.login()
    mcqwswqabc.reportData()
    mcqwswqabc.logout()

@pytest.mark.transcript
def test_MCQW_SectionWise_QandA_byScore():
    mcqwswqabs = McqwSectionWiseQandAByScore()
    mcqwswqabs.mcqw_section_wise_q_and_a_by_score()
    mcqwswqabs.login()
    mcqwswqabs.reportData()
    mcqwswqabs.logout()

@pytest.mark.transcript
def test_MCQW_TimeSpentPerQuestion():
    mcqwtspq = McqwTimeSpentPerQuestion()
    mcqwtspq.mcqw_time_spent_per_question()
    mcqwtspq.login()
    mcqwtspq.reportData()
    mcqwtspq.logout()

@pytest.mark.transcript
def test_Overall_Performance():
    op = OverallPerformance()
    op.overall_performance()
    op.loginToTest()
    op.reportData()

@pytest.mark.transcript
def test_Subjective_Performance():
    sp = SubjectivePerformance()
    sp.subjective_performance()
    sp.login()
    sp.reportData()
    sp.logout()