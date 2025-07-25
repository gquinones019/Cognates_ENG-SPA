from model.cognate import *

def test_is_cognate():
    result = lookup_cognate("animal", Language.SPANISH)
    assert result.result_type == ResultType.COGNATE
    print(result.note)

def test_not_cognate():
    result = lookup_cognate("doll", Language.ENGLISH)
    assert result.result_type == ResultType.NO_MATCH
    print("No match", result.note)
