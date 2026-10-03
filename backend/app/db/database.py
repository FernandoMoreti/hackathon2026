from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.db.config import settings
from app.db.base import Base


class Database:
    def __init__(self, database_url: str) -> None:
        self.engine: Engine = create_engine(database_url, pool_pre_ping=True)
        self.session_factory = sessionmaker(
            bind=self.engine,
            autoflush=False,
            expire_on_commit=False,
        )

    @contextmanager
    def session(self) -> Iterator[Session]:
        with self.session_factory.begin() as session:
            yield session

    def create_schema(self) -> None:
        from app.models import order, user

        Base.metadata.create_all(bind=self.engine)

    def dispose(self) -> None:
        self.engine.dispose()


database = Database(settings.database_url)