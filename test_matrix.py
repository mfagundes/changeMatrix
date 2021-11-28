import io
from textwrap import dedent
from unittest.mock import patch

import pytest as pytest

from matriz import create_array, string, clean_array, color_pixel, ver_pixel, hor_pixel, block_pixel, save_array, \
    fill_pixel


@pytest.fixture
def board():
    return create_array(['4', '5'])


def test_create(board):
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )

def test_clean():
    board = create_array(['4', '5'], 'X')  # aqui ele fica porque tem o X
    board = clean_array(board)
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OOOO
        OOOO
        OOOO'''
    )

def test_pixel(board):
    board = color_pixel('2 2 W'.split(), board)
    assert string(board) == dedent(
        '''\
        OOOO
        OWOO
        OOOO
        OOOO
        OOOO'''
    )

def test_vertical(board):
    ver_pixel('2 2 4 W'.split(), board)
    assert string(board) == dedent(
        '''\
        OOOO
        OWOO
        OWOO
        OWOO
        OOOO'''
    )

def test_horizontal(board):
    hor_pixel('2 3 3 W'.split(), board)
    assert string(board) == dedent(
        '''\
        OOOO
        OOOO
        OWWO
        OOOO
        OOOO'''
    )

def test_block(board):
    block_pixel('2 2 3 4 W'.split(), board)
    assert string(board) == dedent(
        '''\
        OOOO
        OWWO
        OWWO
        OWWO
        OOOO'''
    )

def test_save(board):
    with patch('builtins.open', spec=io.IOBase) as mock:
        save_array('out.bmp', board)

    file = mock.return_value.__enter__.return_value
    file.write.assert_called_once_with(string(board))

def test_fill(board):
    for n in range(1, 5):
        board = color_pixel(f'{n} {n} X'.split(), board)

    board = fill_pixel('3 2 +'.split(), board)

    assert string(board) == dedent(
        '''\
        X+++
        OX++
        OOX+
        OOOX
        OOOO'''
    )

