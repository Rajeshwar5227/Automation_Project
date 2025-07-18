import pytest
from scripts.Assessment.Coding_Performance import CodingPerformance
from scripts.Assessment.Coding_Performance_TC_Summary import CodingPerformanceTcSummary
from scripts.Assessment.Coding_QA_Performance import CodingQAPerformance
from scripts.Assessment.FIB_Comprehensive import FibComprehensive
from scripts.Assessment.FIB_Difficulty_Level import FibDifficultyLevel
from scripts.Assessment.FIB_PerformanceVsOthers_AMH import FibPerformanceVsOthersAmh
from scripts.Assessment.FIB_SectionWise_QandA_byCount import FibSectionWiseQandAByCount
from scripts.Assessment.FIB_SectionWise_QandA_byScore import FibSectionWiseQandAByScore
from scripts.Assessment.FIB_TimeSpentPerQuestion import FibTimeSpentPerQuestion
from scripts.Assessment.MCA_Comprehensive import McaComprehensive
from scripts.Assessment.MCA_DifficultyLevel import McaDifficultyLevel
from scripts.Assessment.MCA_PerformanceVsOthers_AMH import McaPerformanceVsOthersAmh
from scripts.Assessment.MCA_SectionWise_QandA_byCount import McaSectionWiseQandAByCount
from scripts.Assessment.MCA_SectionWise_QandA_byScore import McaSectionWiseQandAByScore
from scripts.Assessment.MCA_TimeSpentPerQuestion import McaTimeSpentPerQuestion
from scripts.Assessment.MCQ_Comprehensive import McqComprehensive
from scripts.Assessment.MCQ_DifficultyLevel import McqDifficultyLevel
from scripts.Assessment.MCQ_Performance import McqPerformance
from scripts.Assessment.MCQ_PerformanceVsOthers_AMH import McqPerformanceVsOthersAmh
from scripts.Assessment.MCQ_SectionWise_QandA_byCount import McqSectionWiseQandAByCount
from scripts.Assessment.MCQ_SectionWise_QandA_byScore import McqSectionWiseQandAByScore
from scripts.Assessment.MCQ_TimeSpentPerQuestion import McqTimeSpentPerQuestion
from scripts.Assessment.MCQW_Comprehensive import McqwComprehensive
from scripts.Assessment.MCQW_DifficultyLevel import McqwDifficultyLevel
from scripts.Assessment.MCQW_PerformanceVsOthers_AMH import McqwPerformanceVsOthersAmh
from scripts.Assessment.MCQW_SectionWise_QandA_byCount import McqwSectionWiseQandAByCount
from scripts.Assessment.MCQW_SectionWise_QandA_byScore import McqwSectionWiseQandAByScore
from scripts.Assessment.MCQW_TimeSpentPerQuestion import McqwTimeSpentPerQuestion
from scripts.Assessment.Overall_Performance import OverallPerformance
from scripts.Assessment.Subjective_Performance import SubjectivePerformance


class TestCandidateTranscript:

    def setup_class(self):
        pass

    @pytest.mark.transcript
    def test_coding_performance(self, config_options):
        server = config_options["server"]
        cp_trans = CodingPerformance()
        cp_trans.coding_performance(server)
        cp_trans.loginToTest(server)
        cp_trans.cp_reportData(server)
        cp_trans.file_close()

    @pytest.mark.transcript
    def test_Coding_Performance_TC_Summary(self, config_options):
        server = config_options["server"]
        cptcs_trans = CodingPerformanceTcSummary()
        cptcs_trans.coding_performance_tc_summary(server)
        cptcs_trans.login(server)
        cptcs_trans.report_data(server)

    def test_Coding_QA_Performance(self, config_options):
        server = config_options["server"]
        cqap = CodingQAPerformance()
        cqap.coding_qa_performance(server)
        cqap.login(server)
        cqap.reportData(server)
        cqap.logout(server)

    @pytest.mark.transcript
    def test_FIB_Comprehensive(self, config_options):
        server = config_options["server"]
        fc = FibComprehensive()
        fc.fib_comprehensive(server)
        fc.login(server)
        fc.reportData(server)
        fc.logout(server)

    @pytest.mark.transcript
    def test_FIB_Difficulty_Level(self, config_options):
        server = config_options["server"]
        fdl = FibDifficultyLevel()
        fdl.fib_difficulty_level(server)
        fdl.loginToTest(server)
        fdl.reportData(server)

    @pytest.mark.transcript
    def test_FIB_PerformanceVsOthers_AMH(self, config_options):
        server = config_options["server"]
        fpvsoamh = FibPerformanceVsOthersAmh()
        fpvsoamh.fib_performance_vs_others_amh(server)
        fpvsoamh.loginToTest(server)
        fpvsoamh.reportData(server)

    @pytest.mark.transcript
    def test_FIB_SectionWise_QandA_byCount(self, config_options):
        server = config_options["server"]
        fswqabc = FibSectionWiseQandAByCount()
        fswqabc.fib_section_wise_q_and_a_by_count(server)
        fswqabc.login(server)
        fswqabc.reportData(server)
        fswqabc.logout(server)

    @pytest.mark.transcript
    def test_FIB_SectionWise_QandA_byScore(self, config_options):
        server = config_options["server"]
        fswqabs = FibSectionWiseQandAByScore()
        fswqabs.fib_section_wise_q_and_a_by_score(server)
        fswqabs.login(server)
        fswqabs.reportData(server)
        fswqabs.logout(server)

    @pytest.mark.transcript
    def test_FIB_Time_Spent_Per_Quetsion(self, config_options):
        server = config_options["server"]
        ftspq = FibTimeSpentPerQuestion()
        ftspq.fib_time_spent_per_question(server)
        ftspq.login(server)
        ftspq.reportData(server)
        ftspq.logout(server)

    @pytest.mark.transcript
    def test_MCA_Comprehensive(self, config_options):
        server = config_options["server"]
        mc = McaComprehensive()
        mc.mca_comprehensive(server)
        mc.login(server)
        mc.reportData(server)
        mc.logout(server)

    @pytest.mark.transcript
    def test_MCA_Difficulty_Level(self, config_options):
        server = config_options["server"]
        mdl = McaDifficultyLevel()
        mdl.mca_difficulty_level(server)
        mdl.loginToTest(server)
        mdl.reportData(server)

    @pytest.mark.transcript
    def test_MCA_PerformanceVsOthers_AMH(self, config_options):
        server = config_options["server"]
        mcapvsoamh = McaPerformanceVsOthersAmh()
        mcapvsoamh.mca_performance_vs_others_amh(server)
        mcapvsoamh.loginToTest(server)
        mcapvsoamh.reportData(server)

    @pytest.mark.transcript
    def test_MCA_SectionWise_QandA_byCount(self, config_options):
        server = config_options["server"]
        mswqabc = McaSectionWiseQandAByCount()
        mswqabc.mca_section_wise_q_and_a_by_count(server)
        mswqabc.login(server)
        mswqabc.reportData(server)
        mswqabc.logout(server)

    @pytest.mark.transcript
    def test_MCA_SectionWise_QandA_byScore(self, config_options):
        server = config_options["server"]
        mcaswqabs = McaSectionWiseQandAByScore()
        mcaswqabs.mca_section_wise_q_and_a_by_score(server)
        mcaswqabs.login(server)
        mcaswqabs.reportData(server)
        mcaswqabs.logout(server)

    @pytest.mark.transcript
    def test_MCA_TimeSpentPerQuestion(self, config_options):
        server = config_options["server"]
        mcatspq = McaTimeSpentPerQuestion()
        mcatspq.mca_time_spent_per_question(server)
        mcatspq.login(server)
        mcatspq.reportData(server)
        mcatspq.logout(server)

    @pytest.mark.transcript
    def test_MCQ_Comprehensive(self, config_options):
        server = config_options["server"]
        mcqc = McqComprehensive()
        mcqc.mcq_comprehensive(server)
        mcqc.login(server)
        mcqc.reportData(server)
        mcqc.logout(server)

    @pytest.mark.transcript
    def test_MCQ_DifficultyLevel(self, config_options):
        server = config_options["server"]
        mcqdl = McqDifficultyLevel()
        mcqdl.mcq_difficulty_level(server)
        mcqdl.loginToTest(server)
        mcqdl.reportData(server)

    @pytest.mark.transcript
    def test_MCQ_Performance(self, config_options):
        server = config_options["server"]
        mcqp = McqPerformance()
        mcqp.mcq_performance(server)
        mcqp.loginToTest(server)
        mcqp.reportData(server)

    @pytest.mark.transcript
    def test_MCQ_PerformanceVsOthers_AMH(self, config_options):
        server = config_options["server"]
        mcqpvoamh = McqPerformanceVsOthersAmh()
        mcqpvoamh.mcq_performance_vs_others_amh(server)
        mcqpvoamh.loginToTest(server)
        mcqpvoamh.reportData(server)

    @pytest.mark.transcript
    def test_MCQ_SectionWise_QandA_byCount(self, config_options):
        server = config_options["server"]
        mcqswqabc = McqSectionWiseQandAByCount()
        mcqswqabc.mcq_section_wise_q_and_a_by_count(server)
        mcqswqabc.login(server)
        mcqswqabc.reportData(server)
        mcqswqabc.logout(server)

    @pytest.mark.transcript
    def test_MCQ_SectionWise_QandA_byScore(self, config_options):
        server = config_options["server"]
        mcqswqabs = McqSectionWiseQandAByScore()
        mcqswqabs.mcq_section_wise_q_and_a_by_score(server)
        mcqswqabs.login(server)
        mcqswqabs.reportData(server)
        mcqswqabs.logout(server)

    @pytest.mark.transcript
    def test_MCQ_TimeSpentPerQuestion(self, config_options):
        server = config_options["server"]
        mcqtspq = McqTimeSpentPerQuestion()
        mcqtspq.mcq_time_spent_per_question(server)
        mcqtspq.login(server)
        mcqtspq.reportData(server)
        mcqtspq.logout(server)

    @pytest.mark.transcript
    def test_MCQW_Comprehensive(self, config_options):
        server = config_options["server"]
        mcqwc = McqwComprehensive()
        mcqwc.mcqw_comprehensive(server)
        mcqwc.login(server)
        mcqwc.reportData(server)
        mcqwc.logout(server)

    @pytest.mark.transcript
    def test_MCQW_DifficultyLevel(self, config_options):
        server = config_options["server"]
        mcqwdl = McqwDifficultyLevel()
        mcqwdl.mcqw_difficulty_level(server)
        mcqwdl.loginToTest(server)
        mcqwdl.reportData(server)

    @pytest.mark.transcript
    def test_MCQW_PerformanceVsOthers_AMH(self, config_options):
        server = config_options["server"]
        mcqwpvoamh = McqwPerformanceVsOthersAmh()
        mcqwpvoamh.mcqw_performance_vs_others_amh(server)
        mcqwpvoamh.loginToTest(server)
        mcqwpvoamh.reportData(server)

    @pytest.mark.transcript
    def test_MCQW_SectionWise_QandA_byCount(self, config_options):
        server = config_options["server"]
        mcqwswqabc = McqwSectionWiseQandAByCount()
        mcqwswqabc.mcqw_section_wise_q_and_a_by_count(server)
        mcqwswqabc.login(server)
        mcqwswqabc.reportData(server)
        mcqwswqabc.logout(server)

    @pytest.mark.transcript
    def test_MCQW_SectionWise_QandA_byScore(self, config_options):
        server = config_options["server"]
        mcqwswqabs = McqwSectionWiseQandAByScore()
        mcqwswqabs.mcqw_section_wise_q_and_a_by_score(server)
        mcqwswqabs.login(server)
        mcqwswqabs.reportData(server)
        mcqwswqabs.logout(server)

    @pytest.mark.transcript
    def test_MCQW_TimeSpentPerQuestion(self, config_options):
        server = config_options["server"]
        mcqwtspq = McqwTimeSpentPerQuestion()
        mcqwtspq.mcqw_time_spent_per_question(server)
        mcqwtspq.login(server)
        mcqwtspq.reportData(server)
        mcqwtspq.logout(server)

    @pytest.mark.transcript
    def test_Overall_Performance(self, config_options):
        server = config_options["server"]
        op = OverallPerformance()
        op.overall_performance(server)
        op.loginToTest(server)
        op.reportData(server)

    @pytest.mark.transcript
    def test_Subjective_Performance(self, config_options):
        server = config_options["server"]
        sp = SubjectivePerformance()
        sp.subjective_performance(server)
        sp.login(server)
        sp.reportData(server)
        sp.logout(server)