"""
Configure truth tests
"""
import pytest


@pytest.fixture(scope='module')
def cost():
    def _cost(argument):
        return argument
    yield _cost


@pytest.fixture(scope='module')
def stability_margin():
    def _stability_margin(argument):
        return argument
    return _stability_margin
