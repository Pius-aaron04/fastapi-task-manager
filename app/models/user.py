from .base_model import BaseModel, Base
from sqlalchemy.orm import mappped_column, relationship, Mapped


class User(BaseModel, Base):
    """User data model for database queries
    """

    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(35), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String())
    task_folders: Mapped[List['TaskFolder']] = relationship(back_populates='user',
                                               cascade='all, delete-orphan',
                                               )
