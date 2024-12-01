import day_01


class Test_day_01:
    def test_differences_individual(self):
        list_a = [3, 4, 2, 1, 3, 3]
        list_b = [4, 3, 5, 3, 9, 3]

        list_a.sort()
        list_b.sort()
        differences_list = day_01.calc_differences(
            sorted_list_a=list_a, sorted_list_b=list_b
        )

        # The smallest number in the left list is 1, and the smallest number in the right list is 3.
        assert list_a[0] == 1
        assert list_b[0] == 3
        # The distance between them is 2.
        assert differences_list[0] == 2

        # The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3.
        assert list_a[1] == 2
        assert list_b[1] == 3
        # The distance between them is 1.
        assert differences_list[1] == 1

        # The third-smallest number in both lists is 3, so the distance between them is 0.
        assert list_a[2] == 3
        assert list_b[2] == 3
        assert differences_list[2] == 0

        # The next numbers to pair up are 3 and 4, a distance of 1.
        assert list_a[3] == 3
        assert list_b[3] == 4
        assert differences_list[3] == 1

        # The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
        assert list_a[4] == 3
        assert list_b[4] == 5
        assert differences_list[4] == 2

        # Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
        assert list_a[5] == 4
        assert list_b[5] == 9
        assert differences_list[5] == 5

    def test_differences_sum(self):
        list_a = [3, 4, 2, 1, 3, 3]
        list_b = [4, 3, 5, 3, 9, 3]

        result = day_01.calc_list_difference(list_a, list_b)
        assert result == 11

    def test_parse2lists(self):
        input = """
3   4
4   3
2   5
1   3
3   9
3   3"""
        (actual_a, actual_b) = day_01.parse_text_2_lists(input)
        list_a = [3, 4, 2, 1, 3, 3]
        list_b = [4, 3, 5, 3, 9, 3]
        assert actual_a == list_a
        assert actual_b == list_b
