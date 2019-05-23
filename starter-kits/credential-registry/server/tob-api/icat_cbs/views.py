from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from icat_cbs.serializers.indy import IndyAgentCallbackSerializer

from api_indy.views.indy import store_credential_int

import json


TOPIC_CONNECTIONS   = "connections"
TOPIC_CREDENTIALS   = "credentials"
TOPIC_PRESENTATIONS = "presentations"
TOPIC_GET_ACTIVE_MENU = "get-active-menu"
TOPIC_PERFORM_MENU_ACTION = "perform-menu-action"


class agentCallbackViewset(APIView):
    permission_classes = [permissions.AllowAny,]
    serializer_class = IndyAgentCallbackSerializer

    def get_serializer_class(self):
        return self.serializer_class

    def post(self, request, *args, **kwargs):
        return Response("")


@api_view(['POST',])
@permission_classes((permissions.AllowAny, ))
def agent_callback(request, topic):
    message = request.data
    serializer_class = IndyAgentCallbackSerializer

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
    """
    Receives notification of a credential processing event:
        message = {
            "connection_id": "...",
            "credential_definition_id": "...",
            "credential_exchange_id": "...",
            "credential_id": "...",
            "credential_offer": {...},
            "credential_request": {...},
            "credential_request_metadata": {...},
            "credential": {
                "referent": "same as credential_id", 
                "attrs": {"degree": "Maths", "age": "24", "date": "2018-05-28", "name": "Alice Smith"}, 
                "schema_id": "same as schema_id", 
                "cred_def_id": "same as credential_definition_id", 
                "rev_reg_id": null, 
                "cred_rev_id": null
            },
            "initiator": "...",
            "schema_id": "...",
            "state": "...",
            "thread_id": "..."
        }
    """
    #global admin_url
    credential_exchange_id = message['credential_exchange_id']
    print("Credential: state=", state, ", credential_exchange_id=", credential_exchange_id)

    if state == 'offer_received':
        print("After receiving credential offer, send credential request")
        #resp = requests.post(admin_url + '/credential_exchange/' + credential_exchange_id + '/send-request')
        #assert resp.status_code == 200
        return Response("")

    elif state == 'stored':
        print("After stored credential in wallet")
        # TBD credential info should come with the message
        #resp = requests.get(admin_url + '/credential/' + message['credential_id'])
        #assert resp.status_code == 200
        print("Stored credential:")
        print(message['credential'])
        print("credential_id", message['credential_id'])
        print("credential_definition_id", message['credential_definition_id'])
        print("schema_id", message['schema_id'])
        print("credential_request_metadata", message['credential_request_metadata'])

        return store_credential_int({"credential_data": message['credential'],
            "credential_request_metadata": message['credential_request_metadata']})

    # TODO other scenarios
    return Response("")


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

