import pytest
from bananas import BananaStore

# Add max bananas test

@pytest.fixture()
def setup():
    bananas = 20
    test_bananastore = BananaStore(bananas)
    return test_bananastore, bananas


def test_bananastore_add_negative_number(setup):

    test_bananastore, bananas = setup
    with pytest.raises(ValueError):
        test_bananastore.add(-5)


def test_bananastore_add_positive_number(setup):

    test_bananastore, bananas = setup
    test_bananastore.add(5)
    assert test_bananastore.bananas == bananas + 5


def test_bananastore_remove_negative_number(setup):

    test_bananastore, bananas = setup
    with pytest.raises(ValueError):
        test_bananastore.remove(-5)


def test_bananastore_remove_positive_number(setup):

    test_bananastore, bananas = setup
    test_bananastore.remove(5)
    assert test_bananastore.bananas == bananas - 5


def test_bananastore_remove_too_many_bananas(setup):

    test_bananastore, bananas = setup
    with pytest.raises(ValueError):
        test_bananastore.remove(bananas + 1)
