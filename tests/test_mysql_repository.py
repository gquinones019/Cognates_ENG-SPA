from db.mysql_repository import *
from model.cognate import PartOfSpeech, WordOrigin, Language

repo = MysqlRepository()

english = {'id': 11,
           'word': 'cereal',
           'pos': 'noun',
           'definition': 'a food that is made from grain and eaten with milk, especially in the morning',
           'word_origin': 'latin',
           'language': 'English'}

spanish = {'id': 12,
           'word': 'cereal',
           'pos': 'noun',
           'definition': 'Planta gramínea cultivada principalmente por su grano, muy utilizado en la alimentación humana y animal, y de la que existen numerosas especies, como el trigo y la cebada.',
           'word_origin': 'latin',
           'language': 'Spanish'}


def test_pos_eng():
    pos = repo.map_pos(english)
    assert pos == PartOfSpeech.NOUN

def test_pos_span():
    pos = repo.map_pos(spanish)
    assert pos == PartOfSpeech.NOUN

def test_origin_eng():
    origin = repo.map_word_origin(english)
    assert origin == WordOrigin.LATIN

def test_origin_span():
    origin = repo.map_word_origin(spanish)
    assert origin == WordOrigin.LATIN

def test_mapper_eng():
    eng = repo.mapper(english)
    assert eng.pos == PartOfSpeech.NOUN
    assert eng.word_origin == WordOrigin.LATIN
    assert eng.lang == Language.ENGLISH

def test_mapper_spa():
    spa = repo.mapper(spanish)
    assert spa.pos == PartOfSpeech.NOUN
    assert spa.word_origin == WordOrigin.LATIN
    assert spa.lang == Language.SPANISH

def test_load_lexicon():
    lexicon = repo.load_lexicon()
    assert len(lexicon) >= 46

