from typing import Dict, List, Tuple

import numpy as np


def main(
    seeds: List[int],
    maps: Dict[Tuple[str, str], Dict[str, List[int]]],
):
    # Reorder maps by ascending source_range_start
    for key, data in maps.items():
        order = np.argsort(data["source_range_start"])
        for subkey, value in data.items():
            maps[key][subkey] = [value[i] for i in order]

    output_type = "location"
    almanac = []
    outputs = []
    for seed in seeds:
        value = {"seed": seed}
        while output_type not in value:
            source_type = list(value)[-1]
            dest_type, ranges = next(
                (key[1], value) for key, value in maps.items() if key[0] == source_type
            )
            i = next(
                (
                    i
                    for (i, start) in enumerate(ranges["source_range_start"])
                    if start <= value[source_type] < start + ranges["range_length"][i]
                ),
                None,
            )
            if i is not None:
                value[dest_type] = ranges["dest_range_start"][i] + (
                    value[source_type] - ranges["source_range_start"][i]
                )
            else:
                value[dest_type] = value[source_type]
        almanac.append(value)
        outputs.append(value[output_type])
    return min(outputs)
