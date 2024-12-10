from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from uuid import uuid4
from datetime import datetime
from sqlalchemy import DateTime, String


class Base(DeclarativeBase):
    pass


class BaseModel:
    id: Mapped[str] = mapped_column(primary_key=True, default=str(uuid4))
    created_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[str] = mapped_column(DateTime, default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """ Instantiates a new model."""
        if kwargs:
            # sets instance attributes from keyword arguments
            if '__class__' in kwargs:
                del kwargs['__class__']
            for k, v in kwargs.items():
                setattr(self, k, v)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid4()))

        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def to_dict(self):
        attrs = {}
        for key, value in self.__dict__.items():
            if key != 'password':
                attrs.update({key: value})
        return attrs    
