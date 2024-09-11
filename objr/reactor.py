# This file is placed in the Public Domain.
# pylint: disable=W0212,W0718


"reactor"


import queue
import threading
import _thread


class Reactor:

    "Reactor"

    def __init__(self):
        self.cbs      = {}
        self.queue    = queue.Queue()
        self.stopped  = threading.Event()

    def callback(self, evt):
        "call callback based on event type."
        func = self.cbs.get(evt.type, None)
        if not func:
            return
        if "target" in dir(func) and func.target not in str(func).lower():
            return
        func(self, evt)

    def loop(self):
        "proces events until interrupted."
        while not self.stopped.is_set():
            try:
                evt = self.poll()
                self.callback(evt)
            except (KeyboardInterrupt, EOFError):
                _thread.interrupt_main()

    def poll(self):
        "function to return event."
        return self.queue.get()

    def put(self, evt):
        "put event into the queue."
        self.queue.put_nowait(evt)

    def register(self, typ, cbs):
        "register callback for a type."
        self.cbs[typ] = cbs

    def start(self):
        "start the event loop."
        self.loop()

    def stop(self):
        "stop the event loop."
        self.stopped.set()


def __dir__():
    return (
        'Reactor',
    )
