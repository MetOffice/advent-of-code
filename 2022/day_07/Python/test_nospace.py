from nospace import TreeBuilder
import pytest

tree = TreeBuilder.build("../test_input.txt")

@pytest.mark.parametrize('filename, size', [('e', 584),
                                            ('a', 94853),
                                            ('d', 24933642),
                                            ('/', 48381165)])
def test_size(filename, size):
    this = tree.get_child(filename)

    assert this.size() == size
