from PIL import Image
import requests
from io import BytesIO
import concurrent.futures
from functools import wraps
import time
from Series import Spoiler_detector
from Macros import RestsMacros
from Macros.DetectorsMacros import *

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds\nstarted at: {start_time},'
              f'\nfinished at: {end_time}')
        return result
    return timeit_wrapper

@timeit
def download_image(url: str) -> Image:
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img


def check_image(url: str, detectors: list) -> Image:
    is_spoiler = PROCESSING
    img = Image.open(BytesIO(requests.get(url).content))
    results = [detector(img) for detector in detectors]
    while is_spoiler == PROCESSING:
        still_processing = False
        for check in results:
            result = check()
            if result == SPOILER:
                is_spoiler = SPOILER
            elif result == PROCESSING:
                still_processing = True
        if not still_processing:
            is_spoiler = NOT_SPOILER
    return is_spoiler == SPOILER


def check_images(urls: list, detectors: list) -> list:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = {url: executor.submit(check_image, url, detectors) for url in urls}
    return {url: results[url].result() for url in results}


def handle_req(req: dict) -> list:
    print([serie for serie in req[RestsMacros.SERIES]])
    detectors = [getattr(Spoiler_detector, serie) for serie in req[RestsMacros.SERIES]]
    res = check_images(req[RestsMacros.IMAGES], detectors)
    print(res)
    return res


if __name__ == '__main__':
    handle_req({RestsMacros.SERIES: ['Avatar'],
                RestsMacros.IMAGES: ['https://letsenhance.io/static/334225cab5be263aad8e3894809594ce/75c5a/MainAfter.jpg','https://static.vecteezy.com/packs/media/vectors/term-bg-1-3d6355ab.jpg']})
