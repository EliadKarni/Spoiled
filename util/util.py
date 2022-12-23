from os import walk

SERIES_PATH = "Series"


def get_ser_lst():
    return [series for series in walk(SERIES_PATH)][0][1]


if __name__ == "__main__":
    print(get_ser_lst())
