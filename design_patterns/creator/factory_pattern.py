from pydantic import BaseModel
from abc import abstractmethod

# more info here https://github.com/ArjanCodes/2021-factory-pattern

class Connector(BaseModel):
    @abstractmethod
    def connect(self, client) -> str:
        raise NotImplementedError("Connect method must be implemented by subclasses.")

    @abstractmethod
    def invoke(self, client) -> str:
        raise NotImplementedError("Invoke method must be implemented by subclasses.")


class OpenAI(Connector):

    def connect(self, client) -> str:
        return f"Connecting to OpenAI with client {client}"

    def invoke(self, client) -> str:
        return f"Invoking OpenAI services with client {client}"


class Claude(Connector):
    def connect(self, client) -> str:
        return f"Connecting to Claude with client {client}"

    def invoke(self, client) -> str:
        return f"Invoking Claude services with client {client}"


class ConnectorFactory:
    @staticmethod
    def get_connector(connector_type: str) -> Connector:

        factories = {"openai": OpenAI, "claude": Claude}

        if connector_type in factories:
            return factories[connector_type]()
        else:
            raise ValueError(f"Unknown connector type: {connector_type}")


factory = ConnectorFactory()
openai_connector = factory.get_connector("openai")
claude_connector = factory.get_connector("claude")

claude_connector.connect("Claude Client")
openai_connector.connect("OpenAI Client")

openai_connector.invoke("OpenAI Client")
claude_connector.invoke("Claude Client")
    