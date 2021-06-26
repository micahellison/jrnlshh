import datetime

from getch import getch

from jrnl import Entry
from jrnl.plugins.base import BaseImporter

__version__ = '0.1'

class Importer(BaseImporter):

    names = ["shh"]
    version = __version__

    @staticmethod
    def import_(journal, input=None):
        """
        Prompt the user for input until they interrupt,
        then add the input to a new journal entry.
        """

        txtInput = ''

        print('Press Ctrl+C or Ctrl+Z or whatever the keyboard interrupt is when done.')
        
        try:
            while True:
                txtInput = txtInput + getch()
              
        except KeyboardInterrupt:
            journal.entries.append(Entry.Entry(journal, datetime.datetime.Now(), txtInput))
