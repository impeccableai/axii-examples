# GCS generator
## Description
This Task generates a sequence of integers from 0 to 14 and uploads it to a Google Cloud Storage (GCS) bucket specified by the `--output` argument. The Task uses the Google Cloud Storage Client library to interact with GCS.

## Inputs
- None

## Outputs
- `output` - Google Cloud Storage file containing the generated sequence

## Parameters
- `GOOGLE_APPLICATION_CREDENTIALS` - environment variable containing the GCS credentials as a JSON string or a path to the credentials file