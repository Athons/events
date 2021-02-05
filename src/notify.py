from gitterpy.client import GitterClient

class Notify:
    """
    Hacky class for notifying gitter.
    """
    def __init__(self, token, community):
        self.community = community
        self.client = GitterClient(token)

    def send(self, channel, message):
        """
        Send a message to the webhook
        """
        self.client.messages.send('{}/{}'.format(self.community, channel), message)
