import re
from typing import Dict, List, Tuple

import numpy as np


def parse(
    input_file,
) -> Tuple[List[int], Dict[Tuple[str, str], Dict[str, List[int]]]]:
    with open(input_file, "r") as fin:
        lines = fin.readlines()

    seeds = [int(x) for x in lines[0].split()[1:]]

    header_pattern = re.compile(r"(\w+)\-to\-(\w+)\s+map:")
    maps: Dict[Tuple[str, str], Dict[str, List[int]]] = {}
    for line in iter(lines[1:]):
        if line.isspace():
            continue
        match = re.match(header_pattern, line)
        if match:
            source = match.group(1)
            destination = match.group(2)
            maps[(source, destination)] = {
                "source_range_start": [],
                "dest_range_start": [],
                "range_length": [],
            }
        else:
            (
                dest_range_start,
                source_range_start,
                range_length,
            ) = (int(x) for x in line.split())
            maps[(source, destination)]["source_range_start"].append(source_range_start)
            maps[(source, destination)]["dest_range_start"].append(dest_range_start)
            maps[(source, destination)]["range_length"].append(range_length)

    for key, data in maps.items():
        order = np.argsort(data["source_range_start"])
        for subkey, value in data.items():
            maps[key][subkey] = [value[i] for i in order]

    return seeds, maps
