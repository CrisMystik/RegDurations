# Copyright CrisMystik (https://t.me/CrisMystik) 2025-2025.
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE_1_0.txt or copy at
#  https://www.boost.org/LICENSE_1_0.txt)

import re
from typing import Union
from .languages import Languages, DURATION_VALUES, VALID_KEYS, SEP_WORD_KEY

__all__ = ['Languages', 'VALID_KEYS', 'DurationParser']

class DurationParser:
    def __init__(self, allowed_languages: Union[list[str], None] = None):
        self.allowed_patterns = {}
        sep_words = []
        all_patterns = set()

        for lang, lang_patterns in DURATION_VALUES.items():
            if (allowed_languages is not None) and (lang not in allowed_languages):
                continue
            for key, patterns in lang_patterns.items():
                if key == SEP_WORD_KEY:
                    sep_words.extend(patterns)
                if key not in self.allowed_patterns:
                    self.allowed_patterns[key] = set()
                self.allowed_patterns[key].update(patterns)
                all_patterns.update(patterns)

        patterns_reg = "|".join(re.escape(p) for p in all_patterns)
        sep_reg = "|".join(re.escape(sep) for sep in sep_words)
        self.regex = re.compile(
            rf"(?i) (?: (?:([0-9]+)\s*({patterns_reg})) | ({sep_reg}) ) (?:[\s,]+|$)".replace(" ", "")
        )

    def find_dict(self, text: str) -> tuple[dict[str, int], Union[int, None], Union[int, None]]:
        matches = [m for m in self.regex.finditer(text) if m]
        first = None
        last = None
        result = {k: 0 for k in VALID_KEYS}

        for match in matches:
            if (not match) or (not match.group().strip()):
                break
            if first is None:
                first = match.start()
            if (last is not None) and (match.start() != last):
                break
            last = match.end()

            if match.group(3):
                continue

            match_type = next(
                (k for k, v in self.allowed_patterns.items() if match.group(2).lower() in v), None
            )

            result[match_type] += int(match.group(1))

        return result, first, last

    def find_relativedelta(self, text: str) -> tuple['relativedelta', Union[int, None], Union[int, None]]:
        raise ModuleNotFoundError('dateutil module not available')

try:
    from dateutil.relativedelta import relativedelta
    def find_relativedelta(self: DurationParser, text: str) -> tuple[relativedelta, Union[int, None], Union[int, None]]:
        raw, first, last = self.find_dict(text)
        return relativedelta(
            years=raw['years'], months=raw['months'], days=raw['days'],
            weeks=raw['weeks'], hours=raw['hours'], minutes=raw['minutes'],
            seconds=raw['seconds']
        ), first, last
    DurationParser.find_relativedelta = find_relativedelta
except ModuleNotFoundError:
    pass
