import db.mysql_repository
from model.cognate import *


class Services:

    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    def lookup_cognate(self, surface_form: str, lang: Language) -> Result:
        entries = self.repo.get(surface_form.lower())  # Looks in lexicon table

        if not entries:
            # Check if this specific word is in false_friends
            false_friend_entries = [
                ff for ff in self.repo.load_false_friends()
                if ff['word'].lower() == surface_form.lower()
            ]
            if false_friend_entries:
                return Result(
                    Word(surface_form, None),
                    None,
                    ResultType.FALSE_FRIEND,
                    "This is a false cognate."
                )
            else:
                return Result(
                    Word(surface_form, None),
                    None,
                    ResultType.NO_MATCH,
                    "This is not a cognate."
                )

        # Word exists in lexicon
        input_entry = next((e for e in entries if e.lang == lang), None)

        if not input_entry:
            return Result(
                Word(surface_form, None),
                None,
                ResultType.NO_MATCH,
                "No entry for input language."
            )

        other_lang = Language.SPANISH if lang == Language.ENGLISH else Language.ENGLISH

        for candidate in entries:
            if (
                    candidate.lang == other_lang and
                    candidate.word_origin == input_entry.word_origin and
                    candidate.pos == input_entry.pos
            ):
                input_word = Word(surface_form, input_entry)
                return Result(
                    input_word,
                    candidate,
                    ResultType.COGNATE,
                    "Cognate found."
                )

        input_word = Word(surface_form, input_entry)
        return Result(input_word, None, ResultType.NO_MATCH, "No cognate found.")
