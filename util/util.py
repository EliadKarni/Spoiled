import os


def get_ser_lst(rootpath: str):
    return [series for series in os.walk(rootpath)]#[0][1]


if __name__ == "__main__":
    print(get_ser_lst())
