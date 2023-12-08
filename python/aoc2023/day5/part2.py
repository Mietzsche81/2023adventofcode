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
    # Set objectives, create data lineage
    input_type = "seed"
    output_type = "location"
    map_keys = [input_type]
    while map_keys[-1] != output_type:
        map_keys.append(next((y for (x, y) in maps if x == map_keys[-1])))

    # Create seed ranges from seeds input
    seed_ranges = [(i, i + n) for i, n in zip(seeds[::2], seeds[1::2])]

    # Find min location for each seed range
    min_locations = []
    for seed_range in seed_ranges:
        source_forks = [seed_range]
        # For each layer of the data lineage's source -> destination mapping
        for map_key in pairwise(map_keys):
            print(map_key, "---", source_forks)
            map = maps[map_key]
            # For each 'fork' of ranges in the source space
            dest_forks = []
            for input_start, input_end in source_forks:
                # For each possible mapping range of destinations applied to said source fork
                for j in range(len(map["source_range_start"])):
                    source_start = map["source_range_start"][j]
                    range_length = map["range_length"][j]
                    source_end = source_start + range_length
                    dest_start = map["dest_range_start"][j]
                    map_delta = dest_start - source_start
                    # No new mapping if not overlapping
                    if input_end < source_start:
                        continue
                    elif input_start >= source_end:
                        continue
                    # But if there's at least some overlap...
                    else:
                        match (input_start < source_start, input_end > source_end):
                            # Input completely contained by transformation
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
                source_forks = dest_forks
            input()
        min_locations.append(min(source_forks)[0])

    return min(min_locations)
