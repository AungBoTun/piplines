#!/usr/bin/env python3

from aws_cdk import core

from piplines.piplines_stack import PiplinesStack


app = core.App()
PiplinesStack(app, "piplines")

app.synth()
