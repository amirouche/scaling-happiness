import time
import operator
import random
import lbst


def test_mic():
    assert lbst._mic()


MAGIC = 100
TREE_MAX_SIZE = 10000 # random.randint(MAGIC, MAGIC * 100)
INTEGER_MAX = random.randint(MAGIC, MAGIC * 10_000)


def test_balanced_and_sorted_random_trees_of_integers():
    for _ in range(MAGIC):
        # given
        expected = dict()
        tree = lbst.make()
        for i in range(TREE_MAX_SIZE):
            key = value = random.randint(-INTEGER_MAX, INTEGER_MAX)
            tree = lbst.set(tree, key, value)
            expected[key] = value
        # when
        out = tuple(lbst.to_dict(tree).items())
        # then
        assert lbst._is_balanced(tree)
        expected = tuple(sorted(expected.items()))
        assert out == expected


def test_balanced_and_sorted_random_trees_of_floats():
    for _ in range(MAGIC):
        # given
        expected = dict()
        tree = lbst.make()
        for i in range(TREE_MAX_SIZE):
            key = value = random.uniform(-INTEGER_MAX, INTEGER_MAX)
            tree = lbst.set(tree, key, value)
            expected[key] = value
        # when
        out = tuple(lbst.to_dict(tree).items())
        # then
        assert lbst._is_balanced(tree)
        expected = tuple(sorted(expected.items()))
        assert out == expected


def test_min():
    for _ in range(MAGIC):
        values = [
            random.randint(-INTEGER_MAX, INTEGER_MAX) for _ in range(TREE_MAX_SIZE)
        ]
        values = sorted(values)

        tree = lbst.make()
        for value in values:
            tree = lbst.set(tree, value, value)

        assert lbst.min(tree) == values[0]


def test_max():
    for _ in range(MAGIC):
        values = [
            random.randint(-INTEGER_MAX, INTEGER_MAX) for _ in range(TREE_MAX_SIZE)
        ]
        values = sorted(values)

        tree = lbst.make()
        for value in values:
            tree = lbst.set(tree, value, value)

        assert lbst.max(tree) == values[-1]


def test_cursor_next():
    for _ in range(MAGIC):
        values = [
            random.randint(-INTEGER_MAX, INTEGER_MAX) for _ in range(TREE_MAX_SIZE)
        ]
        values = sorted(set(values))

        tree = lbst.make()
        for value in values:
            tree = lbst.set(tree, value, value)

        min = lbst.min(tree)
        assert min == values[0]

        cursor = lbst.cursor(tree)
        lbst.cursor_seek(cursor, min)
        assert lbst.cursor_key(cursor) == values[0]

        for index in range(1, len(values)):
            lbst.cursor_next(cursor)
            assert lbst.cursor_key(cursor) == values[index]

        assert not lbst.cursor_next(cursor)


def test_cursor_previous():
    for _ in range(MAGIC):
        values = [
            random.randint(-INTEGER_MAX, INTEGER_MAX) for _ in range(TREE_MAX_SIZE)
        ]
        values = sorted(set(values))

        tree = lbst.make()
        for value in values:
            tree = lbst.set(tree, value, value)

        max = lbst.max(tree)
        assert max == values[len(values) - 1]

        cursor = lbst.cursor(tree)
        lbst.cursor_seek(cursor, max)
        assert lbst.cursor_key(cursor) == values[len(values) - 1]

        for index in range(len(values) - 1, -1):
            lbst.cursor_next(cursor)
            assert lbst.cursor_key(cursor) == values[index]

        assert not lbst.cursor_next(cursor)


def test_delete():
    for _ in range(MAGIC):
        # given
        values = [
            random.randint(-INTEGER_MAX, INTEGER_MAX) for _ in range(TREE_MAX_SIZE)
        ]

        to_delete = values[0]

        values = sorted(set(values))

        tree = lbst.make()
        for value in values:
            tree = lbst.set(tree, value, value)

        # when
        tree = lbst.delete(tree, to_delete)

        # then
        values.remove(to_delete)
        values = {x: x for x in values}

        assert lbst.to_dict(tree) == values
