from utils import get_input


def format_data(data: str) -> tuple[list[int], list[int]]:
    """ Sort location IDs list. """
    location_ids_l1 = []
    location_ids_l2 = []
    for numbers in data.split("\n"):
        nb_l1, nb_l2 = numbers.split("  ")
        location_ids_l1.append(int(nb_l1))
        location_ids_l2.append(int(nb_l2))
    location_ids_l1.sort()
    location_ids_l2.sort()
    return location_ids_l1, location_ids_l2


# Part 1

def part_1() -> None:
    """ Part 1. """
    data = get_input()

    location_ids_l1, location_ids_l2 = format_data(data)

    total_distance = 0
    for location_id_l1, location_id_l2 in zip(location_ids_l1, location_ids_l2):
        total_distance += abs(location_id_l1 - location_id_l2)

    print(total_distance)


# Part 2

def part_2() -> None:
    """ Part 2. """
    data = get_input()

    location_ids_l1, location_ids_l2 = format_data(data)
    # No real need to do that here.
    score_by_value: dict[int, int] = {}
    """ To not have to recompute score each time. """

    def get_score_for_location_id(location_id) -> int:
        """ Get score for a given location ID. Can be cached or newly computed. """
        if score_by_value.get(location_id) is None:
            score_by_value[location_id] = location_id * location_ids_l2.count(location_id)
        return score_by_value[location_id]

    score = 0
    for location_id in location_ids_l1:
        score += get_score_for_location_id(location_id)

    print(score)


if __name__ == "__main__":
    # part_1()
    part_2()
