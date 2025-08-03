from model.cognate import *

lexical_database = {
    "animal": [
        LexicalEntry('animal', PartOfSpeech.NOUN, "any living creature, including humans", WordOrigin.LATIN, Language.ENGLISH),
        LexicalEntry('animal', PartOfSpeech.NOUN, "Ser orgánico que vive, siente y se mueve por propio impulso", WordOrigin.LATIN, Language.SPANISH)
    ],
    "flexible": [
        LexicalEntry('flexible', PartOfSpeech.ADJECTIVE,"to bend", WordOrigin.LATIN, Language.ENGLISH),
        LexicalEntry('flexible', PartOfSpeech.ADJECTIVE, "Que tiene disposición para doblarse fácilmente", WordOrigin.LATIN, Language.SPANISH)

    ]
}

def lookup_cognate(surface_form: str, lang: Language) -> Result:
    entries = lexical_database.get(surface_form.lower())

    if not entries:
        return Result(Word(surface_form, None), None, ResultType.NO_MATCH, "Word not found in database.")

    input_entry = next((e for e in entries if e.lang == lang), None)

    if not input_entry:
        return Result(Word(surface_form, None), None, ResultType.NO_MATCH, "No entry for input language.")

    other_lang = Language.SPANISH if lang == Language.ENGLISH else Language.ENGLISH

    for candidate in entries:
        if candidate.lang == other_lang and candidate.word_origin == input_entry.word_origin and candidate.pos == input_entry.pos:
            input_word = Word(surface_form, input_entry)
            return Result(input_word, candidate, ResultType.COGNATE, "Cognate found.")

    input_word = Word(surface_form, input_entry)
    return Result(input_word, None, ResultType.NO_MATCH, "No cognate found.")

def test_is_cognate():
    result = lookup_cognate("animal", Language.SPANISH)
    assert result.result_type == ResultType.COGNATE
    print(result.note)

def test_not_cognate():
    result = lookup_cognate("doll", Language.ENGLISH)
    assert result.result_type == ResultType.NO_MATCH
    print("No match", result.note)
