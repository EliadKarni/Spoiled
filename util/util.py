import os


def get_ser_lst():
    return os.root_path
    return [series for series in os.walk(os.root_path)]


if __name__ == "__main__":
    print(get_ser_lst())
