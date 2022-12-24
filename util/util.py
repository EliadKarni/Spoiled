import os
import logging


def get_ser_lst(rootpath: str):
    try:
        return [series for series in os.walk(os.path.join(rootpath, "Series"))][0][1]
    except Exception as e:
        logging.exception(e)
        return []


if __name__ == "__main__":
    print(get_ser_lst())
