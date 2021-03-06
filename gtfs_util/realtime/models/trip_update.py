from gtfs_util.model import MixIn
from gtfs_util.realtime import data

from collections import namedtuple


class TripUpdate(namedtuple(
    'TripUpdate',
    [
        'trip',
        'stop_time_update',
        'vehicle',
        'timestamp',
        'delay',
    ]
), MixIn):
    NAME_MAPPING = {}
    DATA_MAPPING = {
        'timestamp': int,
        'stop_time_update': data.transform_stop_time_update,
    }

    FIELDS = (
        'trip',
        'stop_time_update',
        'vehicle',
        'timestamp',
        'delay',
    )
