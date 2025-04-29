import pytest

from datastructures.arraystack import ArrayStack


@pytest.fixture
def stack() -> ArrayStack:
    return ArrayStack(max_size=5, data_type=int)

class TestArrayStack:
    def test_push(self, stack: ArrayStack) -> None:
        stack.push(1)
        assert len(stack) == 1
        assert stack.peek == 1

    def test_pop(self, stack: ArrayStack) -> None:
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert len(stack) == 1
        assert stack.pop() == 1
        assert stack.empty

    def test_peek(self, stack: ArrayStack) -> None:
        stack.push(1)
        stack.push(2)
        assert stack.peek == 2
        stack.pop()
        assert stack.peek == 1

    def test_clear(self, stack: ArrayStack) -> None:
        stack.push(1)
        stack.push(2)
        stack.clear()
        assert stack.empty

    def test_full(self, stack: ArrayStack) -> None:
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        assert stack.full
        with pytest.raises(IndexError):
            stack.push(6)

    def test_empty(self, stack: ArrayStack) -> None:
        assert stack.empty
        with pytest.raises(IndexError):
            stack.pop()

    def test_eq(self, stack: ArrayStack) -> None:
        stack1 = ArrayStack(max_size=5, data_type=int)
        stack2 = ArrayStack(max_size=5, data_type=int)
        stack1.push(1)
        stack1.push(2)
        stack2.push(1)
        stack2.push(2)
        assert stack1 == stack2

    def test_not_eq_different_elements(self, stack: ArrayStack) -> None:
        stack1 = ArrayStack(max_size=5, data_type=int)
        stack2 = ArrayStack(max_size=5, data_type=int)
        stack1.push(1)
        stack1.push(2)
        stack2.push(2)
        stack2.push(1)
        assert stack1 != stack2

    def test_not_eq_different_sizes(self, stack: ArrayStack) -> None:
        stack1 = ArrayStack(max_size=5, data_type=int)
        stack2 = ArrayStack(max_size=5, data_type=int)
        stack1.push(1)
        stack2.push(1)
        stack2.push(2)
        assert stack1 != stack2

    def test_contains(self, stack: ArrayStack) -> None:
        stack.push(1)
        stack.push(2)
        assert 1 in stack
        assert 3 not in stack

    def test_str(self, stack: ArrayStack) -> None:
        stack.push(1)
        stack.push(2)
        assert str(stack) == '[1, 2]'

    def test_repr(self, stack: ArrayStack) -> None:
        stack.push(1)
        stack.push(2)
