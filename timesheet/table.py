import logging
from datetime import datetime
from uuid import uuid4
import pg

logger = logging.getLogger(__name__)

table_query = (
    """CREATE TABLE IF NOT EXISTS timesheet (
        id VARCHAR(255) PRIMARY KEY NOT NULL,
        date_str VARCHAR(8),
        end_time BIGINT,
        work TEXT,
        project VARCHAR(255),
        created_at BIGINT) """,
)


def insert(time_obj, project, work):
    u = uuid4()
    project = project.replace("'", "''")
    work = work.replace("'", "''")
    s = f"""INSERT INTO timesheet (id, date_str, end_time, work, project, created_at) values (
        'ts_{str(u)}',
        '{time_obj.date().isoformat()}',
        {time_obj.timestamp()},
        '{work}',
        '{project}',
        {datetime.now().timestamp()}
    )"""
    logger.debug("-->", s)
    pg.execute(s)


def get(
    where_clause="",
    order_by_clause="order by end_time ASC",
    limit_clause="limit 50 offset 0",
):
    query = f"select id, date_str, end_time, work, project, created_at from timesheet {where_clause} {order_by_clause} {limit_clause};"
    return pg.yield_results(query)


def delete(id: str):
    if len([a for a in get(f"where id = '{id}'")]) == 1:
        s = f"DELETE FROM timesheet WHERE id = '{id}'"
        logger.debug("-->", s)
        pg.execute(s)
    else:
        print("no timesheet entry work found")
