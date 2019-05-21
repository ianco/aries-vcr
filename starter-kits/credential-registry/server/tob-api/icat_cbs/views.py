from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


TOPIC_CONNECTIONS   = "connections"
TOPIC_CREDENTIALS   = "credentials"
TOPIC_PRESENTATIONS = "presentations"
TOPIC_GET_ACTIVE_MENU = "get-active-menu"
TOPIC_PERFORM_MENU_ACTION = "perform-menu-action"


@api_view(['POST',])
def agent_callback(request, topic):
    message = json.loads(request.data)

    # dispatch based on the topic type
    if topic == TOPIC_CONNECTIONS:
        return handle_connections(message['state'], message)

    elif topic == TOPIC_CREDENTIALS:
        return handle_credentials(message['state'], message)

    elif topic == TOPIC_PRESENTATIONS:
        return handle_presentations(message['state'], message)

    elif topic == TOPIC_GET_ACTIVE_MENU:
        return handle_get_active_menu(message)

    elif topic == TOPIC_PERFORM_MENU_ACTION:
        return handle_perform_menu_action(message)

    else:
        print("Callback: topic=", topic, ", message=", message)
        return Response("Invalid topic: "+topic, status=status.HTTP_400_BAD_REQUEST)


def handle_connections(state, message):
    # TODO auto-accept?
    print("handle_connections()", state)
    return Response(some_data)


def handle_credentials(state, message):
    # TODO auto-accept offer and save credentials
    print("handle_credentials()", state)
    return Response(some_data)


def handle_presentations(state, message):
    # TODO auto-respond to proof requests
    print("handle_presentations()", state)
    return Response(some_data)


def handle_get_active_menu(message):
    # TODO add/update issuer info?
    print("handle_get_active_menu()", message)
    return Response("")


def handle_perform_menu_action(message):
    # TODO add/update issuer info?
    print("handle_perform_menu_action()", message)
    return Response("")

