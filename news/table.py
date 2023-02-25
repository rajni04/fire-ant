import time
import logging
from uuid import uuid4
import pg

logger = logging.getLogger(__name__)

table_query = (
    """CREATE TABLE IF NOT EXISTS news (
        id varchar(255) PRIMARY KEY NOT NULL,
        url TEXT UNIQUE NOT NULL,
        content TEXT,
        word_count INT,
        created_at bigint) """,
)


def insert(url, content, word_count):
    u = uuid4()
    content = content.replace("'", "''")
    s = f"""INSERT INTO news (id, created_at, url, content, word_count) values (
        'n_{str(u)}',
        {int(time.time())},
        '{url}',
        '{content}',
        {word_count}
    )"""
    logger.debug("-->", s)
    pg.execute(s)
