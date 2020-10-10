from aws_cdk import core
from aws_cdk import aws_codepipeline as codepipeline
from aws_cdk import aws_codepipeline_actions as cpations
from aws_cdk import pipelines
from .webservice_stage import webservice_stage

class PipeStack(core.Stack):
      def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        #declare sourece and destination 
        source_artifact = codepipeline.Artifact()
        cloud_assembly_artifact = codepipeline.Artifact()

        #declare pipline 
        pipeline = pipelines.CdkPipeline(self, 'Pipeline',
            cloud_assembly_artifact=cloud_assembly_artifact,
            pipeline_name='Pipline',
        
        #Code Trigger point to GitHub and take token from secert manager 
            source_action=cpations.GitHubSourceAction(
                action_name='GitHub',
                output=source_artifact,
                oauth_token=core.SecretValue.secrets_manager('github-token'),
                owner='AungBoTun',
                repo="piplines",
                trigger=cpations.GitHubTrigger.POLL),

        #Code Build to execute ckd to CF 
            synth_action=pipelines.SimpleSynthAction(
                source_artifact=source_artifact,
                cloud_assembly_artifact=cloud_assembly_artifact,
                install_command='npm install -g aws-cdk && pip install -requrements.txt',
                synth_command='cdk synth'))

        pipeline.add_application_stage(webservice_stage(self, 'Pre-Prod', env={
            'account':'308383475786',
            'region':'ap-southeast-1',
        }))