from db.repository import *
import mysql.connector


class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        """
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': 32000,
            'database': 'cognates_db',
        }
        """

        config = {
            'user': 'root',
            'password': 'root',
            'host': 'db',
            'port': 3306,
            'database': 'cognates_db',
        }

        self.connection = None
        self.cursor = None

        try:
            self.connection = mysql.connector.connect(**config)
            self.cursor = self.connection.cursor()
            print("Successfully connected to MySQL and obtained cursor!")
        except mysql.connector.Error as err:
            print(f"Error connecting to MySQL: {err}")
            raise  # Important: Re-raise the exception so connection failures are not silently passed over.
        except Exception as e:
            print(f"An unexpected error occurred during MySQL connection: {e}")
            raise

    def __del__(self):
            # Add checks to ensure connection and cursor exist before trying to close them
            try:
                if self.cursor:
                    self.cursor.close()
            except Exception:
                pass
            try:
                if self.connection and self.connection.is_connected():
                    self.connection.close()
            except Exception:
                pass

    def map_pos(self, entry: dict) -> PartOfSpeech:
        pos_switcher = {'adjective': PartOfSpeech.ADJECTIVE,
                        'adverb': PartOfSpeech.ADVERB,
                        'noun': PartOfSpeech.NOUN,
                        'preposition': PartOfSpeech.PREPOSITION,
                        'verb': PartOfSpeech.VERB}
        pos = pos_switcher.get(entry.get('pos'), None)
        return pos

    def map_word_origin(self, entry: dict) -> WordOrigin:
        word_origin_switcher = {'arabic': WordOrigin.ARABIC,
                                'english': WordOrigin.ENGLISH,
                                'french': WordOrigin.FRENCH,
                                'greek': WordOrigin.GREEK,
                                'italian': WordOrigin.ITALIAN,
                                'latin': WordOrigin.LATIN,
                                'mande': WordOrigin.MANDE,
                                'nahuatl': WordOrigin.NAHUATL,
                                'proto germanic': WordOrigin.PROTO_GERMANIC,
                                'proto indo european': WordOrigin.PROTO_INDO_EUROPEAN,
                                'sinhalese': WordOrigin.SINHALESE}
        word_origin = word_origin_switcher.get(entry.get('word_origin'), None)
        return word_origin

    def map_language(self, entry: dict) -> Language:
        language_switcher = {'English': Language.ENGLISH,
                             'Spanish': Language.SPANISH}
        language = language_switcher.get(entry.get('language'), None)
        return language

    def mapper(self, entry: dict) -> LexicalEntry:
        lexical_entry = LexicalEntry(word=entry.get('word'),
                                     pos=self.map_pos(entry),
                                     definition=entry.get('definition'),
                                     word_origin=self.map_word_origin(entry),
                                     lang=self.map_language(entry))
        return lexical_entry


    def load_lexicon(self) -> list[LexicalEntry]:
        sql = 'SELECT * FROM lexicon'
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'word': word,
                    'pos': pos,
                    'definition': definition,
                    'word_origin': word_origin,
                    'language': lang
                    } for (id, word, pos, definition, word_origin, lang) in self.cursor]
        lexicon = [self.mapper(entry) for entry in entries]
        return lexicon

    def load_false_friends(self) -> list[LexicalEntry]:
        sql = 'SELECT * FROM false_friends'
        self.cursor.execute(sql)
        entries = [{'id': id,
                    'word': word,
                    'pos': pos,
                    'definition': definition,
                    'word_origin': word_origin,
                    'language': lang
                    } for (id, word, pos, definition, word_origin, lang) in self.cursor]
        return entries

    def get(self, word: str) -> list[LexicalEntry]:
        sql = "SELECT * FROM lexicon WHERE word = %s"
        self.cursor.execute(sql, (word,))
        entries = [{'id': id,
                    'word': word,
                    'pos': pos,
                    'definition': definition,
                    'word_origin': word_origin,
                    'language': lang
                    } for (id, word, pos, definition, word_origin, lang) in self.cursor]
        lexicon = [self.mapper(entry) for entry in entries]
        return lexicon



