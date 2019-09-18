from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.choo.api.manager import Manager
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class ChooCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_choo(self, args, arguments):
        """
        ::

          Usage:
                choo --file=FILE
                choo [-d | -t]

          Prints a magnificent train! 

          Arguments:
              FILE   a file name

          Options:
              -h --help
              -f     specify the file
              -d     default train print 
              -t     traverse!

        """
        arguments.FILE = arguments['--file'] or None

        VERBOSE(args)
        VERBOSE(arguments)

        m = Manager()

        if arguments.FILE:
            m.list(path_expand(arguments.FILE))
            m.print_file(arguments.FILE)

        elif arguments['-d']:
            m.train_default()
        
        elif arguments['-t']:
            m.train_move()    

        return ""
