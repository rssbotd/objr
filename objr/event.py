# This file is placed in the Public Domain.


"event"


class Event:

    "Event"

    def __init__(self):
        self.orig = ""
        self.result = []
        self.thr = None
        self.txt = ""

    def reply(self, txt):
        "add text to the result"
        self.result.append(txt)


def __dir__():
    return (
        'Event',
    )
