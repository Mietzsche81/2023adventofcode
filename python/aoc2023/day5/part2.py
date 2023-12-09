import itertools as it
from typing import Dict, List, Tuple


def pairwise(iterable):
    a, b = it.tee(iterable)
    next(b, None)
    return zip(a, b)


def main(
    seeds: List[int],
    maps: Dict[Tuple[str, str], Dict[str, List[int]]],
):
    input_type = "seed"
    output_type = "location"

    """
    # Reorder maps by lowest destination
    for key, data in maps.items():
        order = np.argsort(data["dest_range_start"])
        for subkey, value in data.items():
            maps[key][subkey] = [value[i] for i in order]
    """

    # Create data lineage
    map_keys = [input_type]
    while map_keys[-1] != output_type:
        map_keys.append(next((y for (x, y) in maps if x == map_keys[-1])))

    # Create seed ranges
    seed_ranges = [(i, i + n) for i, n in zip(seeds[::2], seeds[1::2])]

    # Find min location for each seed range
    min_locations = []
    for seed_range in seed_ranges:
        forks = [seed_range]
        # For each layer of the map
        for map_key in pairwise(map_keys):
            map = maps[map_key]
            # For each possible range of sources
            dest_forks = []
            for input_start, input_end in forks:
                # For each mapped possible range of destinations
                for j in range(len(map["source_range_start"])):
                    source_start = map["source_range_start"][j]
                    range_length = map["range_length"][j]
                    source_end = source_start + range_length
                    dest_start = map["dest_range_start"][j]
                    map_delta = dest_start - source_start
                    # No new mapping if not overlapping
                    if input_end < source_start:
                        # dest_forks += [(input_start, input_end)]
                        continue
                    elif input_start >= source_end:
                        # dest_forks += [(input_start, input_end)]
                        continue
                    # At least some overlap...
                    else:
                        match (input_start < source_start, input_end > source_end):
                            # Input complete contained by transformation
                            case (False, False):
                                dest_forks += [
                                    (
                                        input_start + map_delta,
                                        input_end + map_delta,
                                    )
                                ]
                            # Input completely contains transformation
                            case (True, True):
                                dest_forks += [
                                    (input_start, source_start),
                                    (source_start + map_delta, source_end + map_delta),
                                    (source_end, input_end),
                                ]
                            # Start is outside
                            case (True, False):
                                dest_forks += [
                                    (input_start, source_start),
                                    (source_start + map_delta, input_end + map_delta),
                                ]
                            # End is outside
                            case (False, True):
                                dest_forks += [
                                    (input_start + map_delta, source_end + map_delta),
                                    (source_end, input_end),
                                ]
            dest_forks.sort()
            if dest_forks:
                forks = dest_forks
            # input()
        min_locations.append(min(forks)[0])

    return min(min_locations)
