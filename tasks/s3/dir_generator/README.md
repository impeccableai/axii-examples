# S3 Dir Generator
## Description
This Task generates multiple files with a specified number of lines and uploads them to an S3 bucket. The output S3 path is specified using the `--output` flag. The Task loops through the range of the `count` parameter and creates an S3 object for each file with the line content.

## Outputs
- `output` - S3 directory path where the generated files are uploaded

## Parameters
- `count` - number of files to generate (default: 10)

## Environment Variables
- `S3_ACCESS_KEY` - AWS access key for S3
- `S3_SECRET_KEY` - AWS secret key for S3
- `S3_HOST` - S3 host URL