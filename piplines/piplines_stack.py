from aws_cdk import core
from os import path 
import aws_cdk.aws_lambda as lmb
import aws_cdk.aws_apigateway as apigw


class PiplinesStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        this_dir = path.dirname(__file__)

        #declare lambdahandler with specifc values (language,handlername,locationof lambda file)
        handler = lmb.Function(self, 'Handler',   
            runtime= lmb.Runtime.PYTHON_3_7,
            handler='handler.handler',
            code=lmb.Code.from_asset(path.join(this_dir,'lambda')))

        #declare api simple restapi to assign lambda function 
        gw = apigw.LambdaRestApi(self, 'Gateway',
            description ='Endpoint for a simple Lambda-powered web service',
            handler=handler.current_version)

        #declare cfoutput to get apigatewayurl 
        self.url_output= core.CfnOutput(self, 'Url',
            value=gw.url)
