import pytest
from datastructures.liststack import ListStack

class TestListStack:

    @pytest.fixture
    def empty_stack(self) -> ListStack[int]:
        return ListStack[int](data_type=int)

    @pytest.fixture
    def populated_stack(self) -> ListStack[int]:
        stack = ListStack[int](data_type=int)
        for i in range(5):  # Push 0, 1, 2, 3, 4 onto the stack
            stack.push(i)
        return stack

    def test_push(self, empty_stack: ListStack[int]) -> None:
        empty_stack.push(10)
        assert len(empty_stack) == 1
        assert empty_stack.peek() == 10

    def test_pop(self, populated_stack: ListStack[int]) -> None:
        assert populated_stack.pop() == 4
        assert len(populated_stack) == 4
        assert populated_stack.pop() == 3

    def test_pop_empty_stack(self, empty_stack: ListStack[int]) -> None:
        with pytest.raises(IndexError):
            empty_stack.pop()

    def test_peek(self, populated_stack: ListStack[int]) -> None:
        assert populated_stack.peek() == 4
        assert len(populated_stack) == 5

    def test_peek_empty_stack(self, empty_stack: ListStack[int]) -> None:
        with pytest.raises(IndexError):
            empty_stack.peek()

    def test_empty_property(self, empty_stack: ListStack[int], populated_stack: ListStack[int]) -> None:
        assert empty_stack.empty is True
        assert populated_stack.empty is False

    def test_clear(self, populated_stack: ListStack[int]) -> None:
        populated_stack.clear()
        assert len(populated_stack) == 0
        assert populated_stack.empty is True

    def test_contains(self, populated_stack: ListStack[int]) -> None:
        assert 3 in populated_stack
        assert 10 not in populated_stack

    def test_eq(self, populated_stack: ListStack[int]) -> None:
        other_stack = ListStack[int](data_type=int)
        for i in range(5):
            other_stack.push(i)
        assert populated_stack == other_stack
        other_stack.push(10)
        assert populated_stack != other_stack

    def test_len(self, empty_stack: ListStack[int], populated_stack: ListStack[int]) -> None:
        assert len(empty_stack) == 0
        assert len(populated_stack) == 5

