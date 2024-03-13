import uuid
import datetime


class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        print f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        self.__dict__.__setitem__('__class__', self.__class__.__name__)

        return dict(self.__dict__)
