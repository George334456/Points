import pytest
from calculate_tax import calculate, extended_output

def test_calculate():
    percentages=[.1, .1]
    bracket=[500]
    assert calculate(percentages, bracket, 300) == [30]
    assert calculate(percentages, bracket, 500) == [50]
    assert calculate(percentages, bracket, 600) == [50, 10]

def test_calculate_advanced():
    percentages = [.1, .2, .3]
    bracket = [500, 2000]
    assert calculate(percentages, bracket, 300) == [30]
    assert calculate(percentages, bracket, 1500) == [50, 200]
    assert calculate(percentages, bracket, 5000) == [50, 400, 750]
