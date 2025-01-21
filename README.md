# RegDurations

This library allows to simply parse durations written in a string, in multiple supported languages.

## Usage
``` python
from regdurations import DurationParser

duration_parser = DurationParser()
# optionally specify a list of supported languages:
duration_parser = DurationParser(allowed_languages=['it', 'en'])

duration_parser.find_relativedelta('3 weeks 10y 4 anni 5 minuti')
>>> (relativedelta(years=+14, days=+21, minutes=+5), 0, 27)  # result, starting index, ending index
# or, if dateutil is not installed:
duration_parser.find_dict('4s 23gg 78 settimane')
>>> ({'seconds': 4, 'minutes': 0, 'hours': 0, 'days': 23, 'weeks': 78, 'months': 0, 'years': 0}, 0, 20)
```

## Supported Languages
* `EN`, `IT`, `FR`, `DE`, `ES`
* Contributions for new languages are accepted

## Credits
Thanks to [CalledLuca](https://github.com/CalledLuca) for the idea and the `FR`, `DE`, `ES` languages!

## License
This project is licensed under the **Boost Software License**. Please take a look.
