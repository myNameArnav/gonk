import requests
import time
from config import BASE_URL, PORT, SIZE, BITS, DL_PARAMS, UP_PARAMS, RANDOM_DATA, HEADERS


def measure_download_speed(url: str = f"{BASE_URL}:{PORT}/download", bits=BITS) -> int:
    start_time = time.time()

    requests.get(
        url,
        params=DL_PARAMS,
        headers=HEADERS,
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    download_speed = (SIZE * (8 if bits else 1)) / (elapsed_time * 1024 * 1024)

    return download_speed


def measure_upload_speed(url: str = f"{BASE_URL}:{PORT}/upload", bits=BITS) -> int:
    random_data = RANDOM_DATA

    start_time = time.time()

    requests.post(
        url, params=UP_PARAMS, headers=HEADERS, data=random_data
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    upload_speed = (SIZE * (8 if bits else 1)) / (elapsed_time * 1024 * 1024)

    return upload_speed
