import pytest
from anon_survey import AnonymousSurvey

@pytest.fixture
def anon_survery():
    anon = AnonymousSurvey("The question")
    return anon

# Pass the fixture in as an argument
def test_store_response_single(anon_survery):
    anon_survery.store_response("The response")
    assert "The response" in anon_survery.responses


def test_store_response_multi(anon_survery):
    anon_survery.store_response("The response1")
    anon_survery.store_response("The response2")
    anon_survery.store_response("The response3")
    assert "The response3" in anon_survery.responses
    assert len(anon_survery.responses) == 3