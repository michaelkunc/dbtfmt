"""holds the main methods for this package"""
from collections import defaultdict
from typing import List, Dict


def reader(filepath: str) -> List[str]:
    with open(filepath) as sql_file:
        file_contents = sql_file.read().replace("/n", "").lower()
    return file_contents.split()


def scan_file(file_contents: List) -> Dict:
    key_chars = ["select", "{{", "config(", "}}", "from", "where"]
    scan_result = defaultdict(list)
    for i, e in enumerate(file_contents):
        for k in key_chars:
            if e == k:
                scan_result[k].append(i)
    return scan_result
