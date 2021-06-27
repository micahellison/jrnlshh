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

        print('Press Ctrl+C or Ctrl+Z or whatever the keyboard interrupt is when done.')
        txt_input = silently_get_characters()
              
        journal.entries.append(Entry.Entry(journal, datetime.datetime.now(), txt_input))


def silently_get_characters():
    txt_input = ''

    while True:
        get_character = getch()
        if isinstance(get_character, bytes):
            get_character = get_character.decode("utf-8")

        if get_character == '\x1a': # ctrl+Z
            return txt_input

        if get_character == '\x03': # ctrl+C
            raise KeyboardInterrupt

        txt_input = txt_input + get_character
