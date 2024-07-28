from datetime import datetime

import pytz


def local_now():
    timezone = pytz.timezone('Europe/Budapest')
    return datetime.now(timezone)
