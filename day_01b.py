def get_number_of_observations(my_list: list, observation) -> int:
    result = my_list.count(observation)
    return result


def get_similarity_score(list_a: list[int], list_b: list[int]) -> int:
    result: int = 0
    for value in list_a:
        result += value * get_number_of_observations(list_b, value)
    return result
