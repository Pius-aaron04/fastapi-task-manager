'''Task folder model'''
from .base_model import Base, BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String


class TaskList(BaseModel, Base):
    """ Task Folder model for db interaction
    """

    __tablename__ = 'task_list'

    id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid4()))
    user_id: Mapped[str] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship(back_populates="task_lists", uselist=False)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(nullable=True)
    parent_id: Mapped[str] = mapped_column(ForeignKey('task_lists.id'), nullable=True)
    parent: Mapped["TaskList"] = relationship("TaskList",
                                                remote_side=[id],
                                                backref="sublists")
