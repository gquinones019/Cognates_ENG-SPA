from enum import Enum
from typing import Optional

class PartOfSpeech(Enum):
    ADJECTIVE = "Adjective"
    ADVERB = "Adverb"
    NOUN = "Noun"
    VERB = "Verb"

class WordOrigin(Enum):
    ARABIC = "Arabic"
    ENGLISH = "English"
    FRENCH = "French"
    GREEK = "Greek"
    ITALIAN = "Italian"
    LATIN = "Latin"
    MANDE = "Mande"
    NAHUATL = "Nahuatl"
    SINHALESE = "Sinhalese"

class Language(Enum):
    ENGLISH = "English"
    SPANISH = "Spanish"

class ResultType(Enum):
    COGNATE = "Cognate"
    NO_MATCH = "No Match"

class LexicalEntry:
    def __init__(self,
                pos: PartOfSpeech,
                definition: str,
                word_origin: WordOrigin,
                lang: Language):
        self.pos = pos
        self.definition = definition
        self.word_origin = word_origin
        self.lang = lang

class Word:
    def __init__(self,
                 surface_form: str,
                 lex_entry: LexicalEntry):
        self.surface_form = surface_form
        self.lex_entry = lex_entry

class Result:
    def __init__(self,
                 input_word: Word,
                 matched_entry: Optional[LexicalEntry],
                 result_type: ResultType,
                 note: str = ""):
        self.input_word = input_word
        self.matched_entry = matched_entry
        self.result_type = result_type
        self.note = note

lexical_database = {
    "animal": [
        LexicalEntry(PartOfSpeech.NOUN, "any living creature, including humans", WordOrigin.LATIN, Language.ENGLISH),
        LexicalEntry(PartOfSpeech.NOUN, "Ser orgánico que vive, siente y se mueve por propio impulso", WordOrigin.LATIN, Language.SPANISH)
    ],
    "flexible": [
        LexicalEntry(PartOfSpeech.ADJECTIVE,"to bend", WordOrigin.LATIN, Language.ENGLISH),
        LexicalEntry(PartOfSpeech.ADJECTIVE, "Que tiene disposición para doblarse fácilmente", WordOrigin.LATIN, Language.SPANISH)

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

