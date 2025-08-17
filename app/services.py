import db.mysql_repository
from model.cognate import *


class Services:
    def __init__(self):
        self.repo = db.mysql_repository.MysqlRepository()

    def lookup_cognate(self, surface_form: str, lang: Language) -> Result:
        # Step 1: Check for true cognates first
        entries = self.repo.get(surface_form.lower())
        input_entry = next((e for e in entries if e.lang == lang), None)

        if input_entry:
            # The word exists in the lexicon for the input language.
            # Now check for a cognate in the other language.
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

        # Step 2: If no true cognate is found, check for false cognates
        false_friends = self.repo.load_false_friends()
        false_friend_entry = next(
            (ff for ff in false_friends if ff['word'].lower() == surface_form.lower()),
            None
        )

        if false_friend_entry:
            return Result(
                Word(surface_form, None),
                None,
                ResultType.FALSE_FRIEND,
                "This is a false cognate."
            )

        # Step 3: If not a true or false cognate, it's not a cognate at all
        return Result(
            Word(surface_form, None),
            None,
            ResultType.NO_MATCH,
            "This is not a cognate."
        )