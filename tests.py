#!/usr/bin/env python
from py.test import main, raises
from math import isclose

from FILE import FUNCTION


def test_foo():
    assert foo(1,2) == 2

    with raises(ValueError):
        foo(5,4)


if __name__ == '__main__':
    main()