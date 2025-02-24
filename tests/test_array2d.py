import pytest

from datastructures.array2d import Array2D

class TestArray2D:
    
    # ✅ Fixtures to create test instances of Array2D
    @pytest.fixture
    def empty3x3(self) -> Array2D[int]:
        """Returns an empty 3x3 Array2D with int type."""
        return Array2D.empty(rows=3, cols=3, data_type=int)
    
    @pytest.fixture
    def filled3x3(self) -> Array2D[int]:
        """Returns a pre-filled 3x3 Array2D with integers."""
        return Array2D([[1, 2, 3], [4, 5, 6], [7, 8, 9]], data_type=int)

    # ✅ Test Initialization of an Empty Array
    def test_init_empty_3x3(self, empty3x3: Array2D[int]) -> None:
        """Checks if an empty 3x3 Array2D is initialized with default values (0)."""
        for row in range(3):
            for col in range(3):
                assert empty3x3[row][col] == 0

    # ✅ Test Initialization of a Filled Array
    def test_init_filled_3x3(self, filled3x3: Array2D[int]) -> None:
        """Checks if a 3x3 Array2D initializes correctly with predefined values."""
        expected_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for row in range(3):
            for col in range(3):
                assert filled3x3[row][col] == expected_values[row][col]

    # ✅ Test Getting and Setting Items
    def test_set_get_item(self, empty3x3: Array2D[int]) -> None:
        """Ensures values can be set and retrieved correctly."""
        empty3x3[1][1] = 42
        assert empty3x3[1][1] == 42

    # ✅ Test Row Iteration
    def test_row_iteration(self, filled3x3: Array2D[int]) -> None:
        """Verifies that rows can be iterated correctly."""
        row_values = [list(row) for row in filled3x3]
        assert row_values == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # ✅ Test Nested Iteration (Full 2D Traversal)
    def test_nested_iteration(self, filled3x3: Array2D[int]) -> None:
        """Checks if nested iteration over the 2D array works correctly."""
        values = []
        for row in filled3x3:
            for item in row:
                values.append(item)
        
        assert values == [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # ✅ Test Out of Bounds Indexing
    def test_out_of_bounds(self, filled3x3: Array2D[int]) -> None:
        """Ensures accessing an index out of bounds raises IndexError."""
        with pytest.raises(IndexError):
            _ = filled3x3[3][0]  # Out of bounds row

        with pytest.raises(IndexError):
            _ = filled3x3[0][3]  # Out of bounds column

    # ✅ Test Length (Row Count)
    def test_len(self, filled3x3: Array2D[int]) -> None:
        """Ensures len(Array2D) returns the correct number of rows."""
        assert len(filled3x3) == 3

    # ✅ Test String Representation
    def test_str_repr(self, filled3x3: Array2D[int]) -> None:
        """Checks if str and repr are formatted correctly."""
        expected_str = "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]"
        assert str(filled3x3) == expected_str
        assert repr(filled3x3).startswith("Array2D 3 Rows x 3 Columns")

    # ✅ Test Reverse Iteration
    def test_reverse_iteration(self, filled3x3: Array2D[int]) -> None:
        """Verifies that reversed(Array2D) correctly reverses row order."""
        reversed_rows = list(reversed(filled3x3))
        expected = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        assert [list(row) for row in reversed_rows] == expected

    # ✅ Test for ValueError if `starting_sequence` is not a sequence
    def test_init_not_sequence(self) -> None:
        """Ensures a ValueError is raised if the input is not a sequence."""
        with pytest.raises(ValueError, match="must be a sequence of sequences"):
            _ = Array2D(123, data_type=int)  # Not a list of lists

        with pytest.raises(ValueError, match="must be a sequence of sequences"):
            _ = Array2D("invalid_string", data_type=int)  # Not a sequence of sequences

        with pytest.raises(ValueError, match="must be a sequence of sequences"):
            _ = Array2D({1: [1, 2, 3]}, data_type=int)  # Dictionary is not a valid sequence

    # ✅ Test for ValueError if `starting_sequence` contains mixed types
    def test_init_mixed_types(self) -> None:
        """Ensures a ValueError is raised if items in `starting_sequence` are of mixed types."""
        with pytest.raises(ValueError, match="All items must be of the same type"):
            _ = Array2D([[1, 2, "three"], [4, 5, 6]], data_type=int)  # Mixed types

        with pytest.raises(ValueError, match="All items must be of the same type"):
            _ = Array2D([[1.0, 2.0, 3], [4, "five", 6]], data_type=float)  # Mixed types

        with pytest.raises(ValueError, match="All items must be of the same type"):
            _ = Array2D([[1, 2, 3], ["four", "five", "six"]], data_type=str)  # Mixed row types

    # ✅ Test for ValueError if `starting_sequence` has inconsistent lengths
    def test_init_inconsistent_lengths(self) -> None:
        """Ensures a ValueError is raised if rows in `starting_sequence` have different lengths."""
        with pytest.raises(ValueError, match="must be a sequence of sequences with the same length"):
            _ = Array2D([[1, 2, 3], [4, 5]], data_type=int)