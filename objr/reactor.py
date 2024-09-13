# This file is placed in the Public Domain.
# pylint: disable=R0903,W0105,W0212,W0613,W0718


"reactor"


import io
import queue
import threading
import time
import traceback
import _thread


from .errors import later
from .thread import launch


class Reactor:

    "Reactor"

    def __init__(self):
        self.cbs      = {}
        self.queue    = queue.Queue()
        self.stopped  = threading.Event()

    def callback(self, evt):
        "call callback based on event type."
        func = self.cbs.get(evt.type, None)
        if func:
            evt.thr = launch(func, self, evt)

    def loop(self):
        "proces events until interrupted."
        while not self.stopped.is_set():
            try:
                evt = self.poll()
                self.callback(evt)
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()
            except Exception as ex:
                time.sleep(1.0)
                later(ex)

    def poll(self):
        "function to return event."
        return self.queue.get()

    def put(self, evt):
        "put event into the queue."
        self.queue.put_nowait(evt)

    def ready(self):
        while 1:
            if self.queue.qsize() == 0:
                break
            time.sleep(0.1)

    def register(self, typ, cbs):
        "register callback for a type."
        self.cbs[typ] = cbs

    def start(self):
        "start the event loop."
        launch(self.loop)

    def stop(self):
        "stop the event loop."
        self.stopped.set()


def __dir__():
    return (
        'Reactor',
    )
