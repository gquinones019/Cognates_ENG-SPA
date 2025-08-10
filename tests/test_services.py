from app.services import Services
from model.cognate import Language, ResultType

services = Services()

# This tests if the word is a cognate.

def test_is_cognate():
    result = services.lookup_cognate("animal", Language.SPANISH)
    assert result.result_type == ResultType.COGNATE
    print(result.note)

# This tests if the word is a false friend or false cognate.

def test_false_friends():
    result = services.lookup_cognate("once", Language.ENGLISH)
    assert result.result_type == ResultType.FALSE_FRIEND
    print(result.note)

# This test if a word is not in the cognates database.

def test_not_cognate():
    result = services.lookup_cognate("doll", Language.ENGLISH)
    assert result.result_type == ResultType.NO_MATCH
    print(result.note)

