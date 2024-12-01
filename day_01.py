import io

import polars as pl


def calc_differences(sorted_list_a: list[int], sorted_list_b: list[int]) -> list[int]:
    zipped_list = zip(sorted_list_a, sorted_list_b)
    result_list: list[int] = []
    for pairs in zipped_list:
        result = abs(pairs[0] - pairs[1])
        result_list.append(result)
    return result_list


def calc_list_difference(list_a: list[int], list_b: list[int]) -> int:
    if len(list_a) != len(list_b):
        raise ValueError(f"Differences in length: {len(list_a)=}, {len(list_b)=}")
    list_a.sort()
    list_b.sort()

    result_list = calc_differences(sorted_list_a=list_a, sorted_list_b=list_b)

    result = sum(result_list)
    return result


def parse_text_2_lists(filename: str | io.StringIO) -> tuple[list[int], list[int]]:
    text = ""
    if isinstance(filename, str):
        with open(filename, "r") as file:
            # Read the entire file content into a string
            text = file.read()
    elif isinstance(filename, io.StringIO):
        text = filename.getvalue()
    else:
        raise ValueError(filename)

    text_one_space = text.replace("  ", " ")
    text_one_space = text_one_space.replace("  ", " ")

    file = io.StringIO(text_one_space)
    df = pl.read_csv(
        file, has_header=False, new_columns=["list_a", "list_b"], separator=" "
    )
    list_a = pl.Series(df.select("list_a")).to_list()
    list_b = pl.Series(df.select("list_b")).to_list()
    return (list_a, list_b)
