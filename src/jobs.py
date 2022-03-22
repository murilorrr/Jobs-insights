from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path, "r") as file:
        jobsStructured = csv.DictReader(file)
        array = []
        for item in jobsStructured:
            array.append(item)
        return array
