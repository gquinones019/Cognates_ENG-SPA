from model.cognate import *

def test_enum_values():
    assert PartOfSpeech.NOUN.value == "Noun"
    assert WordOrigin.LATIN.value == "Latin"
    assert Language.ENGLISH.value == "English"
    assert ResultType.COGNATE.value == "Cognate"


def test_create_lexical_entry():
    entry = LexicalEntry(
        word="libro",
        pos=PartOfSpeech.NOUN,
        definition="book",
        word_origin=WordOrigin.LATIN,
        lang=Language.SPANISH
    )
    assert entry.word == "libro"
    assert entry.pos == PartOfSpeech.NOUN
    assert entry.definition == "book"
    assert entry.word_origin == WordOrigin.LATIN
    assert entry.lang == Language.SPANISH


def test_create_word_with_lexical_entry():
    entry = LexicalEntry(
        word="libro",
        pos=PartOfSpeech.NOUN,
        definition="book",
        word_origin=WordOrigin.LATIN,
        lang=Language.SPANISH
    )
    word = Word(surface_form="libro", lex_entry=entry)
    assert word.surface_form == "libro"
    assert word.lex_entry is entry


def test_result_with_matched_entry():
    entry = LexicalEntry(
        word="book",
        pos=PartOfSpeech.NOUN,
        definition="A set of written pages",
        word_origin=WordOrigin.PROTO_GERMANIC,
        lang=Language.ENGLISH
    )
    word = Word(surface_form="book", lex_entry=entry)
    result = Result(
        input_word=word,
        matched_entry=entry,
        result_type=ResultType.COGNATE,
        note="Common Latin root"
    )
    assert result.input_word is word
    assert result.matched_entry is entry
    assert result.result_type == ResultType.COGNATE
    assert result.note == "Common Latin root"

def test_result_without_matched_entry():
    entry = LexicalEntry(
        word="mesa",
        pos=PartOfSpeech.NOUN,
        definition="table",
        word_origin=WordOrigin.LATIN,
        lang=Language.SPANISH
    )
    word = Word(surface_form="mesa", lex_entry=entry)
    result = Result(
        input_word=word,
        matched_entry=None,
        result_type=ResultType.NO_MATCH
    )
    assert result.matched_entry is None
    assert result.result_type == ResultType.NO_MATCH
