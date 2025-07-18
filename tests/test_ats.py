import pytest
from scripts.ATS.ats_baseimplementation import ATS_BaseImplementation
from scripts.ATS.ats_legato import ATS_Legato


@pytest.mark.ats
def test_base_implementation():
    bimp = ATS_BaseImplementation()
    bimp.get_token()
    bimp.get_data()
    bimp.register_tag_candidate_to_test()

@pytest.mark.ats
def test_legato():
    lgt = ATS_Legato()
    lgt.get_token()
    lgt.get_data()
    lgt.registerAndTagCandidateToTest()


