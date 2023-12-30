import sqlite3
from time import time
from config import SIZE, SERVER, IS_BITS, BYTE

with sqlite3.connect("gonk.db") as conn:
    cursor = conn.cursor()

    # cursor.execute(
    #     """
    #         drop table network_data;
    # """
    # )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS network_data (
            id INTEGER PRIMARY KEY,
            timestamp INTEGER NOT NULL,
            size INTEGER NOT NULL,
            download REAL NOT NULL,
            upload REAL NOT NULL,
            is_bits INTEGER NOT NULL,
            server TEXT NOT NULL
        )
    """
    )


def insert_data_network(
    download_speed: float,
    upload_speed: float,
    size=SIZE,
    server=SERVER,
    is_bits=IS_BITS,
) -> dict:
    with sqlite3.connect("gonk.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO network_data(timestamp, download, upload, size, server, is_bits) VALUES (?, ?, ?, ?, ?, ?)",
            (int(time()), download_speed, upload_speed, size, server, is_bits),
        )
        human_size = SIZE / BYTE
        return {
            "status": "success",
            "download_speed": download_speed,
            "upload_speed": upload_speed,
            "size": human_size,
        }


def show_network_history() -> list:
    with sqlite3.connect("gonk.db") as conn:
        cursor = conn.cursor()

        cursor.execute(
            "select timestamp, download, upload, size, server, is_bits from network_data"
        )
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]
        result = {"data": [dict(zip(columns, row)) for row in rows]}

        return result


def show_filtered_history_data(from_date, to_date) -> list:
    with sqlite3.connect("gonk.db") as conn:
        cursor = conn.cursor()
        cursor.execute(
            "select timestamp, download, upload, size, server, is_bits from network_data where timestamp between ? and ?",
            (from_date, to_date),
        )
        rows = cursor.fetchall()

        columns = [desc[0] for desc in cursor.description]
        result = {"data": [dict(zip(columns, row)) for row in rows]}
        
        return result
