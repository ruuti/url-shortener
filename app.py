from chalice import Chalice, Response
from pydantic import ValidationError

from lib.models import Url


app = Chalice(app_name='short')


@app.route('/{id}', methods=['GET'])
def get(id):
    try:
        url = Url.get(id=id)
        return Response(body=url.json(), status_code=200)
    except:
        return Response(body=None, status_code=404)


@app.route('/', methods=['POST'], content_types=['application/json'])
def create():
    try:
        url = Url(**app.current_request.json_body)
        url.save()
        return Response(body=url.json(), status_code=200)
    except ValidationError as e:
        return Response(body=e.json(), status_code=400)
