#!/bin/bash
cat > template.yaml <<EOM
AWSTemplateFormatVersion: '2010-09-09'
Transform: AWS::Serverless-2016-10-31
Resources:
  SampleLambdaFunction:
      Type: 'AWS::Serverless::Function'
      Properties:
        FunctionName: sample-lambda
        Handler: lambda_function.lambda_handler
        Runtime: python3.9
        CodeUri: functions/
        Timeout: 30
        MemorySize: 128
        Role: $LAMBDA_EXECUTION_RLE
        Environment:
          Variables:
            API_URL: $API_URL
EOM