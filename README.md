# AWS Lambda CodeDeploy Project

Demonstrates automated Lambda deployments through CodePipeline, where CodeBuild packages the function and publishes versions, while CodeDeploy performs blue-green traffic shifting between Lambda alias versions.

## Project Structure

```bash
├── lambda_function.py    # Main Lambda handler
├── requirements.txt      # Python dependencies
├── appspec.yml          # CodeDeploy configuration
├── buildspec.yml        # CodeBuild configuration
```

## Prerequisites

- AWS Lambda function `sabs-lambda` exists
- Lambda alias `live` exists that points to version 1.
- CodeBuild configuration.
- CodeDeploy application and deployment group configured
- IAM roles with proper permissions

## Deployment Process

1. **Build Phase**: Installs dependencies and creates deployment package
2. **Post Build Phase**: Updates Lambda code and publishes new version
3. **CodeDeploy**: Shifts traffic from current to new version using canary, linear or allinone strategy.

## Key Features

- **Dynamic Versioning**: Automatically detects current version and creates new version
- **Traffic Shifting**: Uses CodeDeploy for safe deployments with rollback capability
- **Validation Hooks**: Pre and post-deployment validation functions

## Usage

Push code to trigger CodePipeline, which will:
1. Build Lambda package with dependencies
2. Update function code
3. Deploy using CodeDeploy with traffic shifting

## Configuration

Update `appspec.yml` placeholders are automatically replaced during build:
- `Current_Version` → Current alias version
- `Target_Version` → Newly published version