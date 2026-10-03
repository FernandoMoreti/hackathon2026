from collections.abc import Generator

from sqlalchemy.orm import Session

from app.db.database import database

def get_db_session() -> Generator[Session, None, None]:
    with database.session() as session:
        yield session