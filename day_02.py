import logging
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


def get_differences(values: list[int]) -> list[int]:
    differences: list[int] = []
    for i in range(1, len(values)):
        difference = values[i] - values[i - 1]
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


def is_safe_tolerate_1(values: list[int]) -> tuple[bool, int]:
    differences = get_differences(values)
    if is_safe(differences):
        logging.debug(f"{values=} - safe without removing")
        return True, -1

    for i in reversed(range(0, len(values) - 1)):
        values_minus_i = values.copy()
        values_minus_i.pop(i)
        differences = get_differences(values_minus_i)
        if is_safe(differences):
            logging.debug(f"{values=} - safe after removing pos {i}")
            return True, i

    logging.debug(f"{values=} - unsafe")
    return False, -100


def calc_safe_reports_tolerate_1(filename: str) -> int:
    data = read_data(filename=filename)
    result = 0
    for line in data:
        safe = is_safe_tolerate_1(line)[0]
        if safe:
            result += 1
    return result
