# This file is placed in the Public Domain.


"list of commands"


from objx.face import keys
from objr.cmds   import Commands


def cmd(event):
    "list commands."
    event.reply(",".join(sorted(keys(Commands.cmds))))
