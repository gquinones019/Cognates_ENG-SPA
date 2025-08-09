from enum import Enum
from typing import Optional

class PartOfSpeech(Enum):
    ADJECTIVE = "Adjective"
    ADVERB = "Adverb"
    NOUN = "Noun"
    PREPOSITION = "Preposition"
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
    PROTO_GERMANIC = "Proto Germanic"
    PROTO_INDO_EUROPEAN = "Proto Indo European"
    SINHALESE = "Sinhalese"

class Language(Enum):
    ENGLISH = "English"
    SPANISH = "Spanish"

class ResultType(Enum):
    COGNATE = "Cognate"
    NO_MATCH = "No Match"
    FALSE_FRIEND = "False Friend"

class LexicalEntry:
    def __init__(self,
                word: str,
                pos: PartOfSpeech,
                definition: str,
                word_origin: WordOrigin,
                lang: Language):
        self.word = word
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
