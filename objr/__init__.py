# This file is placed in the Public Domain.


"""objects reactor


SYNOPSIS

    >>> from objr import Reactor
    >>> reactor.register("command", command)
    >>> reactor.start()


INSTALL

    $ pip install objr


DESCRIPTION

    OBJR is a threaded, defer exceptions for later, keep
    on running callback engine.


COPYRIGHT

    OBJR is Public Domain.

"""


from . import broker, client, errors, event, reactor, thread


from .broker  import *
from .client  import *
from .errors  import *
from .event   import *
from .reactor import *
from .thread  import *


def __dir__():
    return (
        'Broker',
        'Client',
        'Errors',
        'Reactor',
        'Thread',
        'errors',
        'later'
    )
