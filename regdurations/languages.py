from enum import Enum

VALID_KEYS = ('seconds', 'minutes', 'hours', 'days', 'weeks', 'months', 'years')
SEP_WORD_KEY = 'sep'

class Languages(str, Enum):
    ENGLISH = "en"
    ITALIAN = "it"
    FRENCH = "fr"
    SPANISH = "es"
    GERMAN = "de"

DURATION_VALUES = {
    Languages.ENGLISH: {
        "seconds": ["s", "second", "seconds"],
        "minutes": ["m", "min", "minute", "minutes"],
        "hours": ["h", "hour", "hours"],
        "days": ["d", "day", "days"],
        "weeks": ["w", "week", "weeks"],
        "months": ["mo", "month", "months"],
        "years": ["y", "year", "years"],
        SEP_WORD_KEY: ["and"]
    },
    Languages.ITALIAN: {
        "seconds": ["s", "secondo", "secondi"],
        "minutes": ["m", "min", "minuto", "minuti"],
        "hours": ["h", "o", "ora", "ore"],
        "days": ["g", "gg", "giorno", "giorni"],
        "weeks": ["sett", "settimana", "settimane"],
        "months": ["mese", "mesi"],
        "years": ["a", "anno", "anni"],
        SEP_WORD_KEY: ["e", "ed"]
    },

    Languages.FRENCH: {
        "seconds": ["s", "seconde", "secondes"],
        "minutes": ["m", "min", "minute", "minutes"],
        "hours": ["h", "heure", "heures"],
        "days": ["j", "jour", "jours"],
        "weeks": ["sem", "semaine", "semaines"],
        "months": ["mois"],
        "years": ["an", "année", "années", "ans"],
        SEP_WORD_KEY: ["et"]
    },
    Languages.SPANISH: {
        "seconds": ["s", "segundo", "segundos"],
        "minutes": ["m", "min", "minuto", "minutos"],
        "hours": ["h", "hora", "horas"],
        "days": ["d", "día", "días"],
        "weeks": ["sem", "semana", "semanas"],
        "months": ["mes", "meses"],
        "years": ["a", "año", "años"],
        SEP_WORD_KEY: ["y"]
    },
    Languages.GERMAN: {
        "seconds": ["s", "sekunde", "sekunden"],
        "minutes": ["m", "min", "minute", "minuten"],
        "hours": ["h", "stunde", "stunden"],
        "days": ["t", "tag", "tage"],
        "weeks": ["w", "woche", "wochen"],
        "months": ["mo", "monat", "monate"],
        "years": ["j", "jahr", "jahre"],
        SEP_WORD_KEY: ["und"]
    }
}
