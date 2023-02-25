from typing import Tuple
import re
from datetime import datetime
from dateutil.parser import parse as datetime_parse
from timesheet.table import insert, get, delete


def entry_parse(entry: str) -> (Tuple[str, str]):
    """Parse entry string into project and entry"""
    if ";;" in entry:
        # tasksless entry
        return "", entry
    else:
        # task entry
        try:
            i = entry.index(":")
        except ValueError:
            return "", entry

        return entry[:i], entry[i + 1 :].strip()


def insert_entry(time_str: str, entry_str: str, merge: bool = False):
    """
    Insert entry in timesheet table
    time_str: time string
    entry_str: entry string
    merge: merge with last entry if True

    Currently merge is done by deleting the last entry and inserting a new one. This is not ideal. But it works for now. The ideal way would be to update the last entry.
    """
    try:
        t = datetime_parse(time_str)
        # t =t.isoformat()
    except:
        t = datetime.now()
    proj, entry = entry_parse(entry_str)
    print(t, proj, entry, sep="--")

    if merge:
        date_str = t.strftime("%Y-%m-%d")
        e = [
            e
            for e in get(
                where_clause=f"where date_str = '{date_str}'",
                order_by_clause="order by end_time desc",
                limit_clause="limit 1",
            )
        ]
        if len(e) == 1:
            e = e[0]
            if e[4] == proj and e[3] == entry:
                # delete last entry
                id = e[0]
                print("Merging with last entry")
                delete(id)

    insert(t, proj, entry)


def make_entry(entry: str):
    """Make entry in timesheet table"""

    ee = entry.strip().split()
    if len(ee) == 0:
        raise Exception("Invalid")

    ee = [e.strip() for e in ee]

    if not re.match("^[0-9:]+$", ee[0]):
        insert_entry(datetime.now().isoformat(), " ".join(ee), True)
    else:
        if len(ee) == 1:
            Exception("Invalid")
        insert_entry(ee[0], " ".join(ee[1:]), True)
