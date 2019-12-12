"""
Configure truth tests
"""
import pytest


@pytest.fixture(scope='module')
def cost(unit_type):
    return unit_type


@pytest.fixture(scope='module')
def stability(unit_type):
    return unit_type
