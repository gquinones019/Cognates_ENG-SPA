from db.repository import *
import mysql.connector


class MysqlRepository(Repository):
    def __init__(self):
        super().__init__()
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': 32000,
            'database': 'cognates_db'
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
        if self.cursor:  # Check if cursor object exists (i.e., not None)
            self.cursor.close()
                # print("MySQL cursor closed.") # Optional: for debugging
        if self.connection and self.connection.is_connected():  # Check if connection exists AND is still open
            self.connection.close()
                # print("MySQL connection closed.") # Optional: for debugging
        else:
                # This 'else' block will catch cases where connection was never established or already closed
                # print("No active MySQL connection or cursor to close.") # Optional: for debugging
            pass  # Or just do nothing, which is fine


        """
    def __del__(self):
        try:
            if hasattr(self, 'cursor') and self.cursor:
                self.cursor.close()
            if hasattr(self, 'connection') and self.connection:
                self.connection.close()
        except Exception:
            pass
        """

    def map_pos(self, entry: dict) -> PartOfSpeech:
        pos_switcher = {'adjective': PartOfSpeech.ADJECTIVE,
                        'adverb': PartOfSpeech.ADVERB,
                        'noun': PartOfSpeech.NOUN,
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

    """
    def lexical(self) -> LexicalEntry:
        lexicon = self.load_lexicon()
        if lexicon:
            return lexicon[0]
        else:
            raise ValueError("No lexical entries found in the database.")
    """