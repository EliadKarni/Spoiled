import os


def get_ser_lst():
    return [series for series in os.walk(os.root_path)][0]


if __name__ == "__main__":
    print(get_ser_lst())
