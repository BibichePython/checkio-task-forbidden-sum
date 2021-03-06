from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee

from tests import TESTS

def forbidden(code, runner):
    f_words = ["sum", "import", "for", "while", "reduce"]
    for w in f_words:
        if w in code:
            return False, "I found '{0}' in you code.".format(w)
    return True, "ok"

api.add_listener(
    ON_CONNECT,
    CheckiOReferee(
        tests=TESTS,
        inspector=forbidden).on_ready)
