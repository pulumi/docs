---
title: Convert CloudFormation Templates to a Programming Language
url: /cf2pulumi
layout: cf2pulumi
linktitle: CloudFormation to Pulumi
menu:
  converters:
    identifier: cf2pulumi
    weight: 1
    
meta_desc: See what your CloudFormation templates would look like in a modern programming language thanks to Pulumi.

examples:
    - name: Provision a Log Group
      filename: instance.yaml
      description:
      code: |
        AWSTemplateFormatVersion: "2010-09-09"
        Description: Create a simple Log Group
        Parameters:
          KmsKeyId:
            Type: String
            Description: The Amazon Resource Name (ARN) of the CMK to use when encrypting log data.
        Resources:
          myLogGroup:
            Type: AWS::Logs::LogGroup
            Properties:
              KmsKeyId: Fn::Sub: ${KmsKeyId}
              LogGroupName: myLogGroup
              RetentionInDays: 7

    - name: A Sample Lambda Step Function
      filename: aws.yaml
      description:
      code: |
        AWSTemplateFormatVersion: '2010-09-09'
        Description: An example template for a Step Functions state machine.
        Resources:
          MyStateMachine:
            Type: AWS::StepFunctions::StateMachine
            Properties:
              StateMachineName: HelloWorld-StateMachine
              DefinitionString: |-
                {
                  "StartAt": "HelloWorld",
                  "States": {
                    "HelloWorld": {
                      "Type": "Task",
                      "Resource": "arn:aws:lambda:us-east-1:111122223333:function:HelloFunction",
                      "End": true
                    }
                  }
                }
              RoleArn: arn:aws:iam::111122223333:role/service-role/StatesExecutionRole-us-east-1
              Tags:
                -
                  Key: "keyname1"
                  Value: "value1"
                -
                  Key: "keyname2"
                  Value: "value2"

form:
    hubspot_form_id: 8381e562-5fdf-4736-bb10-86096705e4ee
---
