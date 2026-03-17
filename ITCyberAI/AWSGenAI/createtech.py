# Creating Standardized Technical Components

# 6 Pillars of Excellence

# Operational Excellence - Prompt versioning and model lifecycle management

# Security - Defense in depth via Bedrock Guardrails.
# Implementation | VPC Endpoint - a secure private hallway for companies to receive information off the internet.
# Encryption at rest: Protects your data while it's in data storage.
# Encryption in transit: Protects your data while it's moving across networks
# IAM least privilege: Gives each employee the least amount of privilege they need to access files

# Reliability - Fallbacks and multi-region resilience
# Implementation | Exponential backoff retries: apply a stacking delay on server pings so the server doesn't get overloaded with retries.
# Cross-Region Model Failover: using other servers when one AI model goes down

# Performance - Optimized selection and response caching

# Cost Optimization - Model tiering based on complexity.
# Implementation | Token optimization: optimizing the use to cost ratio so users feel as though they are getting value
# Caching frequent requests: store the result of something expensive so the next time the same thing is asked, you can just hand back the saved answer.

# Sustainability - Right-sizing models for minimal footprint
# Implementation | Craft efficient prompts to reduce compute-per-transaction

# Enterprise Standardization Sandbox

# Prompt Template Example - Maintain versioned prompt templates to ensure consistency

PROMPT_TEMPLATES = {
    "summarization_v2": {
        "system": "You are a concise summarizer. Output only the summary.",
        "user": "Summarize the following in {max_sentences} sentences:\n\n{content}"
    }
}

# Guardrails Config - Define enterprise-standard guardrails for consistent security controls/

GUARDRAILS_CONFIG = {
  "name": "enterprise-standard-guardrail",
  "contentPolicyConfig": {
    "filtersConfig": [
      {"type": "HATE", "inputStrength": "HIGH", "outputStrength": "HIGH"},
      {"type": "VIOLENCE", "inputStrength": "HIGH", "outputStrength": "HIGH"}
    ]
  },
  "sensitiveInformationPolicyConfig": {
    "piiEntitiesConfig": [
      {"type": "EMAIL", "action": "ANONYMIZE"},
      {"type": "SSN", "action": "BLOCK"}
    ]
  }
}

# Infrastructure as Code (IaC) - Deploy all Bedrock resources through CDK, CloudFormation, or Terraform to ensure reproducibilty/auditability
# Write the infrastructure down as code so it can be versioned, repeated, and automated.
# CloudFormation | AWS's built-in tool. Write a big JSON/YAML file that describes the setup you want and AWS builds it.
# CDK | One level up from CloudFormation. Instead of raw YAML/JSON, you write real code. CDK handles the rest.
# Terraform | The Universal Remote. Made by HashiCorp in HCL. Works with any cloud - AWS, Azure, Google Cloud

class Construct:
    pass

class StandardKnowledgeBase(Construct):
    def __init__(self, scope, id, *, data_source_bucket, 
                 embedding_model="amazon.titan-embed-text-v2:0"):
        super().__init__(scope, id)
        # Reusable KB configuration with organizational defaults
        # Deployment includes security logging & encryption



