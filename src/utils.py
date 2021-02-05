"""
utils for the rest of the tooling
"""
import datetime


def changed_after_days(days_before=7):
    """
    Terribly named function.
    aims to let you specify how long ago to check back.
    """
    res = (datetime.datetime.now() - datetime.timedelta(days=days_before))
    # feedparser uses struct_time for some reason.
    return res.timetuple()
