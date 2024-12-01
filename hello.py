import day_01


def main():
    print("Hello from adventofcode-2024!")

    list_a, list_b = day_01.parse_text_2_lists(day_01.input)
    result_day01 = day_01.calc_list_difference(list_a=list_a, list_b=list_b)
    print(f"Result day 01: {result_day01}")


if __name__ == "__main__":
    main()
