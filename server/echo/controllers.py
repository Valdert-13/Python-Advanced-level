from protocol import make_response
from messenger.controllers import send_message


def get_echo(request):
    data = request.get('data')
    return make_response(request, 200, data)
