from datetime import datetime, timedelta
import math


def to_datetime(epoch_ms: int):
    try:
        return datetime.fromtimestamp(epoch_ms/1000).strftime("%Y-%m-%dT%H:%M:%SZ")
    except:
        raise ValueError(f"Wrong format (%Y-%m-%dT%H:%M:%SZ) for epoch_ms: {epoch_ms}")


def is_epoch_time(value: int) -> bool:
    if isinstance(value, int):
        if value > 0 and len(str(value)) == 13 and str(value)[:2] == "16":
            return True

    return False


def convert_times(json_data: dict) -> dict:
    for key, value in json_data.items():
        if is_epoch_time(value):
            json_data[key] = to_datetime(value)
        if isinstance(value, dict):
            convert_times(value)
        elif isinstance(value, list):
            for val in value:
                if isinstance(val, str):
                    pass
                elif isinstance(val, list):
                    pass
                else:
                    convert_times(val)

    return json_data
