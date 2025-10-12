import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_multiple_streaks_longest_in_middle():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_zeros_and_negatives():
    assert longest_positive_streak([-1, 0, -5, 0, -10]) == 0

def test_all_positive():
    assert longest_positive_streak([1, 1, 1, 1, 1]) == 5

def test_streak_at_the_beginning():
    assert longest_positive_streak([4, 5, 0, 1, 2]) == 2

def test_streak_at_the_end():
    assert longest_positive_streak([1, 2, 0, 4, 5, 6]) == 3
