import os
import uuid
from pydantic import BaseModel, HttpUrl, Field

from lib import cache
from lib import storage


def create_key():
    """
    Create entry key

    :return: Key string
    """
    return str(uuid.uuid4())[:8]


class Url(BaseModel):
    id: str = Field(default_factory=create_key)
    url: HttpUrl
    short_link: HttpUrl = None

    def __init__(self, **data):
        super().__init__(**data)

        BASE_URL = os.environ['BASE_URL']
        link = "%s/%s" % (BASE_URL, self.id)
        self.short_link = link

    def get(id):
        cached = cache.get_by_key(id)
        if cached:
            return Url(id=id, **cached)

        file = storage.get(id)
        if file:
            cache.set_entry(id, file)
        return Url(id=id, **file)

    def save(self):
        object_to_store = {
            'url': self.url
        }
        return storage.save(self.id, object_to_store)
