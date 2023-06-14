# S3 Generator
## Description
This Task generates a text file with numbers from 0 to 14 and uploads it to an S3-compatible storage service. The output file location is specified as a command line argument using the \"output\" flag. The Task uses the `boto3` library to interact with S3 and requires the `S3_HOST`, `S3_ACCESS_KEY`, and `S3_SECRET_KEY` environment variables to be set.

### Example
`Output`:
```text
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
```
## Outputs
- `output` - file uploaded to S3

## Environment Variables
- `S3_HOST` - S3-compatible storage service host
- `S3_ACCESS_KEY` - access key for S3-compatible storage service
- `S3_SECRET_KEY` - secret key for S3-compatible storage service