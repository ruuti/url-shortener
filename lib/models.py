import uuid
from pydantic import BaseModel, HttpUrl

from lib import storage


def create_key():
    """
    Create entry key

    :return: Key string
    """
    return str(uuid.uuid4())[:8]


class Url(BaseModel):
    id: str = create_key()
    url: HttpUrl

    def get(id):
        file = storage.get(id)
        return Url(id=id, **file)

    def save(self):
        object_to_store = {
            'url': self.url
        }
        return storage.save(self.id, object_to_store)
