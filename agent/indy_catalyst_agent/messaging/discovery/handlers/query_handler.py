"""Handler for incoming query messages."""

from ...base_handler import BaseHandler, BaseResponder, RequestContext
from ...message_factory import MessageFactory

from ..messages.disclose import Disclose
from ..messages.query import Query


class QueryHandler(BaseHandler):
    """Handler for incoming query messages."""

    async def handle(self, context: RequestContext, responder: BaseResponder):
        """Message handler implementation."""
        self._logger.debug("QueryHandler called with context %s", context)
        assert isinstance(context.message, Query)

        factory: MessageFactory = await context.inject(MessageFactory)
        types = factory.protocols_matching_query(context.message.query)
        reply = Disclose(protocols={k: {} for k in types})
        await responder.send_reply(reply)
