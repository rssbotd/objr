README
######

NAME

::

    OBJR - objects runtime


SYNOPSIS

::

    objr  <cmd> [key=val] [key==val]
    objr  [-a] [-c] [-d] [-i] [-v]

    options are:

    -a     load all modules
    -c     start console
    -d     run in the background
    -h     show help
    -i     start services
    -v     use verbose


INSTALL

::

    $ pipx install objr
    $ pipx ensurepath


DESCRIPTION

::
    OBJR contains all the python3 code to program objects in a functional
    way. It provides a base Object class that has only dunder methods, all
    methods are factored out into functions with the objects as the first
    argument. It is called Object Programming (OP), OOP without the
    oriented.

    OBJR  allows for easy json save//load to/from disk of objects. It
    provides an "clean namespace" Object class that only has dunder
    methods, so the namespace is not cluttered with method names. This
    makes storing and reading to/from json possible.

    OBJR has all you need to program a unix cli program, such as disk
    perisistence for configuration files, event handler to handle the
    client/server connection, code to introspect modules for
    commands, deferred exception handling to not crash on an error, a
    parser to parse commandline options and values, etc.

    OBJR has a demo bot, it can connect to IRC, fetch and display RSS
    feeds, take todo notes, keep a shopping list and log text. You can
    also copy/paste the service file and run it under systemd for 24/7
    presence in a IRC channel.

    OBJR is Public Domain.


CONFIGURATION

::

    $ objr cfg 
    channel=#objr commands=True nick=objr port=6667 server=localhost

    irc

    $ objr cfg server=<server>
    $ objr cfg channel=<channel>
    $ objr cfg nick=<nick>

    sasl

    $ objr pwd <nsvnick> <nspass>
    $ objr cfg password=<frompwd>

    rss

    $ objr rss <url>
    $ objr dpl <url> <item1,item2>
    $ objr rem <url>
    $ objr nme <url> <name>


USAGE

::

    without any argument the program does nothing

    $ objr
    $

    see list of commands

    $ objr cmd
    cmd,err,mod,req,thr,ver

    list of modules

    $ objr mod
    cmd,err,fnd,irc,log,mod,req,rss,tdo,thr

    use -c to start a console

    $ objr -c

    use mod=<name1,name2> to load additional modules

    $ objr -c mod=irc,rss
    >

    use -v for verbose

    $ objr -civ mod=irc
    Jun 25 13:00:56 2024 OBJR CV CMD,ERR,FND,IRC,MOD,OPM,RSS,THR,TMR,UPT,VER
    >


COMMANDS

::

    cmd - commands
    cfg - irc configuration
    dlt - remove a user
    dpl - sets display items
    fnd - find objects 
    log - log some text
    met - add a user
    mre - displays cached output
    pwd - sasl nickserv name/pass
    rem - removes a rss feed
    rss - add a feed
    thr - show the running threads

SYSTEMD

::

    save the following it in /etc/systemd/system/objr.service and
    replace "<user>" with the user running pipx

    [Unit]
    Description=object runtime
    Requires=network-online.target
    After=network-online.target

    [Service]
    Type=simple
    User=<user>
    Group=<user>
    WorkingDirectory=/home/<user>/.objr
    ExecStart=/home/<user>/.local/pipx/venvs/objr/bin/objr -d
    RemainAfterExit=yes

    [Install]
    WantedBy=default.target

    then run this

    $ mkdir ~/.objr
    $ sudo systemctl enable objr --now

    default channel/server is #objr on localhost

FILES

::

    ~/.objr
    ~/.local/bin/objr
    ~/.local/pipx/venvs/objr/

AUTHOR

::

    xobjectz <objx@proton.me>

COPYRIGHT

::

    OBJR is Public Domain.
