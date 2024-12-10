import logging
import os

import day_01
import day_01b
import day_02

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    print("Hello from adventofcode-2024!")

    list_a, list_b = day_01.parse_text_2_lists(
        os.path.join(os.getcwd(), "day_01_input.txt")
    )
    result_day01 = day_01.calc_list_difference(list_a=list_a, list_b=list_b)
    print(f"Result day 01: {result_day01}")

    result_day01b = day_01b.get_similarity_score(list_a=list_a, list_b=list_b)
    print(f"Result day 01b: {result_day01b}")

    safe_reports = day_02.calc_safe_reports(
        os.path.join(os.getcwd(), r"day_02\data.txt")
    )
    print(f"Result day 02: {safe_reports=}")

    safe_reports_tolerate_1 = day_02.calc_safe_reports_tolerate_1(
        os.path.join(os.getcwd(), r"day_02\data.txt")
    )
    print(f"Result day 02b: {safe_reports_tolerate_1=}")  # not 398, which is too low


if __name__ == "__main__":
    main()
