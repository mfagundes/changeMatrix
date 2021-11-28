from textwrap import dedent
import pytest as pytest

from matriz import create_array, string


def test_create():
    board = create_array(['4', '5'])
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )
