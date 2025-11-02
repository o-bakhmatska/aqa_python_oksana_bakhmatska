
import pytest
from lesson_12.homework12 import divide, Student, ArrayTransformer

@pytest.mark.divide_test
class TestDivide:

    # def test_divide_valid(self):
    #     assert divide(10, 2) == 5
    #     assert divide(-6, 3) == -2
    #     assert divide(7.5, 2.5) == 3.0
    @pytest.mark.smoke
    @pytest.mark.parametrize('first_value,second_value,expected_result',
                             [
                                 (10, 2, 5),
                                 (-6, 3, -2),
                                 (7.6, 2.5, 3.04),
                             ]
                             )
    def test_divide_valid(self, first_value, second_value, expected_result):
        assert divide(first_value, second_value) == expected_result

    def test_divide_zero(self):
        with pytest.raises(ValueError, match="Division by zero is impossible!"):
            divide(10, 0)

    def test_divide_invalid_types(self):
        with pytest.raises(TypeError, match="Both arguments must be numbers!"):
            divide("10", 5)
        with pytest.raises(TypeError):
            divide(10, None)
        with pytest.raises(TypeError):
            divide([], 2)

    @pytest.mark.parametrize('first_value,second_value,expected_result',
                             [
                                 (0, 5, 0),
                                 (5, -1, -5)
                             ]
                             )
    def test_divide_edge_cases(self, first_value, second_value, expected_result):
        assert divide(first_value, second_value) == expected_result
    # def test_divide_edge_cases(self):
    #     assert divide(0, 5) == 0
    #     assert divide(5, -1) == -5

@pytest.mark.student_test
class TestStudent:
    @pytest.mark.smoke
    def test_student_creation(self):
        student = Student("Alex", "Forbes", 20, 88.5)
        assert student.name == "Alex"
        assert student.surname == "Forbes"
        assert student.age == 20
        assert student.average_grade == 88.5

    @pytest.mark.smoke
    def test_change_average_grade(self):
        student = Student("Alex", "Forbes", 20, 88.5)
        student.change_average_grade(92.0)
        assert student.average_grade == 92.0

    def test_display_info(self, capsys):
        student = Student("Alex", "Forbes", 20, 88.5)
        student.display_info()

        captured = capsys.readouterr()
        assert "First name: Alex" in captured.out
        assert "Last name: Forbes" in captured.out
        assert "Age: 20" in captured.out
        assert "Average_grade: 88.5" in captured.out

    def test_change_average_grade_output(self, capsys):
        student = Student("Alex", "Forbes", 20, 88.5)
        student.change_average_grade(95)
        captured = capsys.readouterr()
        assert "Average grade was changed to: 95" in captured.out

@pytest.mark.array_transformer
class TestArrayTransformer:

    @pytest.mark.smoke
    @pytest.mark.parametrize('first_value,, expected_result',
                                 [
                                     ("1,2,3", 6),
                                     ("10,20,30", 60),
                                     ("0,0,0", 0),
                                     ("1,2,a", "Не можу це зробити!"),
                                     ("qwerty", "Не можу це зробити!"),
                                     (" ", "Не можу це зробити!")
                                 ]
                                 )
    def test_divide_edge_cases(self, first_value, expected_result):
        assert ArrayTransformer.sum_of_numbers(first_value) == expected_result
    # def test_sum_of_numbers_valid(self):
    #     assert ArrayTransformer.sum_of_numbers("1,2,3") == 6
    #     assert ArrayTransformer.sum_of_numbers("10,20,30") == 60
    #     assert ArrayTransformer.sum_of_numbers("0,0,0") == 0

    # def test_divide_edge_cases(self, first_value, expected_result):
    #     assert ArrayTransformer.sum_of_numbers(first_value) == expected_result
    # def test_sum_of_numbers_invalid(self):
    #     assert ArrayTransformer.sum_of_numbers("1,2,a") == "Не можу це зробити!"
    #     assert ArrayTransformer.sum_of_numbers("qwerty") == "Не можу це зробити!"
    #     assert ArrayTransformer.sum_of_numbers("") == "Не можу це зробити!"

    @pytest.mark.smoke
    def test_transform_all_mixed(self):
        some_array = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3", "1,2,3,4,100"]
        process = ArrayTransformer(some_array)
        assert process.transform_all() == [10, 60, "Не можу це зробити!", 110]

    def test_transform_all_empty_string(self):
        some_array = ["", "1,2,3"]
        process = ArrayTransformer(some_array)
        assert process.transform_all() == ["Не можу це зробити!", 6]

    def test_transform_all_all_invalid(self):
        some_array = ["a,b,c", "x,y,z"]
        process = ArrayTransformer(some_array)
        assert process.transform_all() == ["Не можу це зробити!", "Не можу це зробити!"]