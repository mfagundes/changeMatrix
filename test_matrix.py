from textwrap import dedent
import pytest as pytest

from matriz import create_array, string, clean_array, color_pixel, ver_pixel


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
