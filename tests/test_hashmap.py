from datastructures.hashmap import HashMap
import pytest

class TestHashMap:

    @pytest.fixture
    def empty_hashmap(self) -> HashMap[int, str]:
        return HashMap[int, str]()

    @pytest.fixture
    def populated_hashmap(self) -> HashMap[int, str]:
        hashmap = HashMap[int, str]()
        for i in range(10):
            hashmap[i] = str(i)
        return hashmap

    def test_set_and_get_item(self, empty_hashmap: HashMap[int, str]):
        empty_hashmap[1] = "one"
        assert empty_hashmap[1] == "one"

    def test_get_nonexistent_key(self, empty_hashmap: HashMap[int, str]):
        with pytest.raises(KeyError):
            _ = empty_hashmap[99]

    def test_update_existing_key(self, populated_hashmap: HashMap[int, str]):
        populated_hashmap[5] = "updated"
        assert populated_hashmap[5] == "updated"

    def test_delete_item(self, populated_hashmap: HashMap[int, str]):
        del populated_hashmap[5]
        assert 5 not in populated_hashmap

    def test_delete_nonexistent_key(self, empty_hashmap: HashMap[int, str]):
        with pytest.raises(KeyError):
            del empty_hashmap[99]

    def test_contains_key(self, populated_hashmap: HashMap[int, str]):
        assert 5 in populated_hashmap
        assert 99 not in populated_hashmap

    def test_len(self, populated_hashmap: HashMap[int, str], empty_hashmap: HashMap[int, str]):
        assert len(populated_hashmap) == 10
        assert len(empty_hashmap) == 0

    def test_iteration(self, populated_hashmap: HashMap[int, str]):
        keys = list(sorted(iter(populated_hashmap)))
        assert keys == list(range(10))

    def test_resize(self, empty_hashmap: HashMap[int, str]):
        for i in range(20):
            empty_hashmap[i] = str(i)
        assert len(empty_hashmap) == 20
        for i in range(20):
            assert empty_hashmap[i] == str(i)
