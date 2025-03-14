import copy
import pytest
from datastructures.array import Array

from tests.car import Car, Color, Make, Model

class TestArray:
    car1 = Car('123', Color.RED, Make.TOYOTA, Model.CAMRY)
    car2 = Car('456', Color.BLUE, Make.TOYOTA, Model.CIVIC)
    car3 = Car('789', Color.BLACK, Make.FORD, Model.FUSION)

    @pytest.fixture
    def setup_complex_object_array(self) -> Array[Car]:
        return Array[Car](starting_sequence=[self.car1, self.car2, self.car3], data_type=Car)

    @pytest.fixture
    def setup_numerical_array(self) -> Array[int]:
        return Array[int](starting_sequence=[i for i in range(10)], data_type=int)

    def test_constructing_an_array_with_a_complex_object_should_deep_copy_the_complex_objects_data(self, setup_complex_object_array: Array[Car]):
        original_array = setup_complex_object_array
        
        deep_copied_array = copy.deepcopy(original_array)
        deep_copied_array[0].vin = '000'

        assert original_array[0] is not deep_copied_array[0]
    
    def test_constructing_an_array_with_a_numerical_type_should_copy_the_numerical_data(self, setup_numerical_array: Array):
        array = copy.copy(setup_numerical_array)
        for i in range(len(array)):
            assert array[i] == setup_numerical_array[i]


    def test_index_operator_should_return_the_item_at_the_index_specified_of_the_array(self, setup_numerical_array: Array):
        assert setup_numerical_array[5] == 5
    
    def test_index_operator_should_raise_an_IndexError_exception_if_the_index_is_out_of_bounds(self, setup_numerical_array: Array):
        with pytest.raises(IndexError):
            setup_numerical_array[-11]
    
    def adding_an_item_to_a_full_array_should_raise_an_index_error_exception(self, setup_numerical_array: Array):
        with pytest.raises(IndexError):
            setup_numerical_array[10]

    def test_equality_operator_should_return_true_for_valid_instances_containing_the_same_data(self, setup_numerical_array: Array):
        array1 = setup_numerical_array
        array2 = setup_numerical_array

        assert array1 == array2

    def test_non_equality_operator_should_return_true_for_valid_instances_containing_the_same_data(self, setup_numerical_array: Array, setup_complex_object_array: Array):
        array1 = setup_numerical_array
        array2 = setup_complex_object_array

        assert array1 != array2

    def test_equality_operator_should_return_false_for_comparison_of_a_array_to_another_object_type(self, setup_numerical_array: Array):
        assert setup_numerical_array != 'string instance'

    def test_contains_operator_should_return_true_if_the_item_being_checked_is_in_the_array(self, setup_numerical_array: Array):
        assert 1 in setup_numerical_array

    def test_contains_operator_should_return_false_if_the_item_being_checked_is_not_in_the_array(self, setup_numerical_array: Array):
        assert 11 not in setup_numerical_array
    
    def test_to_string_operator_should_return_a_string_representation_of_the_array(self, setup_numerical_array: Array):
        assert str(setup_numerical_array) is not None
    
    def test_representation_operator_should_return_a_string_representation_of_the_array(self, setup_numerical_array: Array):
        assert repr(setup_numerical_array) is not None
    
    def test_clear_operator_should_clear_the_array(self, setup_numerical_array: Array):
        setup_numerical_array.clear()
        for item in setup_numerical_array:
            assert item is None

    def test_clear_operator_should_reset_the_array_to_default_size_and_values(self, setup_numerical_array: Array):
        setup_numerical_array.clear()
        assert len(setup_numerical_array) == 0
    
    def test_clear_operator_should_reset_the_array_to_the_specified_default_value(self, setup_numerical_array: Array):
        setup_numerical_array.clear()
        assert len(setup_numerical_array) == 0

    def test_del_operator_should_remove_item_in_position_and_copy_the_array_contents_from_index_plus_1_down_to_fill_the_gap_caused_by_deleting_the_item(self, setup_numerical_array: Array):
        del setup_numerical_array[0]
        assert setup_numerical_array[0] == 1

    def test_reversed_operator_should_return_true(self, setup_numerical_array: Array):
        expected = 9
        for item in reversed(setup_numerical_array):
            assert expected == item
            expected -= 1
    
    def test_iterator_operator_should_return_the_item_at_index_during_iteration(self, setup_numerical_array: Array):
        expected = 0
        for item in setup_numerical_array:
            assert expected == item
            expected += 1

    def test_length_operator_should_return_the_length_of_the_array(self, setup_numerical_array: Array):
        assert len(setup_numerical_array) == 10

    def test_length_operator_should_return_the_length_of_the_array_plus_1_after_appending_an_item(self, setup_numerical_array: Array):
        setup_numerical_array.append(10)
        print(repr(setup_numerical_array))
        assert len(setup_numerical_array) == 11

    def test_reverse_operator_should_reverse_the_array(self, setup_numerical_array: Array):
        expected = 9
        for item in reversed(setup_numerical_array):
            assert expected == item
            expected -= 1

    def test_setitem_operator_should_raise_a_type_error_exception_if_the_item_being_set_is_not_the_same_type_as_the_array(self, setup_numerical_array: Array):
        with pytest.raises(TypeError):
            setup_numerical_array[0] = 'string'

    def test_bracket_operator_should_return_a_slice_of_the_array_if_a_slice_is_passed_in(self, setup_numerical_array: Array):
        assert setup_numerical_array[1:5] == Array([1, 2, 3, 4])

    def test_constructor_should_raise_a_value_error_if_the_sequence_passed_in_is_not_a_sequence(self):
        with pytest.raises(ValueError):
            Array(1) #type: ignore

    def test_constructor_should_raise_a_type_error_if_the_sequence_passed_in_is_not_the_same_type_as_the_array(self):
        with pytest.raises(TypeError):
            Array(['string'], int) #type: ignore
    
    def test_bracket_operator_should_raise_a_type_error_if_the_index_is_not_an_integer_or_slice(self, setup_numerical_array: Array):
        with pytest.raises(TypeError):
            setup_numerical_array['string'] #type: ignore
