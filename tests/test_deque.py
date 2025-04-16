import pytest
from datastructures.deque import Deque

class TestDeque:
    @pytest.fixture
    def empty_deque(self) -> Deque[int]:
        # @name Fixture for an empty deque
        return Deque[int](data_type=int)

    @pytest.fixture
    def populated_deque(self) -> Deque[int]:
        # @name Fixture for a deque pre-populated with integers
        deque = Deque[int](data_type=int)
        for i in range(5):  # Enqueue 0, 1, 2, 3, 4
            deque.enqueue(i)
        return deque

    def test_enqueue(self, empty_deque: Deque[int]) -> None:
        empty_deque.enqueue(10)
        assert len(empty_deque) == 1
        assert empty_deque.back() == 10
        assert empty_deque.front() == 10
        assert empty_deque.empty() is False
        assert 10 in empty_deque

    def test_dequeue(self, populated_deque: Deque[int]) -> None:
        assert populated_deque.dequeue() == 0
        assert len(populated_deque) == 4
        assert populated_deque.front() == 1

    def test_dequeue_empty(self, empty_deque: Deque[int]) -> None:
        with pytest.raises(IndexError):
            empty_deque.dequeue()

    def test_enqueue_front(self, empty_deque: Deque[int]) -> None:
        empty_deque.enqueue_front(10)
        assert len(empty_deque) == 1
        assert empty_deque.front() == 10
        assert empty_deque.back() == 10
        assert empty_deque.empty() is False
        assert 10 in empty_deque

    def test_dequeue_back(self, populated_deque: Deque[int]) -> None:
        assert populated_deque.dequeue_back() == 4
        assert len(populated_deque) == 4
        assert populated_deque.back() == 3

    def test_dequeue_back_empty(self, empty_deque: Deque[int]) -> None:
        with pytest.raises(IndexError):
            empty_deque.dequeue_back()

    def test_front(self, populated_deque: Deque[int]) -> None:
        assert populated_deque.front() == 0

    def test_front_empty(self, empty_deque: Deque[int]) -> None:
        with pytest.raises(IndexError):
            _ = empty_deque.front()

    def test_back(self, populated_deque: Deque[int]) -> None:
        assert populated_deque.back() == 4

    def test_back_empty(self, empty_deque: Deque[int]) -> None:
        with pytest.raises(IndexError):
            _ = empty_deque.back()

    def test_empty_property(self, empty_deque: Deque[int], populated_deque: Deque[int]) -> None:
        assert empty_deque.empty() is True
        assert populated_deque.empty() is False

    def test_len(self, empty_deque: Deque[int], populated_deque: Deque[int]) -> None:
        assert len(empty_deque) == 0
        assert len(populated_deque) == 5

    def test_clear(self, populated_deque: Deque[int]) -> None:
        populated_deque.clear()
        assert len(populated_deque) == 0
        assert populated_deque.empty() is True

    def test_contains(self, populated_deque: Deque[int]) -> None:
        assert 3 in populated_deque
        assert 10 not in populated_deque

    def test_eq(self, populated_deque: Deque[int]) -> None:
        other_deque = Deque[int](data_type=int)
        for i in range(5):  # Enqueue 0, 1, 2, 3, 4
            other_deque.enqueue(i)
        assert populated_deque == other_deque

    def test_neq_different_elements(self, populated_deque: Deque[int]) -> None:
        other_deque = Deque[int](data_type=int)
        for i in range(4):  # Enqueue 0, 1, 2, 3
            other_deque.enqueue(i)
        assert populated_deque != other_deque

    def test_neq_different_sizes(self, populated_deque: Deque[int]) -> None:
        other_deque = Deque[int](data_type=int)
        for i in range(6):  # Enqueue 0, 1, 2, 3, 4, 5
            other_deque.enqueue(i)
        assert populated_deque != other_deque

    def test_eq_non_deque(self, populated_deque: Deque[int]) -> None:
        assert populated_deque != [0, 1, 2, 3, 4]

