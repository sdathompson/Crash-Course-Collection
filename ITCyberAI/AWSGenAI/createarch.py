# Choosing a model
# Task type - determine requirements (i.e. text gen or image creation)
# Latency - Real-time applications (Chatbot) vs. Batch processing (Document analysis)
# Cost Efficiency - Balance token-based prompt against provisioned throughput
# Accuracy - Evaluate against specific use-case benchmarks
# Context Window - Determine document length limits
# Fine-tuning - Availability of custom training data

# Amazon Bedrock is the AWS service that helps customers manage serverless applications and infrastructure
# Foundation Models (FMs) are large-scale pre-trained AI models

# Proof of Concept
# Phase 1: Rapid Prototyping - Begin with Amazon Bedrock Playground. Test multiple models with identical prompts.
# Document initial observations regarding response quality, latency, and token consumption.

# Phase 2: Programmatic Testing - Transition to programmatic testing with representative text datasets.
# A minimum of 200 test cases is recommended to achieve statistical significance

import boto3
import json

bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')

def test_model(model_id, prompt, test_cases):
    results = []
    for case in test_cases:
        response = bedrock_runtime.invoke_model(
            modelId=model_id,
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": prompt.format(**case)}]
            })
        )
        results.append(json.loads(response['body'].read()))
    return results

# Phase 3: Evaluation Metrics
# Accuracy: Combine human evaluation with automated scoring against golden datasets.
# Latency: Capture P50 (typical user response time), P95 (what the worst regular users feel), and P99 (the worst case scenerio)
# Cost: Token consumption * Model pricing
# Consistency: Measure response variance across similar inputs to assess reliability

# TODO: Customer Support Chat Bot
# TODO: Dataset Creation - Compile 200 real customer queries
# TODO: Model Comparision - Evaluated Claude Haiku for speed and cost efficiency against Claude Sonnet for accuracy
# TODO: Results Analysis - Claude Haiku: 0.8ms at $.50 per 1k queries with 82% accuracy. Claude Sonnet delivered 2.1 ms at $3.00 per 1k queries with 94%
# TODO: Architectural Decision: Implement intelligent routing using Haiku for simple queries and Sonnet for complex issues.
# TODO: Business Value Validation: Projected 40% reduction in support ticket volume based on PoC accuracy metrics.



