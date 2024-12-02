import os


def read_data(filename: str) -> list[list[int]]:
    if not os.path.exists(filename):
        raise FileNotFoundError(filename)

    result: list[list[int]] = []
    with open(filename, "r") as f:
        for line in f:
            str_values = line.split(sep=" ")
            int_values: list[int] = [int(x) for x in str_values]
            result.append(int_values)

    return result


def get_differences(input: list[int]) -> list[int]:
    differences: list[int] = []
    for i in range(1, len(input)):
        difference = input[i] - input[i - 1]
        differences.append(difference)
    return differences


def sign(a: float | int | None) -> int:
    if a is None:
        return 0
    return bool(a > 0) - bool(a < 0)


def is_safe(differences: list[int]) -> bool:
    min_value = min(differences)
    max_value = max(differences)
    result = (
        sign(min_value) == sign(max_value)
        and abs(min_value) in [1, 2, 3]
        and abs(max_value) in [1, 2, 3]
    )
    return result


def calc_safe_reports(filename: str) -> int:
    data = read_data(filename=filename)
    result = 0
    for line in data:
        safe = is_safe(get_differences(line))
        if safe:
            result += 1
    return result
