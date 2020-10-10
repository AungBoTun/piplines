from aws_cdk import core

from .piplines_stack import PiplinesStack

class webservice_stage(core.Stage):
      def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        service = PiplinesStack(self, 'WebService')

        self.url_output = service.url_output


