import { Stack, StackProps } from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as lambda from "aws-cdk-lib/aws-lambda"
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class CloudStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

   const apiLambda = new lambda.Function(this, "ApiFunction", {
    runtime:lambda.Runtime.PYTHON_3_9,
    code: lambda.Code.fromAsset("../app/"),
    handler:"suggest_api.handler"
   })
  }
}
