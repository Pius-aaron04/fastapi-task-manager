from .base_model import BaseModel, Base
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import String

class User(BaseModel, Base):
    """User data model for database queries
    """

    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(35), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String())
    task_lists: Mapped[list['TaskList']] = relationship(back_populates='user',
                                               cascade='all, delete-orphan',
                                               )
