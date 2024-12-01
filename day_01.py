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
