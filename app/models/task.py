from .base_model import BaseModel, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


class Task(BaseModel, Base):
    """ Task model for db interaction
    """

    __tablename__ = 'tasks'

    description: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String(35))
    parent_id: Mapped[str] = mapped_column(ForeignKey('task_lists.id'))
    parent: Mapped["TaskList"] = relationship("TaskList", backref="tasks")

    def __repr__(self):
        return f"Task(id={self.id!r}, description={self.description!r}, status={self.status}, parent_id={self.parent_id})"
