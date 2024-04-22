import pytest
import tree
def test_tree_find1():
    my_tree = tree.Tree()
    my_tree.add(5)
    my_tree.add(10)
    assert my_tree.find(5) is not None

def test_tree_find2():
    my_tree = tree.Tree()
    assert my_tree.find(10) is None
