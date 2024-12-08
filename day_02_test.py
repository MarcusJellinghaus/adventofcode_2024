import os, logging

import day_02




class Test_Day_02:
    def setUpClass(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def test_read_data(self):
        filename = os.path.join(os.getcwd(), r"day_02\testdata.txt")
        data = day_02.read_data(filename=filename)
        assert len(data) == 6
        assert data[0] == [7, 6, 4, 2, 1]

    def test_get_differences(self):
        test_data = [1, 2, 4, 8, -8]
        differences = day_02.get_differences(test_data)
        assert differences == [1, 2, 4, -16]

    def test_sign(self):
        assert day_02.sign(-3) == -1
        assert day_02.sign(3) == 1
        assert day_02.sign(0) == 0
        assert day_02.sign(None) == 0

    def test_is_safe(self):
        assert day_02.is_safe(day_02.get_differences([7, 6, 4, 2, 1])) is True
        assert day_02.is_safe(day_02.get_differences([1, 2, 7, 8, 9])) is False
        assert day_02.is_safe(day_02.get_differences([9, 7, 6, 2, 1])) is False
        assert day_02.is_safe(day_02.get_differences([1, 3, 2, 4, 5])) is False
        assert day_02.is_safe(day_02.get_differences([8, 6, 4, 4, 1])) is False
        assert day_02.is_safe(day_02.get_differences([1, 3, 6, 7, 9])) is True

    def test_calc_safe_reports(self):
        filename = os.path.join(os.getcwd(), r"day_02\testdata.txt")
        assert day_02.calc_safe_reports(filename=filename) == 2    

    def test_is_safe_tolerate_1(self):
        assert day_02.is_safe_tolerate_1([7, 6, 4, 2, 1])  == (True, -1)
        assert day_02.is_safe_tolerate_1([1, 2, 7, 8, 9]) == (False, -100)
        assert day_02.is_safe_tolerate_1([9, 7, 6, 2, 1]) == (False, -100)

        result_4 = day_02.is_safe_tolerate_1([1, 3, 2, 4, 5])
        assert result_4 == (True, 2)

        result_5 = day_02.is_safe_tolerate_1([8, 6, 4, 4, 1])
        assert result_5 == (True, 3)

        assert day_02.is_safe_tolerate_1([1, 3, 6, 7, 9]) == (True, -1)

    def test_calc_safe_reports_tolerate_1(self):
        filename = os.path.join(os.getcwd(), r"day_02\testdata.txt")
        assert day_02.calc_safe_reports_tolerate_1(filename=filename) == 4