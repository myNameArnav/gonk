import sqlite3
from time import time
from config import SIZE, SERVER

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
            server TEXT NOT NULL
        )
    """
    )


def insert_data_network(download_speed:float, upload_speed:float, size=SIZE, server=SERVER) -> dict:
    with sqlite3.connect("gonk.db") as conn:
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO network_data(timestamp, download, upload, size, server) VALUES (?, ?, ?, ?, ?)",
            (int(time()), download_speed, upload_speed, size, server)
        )

        return {"status": "success"}
