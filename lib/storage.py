import json
import os


def save(key, contents):
    """
    Save dictonary to storage solution. Filename will be constructed from a key: key.json.

    :param str key: Unique string to construct filename from
    :param dict contents: Dictronary presentation of file contents that will be converted to json string
    :return: Boolean
    """
    STORAGE_ROOT = os.environ['STORAGE_ROOT']
    file_name = "%s.json" % (key)
    absolute_path = os.path.join(STORAGE_ROOT, file_name)
    json_object = json.dumps(contents)

    try:
        with open(absolute_path, "w") as file:
            file.write(json_object)
        return True
    except:
        return False


def get(key):
    """
    Get single entry from storage by key

    :param str key: Entry key
    :return: Dict
    """
    STORAGE_ROOT = os.environ['STORAGE_ROOT']
    file_name = "%s.json" % (key)
    absolute_path = os.path.join(STORAGE_ROOT, file_name)
    try:
        file = open(absolute_path)
        data = json.load(file)
        return data
    except:
        # TODO: log error
        return None
