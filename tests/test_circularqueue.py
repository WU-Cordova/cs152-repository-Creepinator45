import pytest
from datastructures.circularqueue import CircularQueue

@pytest.fixture
def empty_queue():
    return CircularQueue(maxsize=5, data_type=int)

@pytest.fixture
def small_queue():
    q = CircularQueue(maxsize=5, data_type=int)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    return q

@pytest.fixture
def full_queue():
    q = CircularQueue(maxsize=5, data_type=int)
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    return q

class TestCircularQueue:

    def test_enqueue(self, empty_queue: CircularQueue):
        empty_queue.enqueue(1)
        assert len(empty_queue) == 1
        assert empty_queue.front == 1

    def test_dequeue(self,  small_queue: CircularQueue):
        assert small_queue.dequeue() == 1
        assert len(small_queue) == 2
        assert small_queue.front == 2

    def test_front(self, small_queue: CircularQueue):
        assert small_queue.front == 1

    def test_is_empty(self, empty_queue: CircularQueue, small_queue: CircularQueue):
        assert empty_queue.empty is True
        assert small_queue.empty is False

    def test_is_full(self, full_queue: CircularQueue):
        assert full_queue.full is True

    def test_size(self, empty_queue: CircularQueue, small_queue: CircularQueue, full_queue: CircularQueue):
        assert len(empty_queue) == 0
        assert len(small_queue) == 3
        assert len(full_queue) == 5

    def test_equal_queues(self):
        q1 = CircularQueue(5)
        q2 = CircularQueue(5)
        for i in range(5):
            q1.enqueue(i)
            q2.enqueue(i)
        assert q1 == q2

        q1.dequeue()
        q1.enqueue(5)
        q2.dequeue()
        q2.enqueue(5)
        assert q1 == q2

    def test_equal_queues_with_different_maxsize(self):
        q1 = CircularQueue(maxsize=5, data_type=int)
        q2 = CircularQueue(maxsize=6, data_type=int)
        for i in range(5):
            q1.enqueue(i)
            q2.enqueue(i)
        assert q1 == q2

    def test_equal_queues_with_elements_in_different_positions_but_equal(self):
        q1 = CircularQueue(maxsize=5, data_type=int)
        q2 = CircularQueue(maxsize=5, data_type=int)
        for i in range(5):
            q1.enqueue(i)
            
        for i in range(3):
            q2.enqueue(i)
            
        for i in range(3):
            q2.dequeue()
        
        for i in range(5):
            q2.enqueue(i)

        assert q1 == q2

    def test_not_equal_queues(self):
        q1 = CircularQueue(maxsize=5, data_type=int)
        q2 = CircularQueue(maxsize=5, data_type=int)
        for i in range(5):
            q1.enqueue(i)
            q2.enqueue(i)
        q1.dequeue()
        q1.enqueue(5)
        assert q1 != q2