import day_01
import day_01b


class Test_day_01b:
    def test_differences_individual(self):
        data = """
3   4
4   3
2   5
1   3
3   9
3   3"""

        list_a, list_b = day_01.parse_text_2_lists(data)

        # For these example lists, here is the process of finding the similarity score:

        # The first number in the left list is 3. It appears in the right list three times, so the similarity score increases by 3 * 3 = 9.
        count = day_01b.get_number_of_observations(list_b, list_a[0])
        assert count == 3

        # The second number in the left list is 4. It appears in the right list once, so the similarity score increases by 4 * 1 = 4.
        # The third number in the left list is 2. It does not appear in the right list, so the similarity score does not increase (2 * 0 = 0).
        # The fourth number, 1, also does not appear in the right list.
        # The fifth number, 3, appears in the right list three times; the similarity score increases by 9.
        # The last number, 3, appears in the right list three times; the similarity score again increases by 9.
        # So, for these example lists, the similarity score at the end of this process is 31 (9 + 4 + 0 + 0 + 9 + 9).

        assert day_01b.get_similarity_score(list_a=list_a, list_b=list_b) == 31
