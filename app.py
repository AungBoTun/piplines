#!/usr/bin/env python3

from aws_cdk import core

from piplines.piplines_stack import PiplinesStack
from piplines.pipe_stack import PipeStack


app = core.App()
PiplinesStack(app, "piplines")
PipeStack(app,'PipeStack',env={
    'account':'308383475786',
    'region':'ap-southeast-1',
})

app.synth()
