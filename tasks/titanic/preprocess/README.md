# Titanic - preprocess
## Description
This Task adds a new column named \"CabinClass\" to the input CSV file. The \"CabinClass\" column contains the first character of the \"Cabin\" column, or \"U\" if the \"Cabin\" column is empty. The processed data is written to an output CSV file.

### Example
`Input`:
```csv
PassengerId,Pclass,Name,Cabin
1,3,John,D123
2,1,Jane,B22
3,2,David,
```

`Output`:
```csv
PassengerId,Pclass,Name,Cabin,CabinClass
1,3,John,D123,D
2,1,Jane,B22,B
3,2,David,,U
```
## Inputs
- `input` - input CSV file

## Outputs
- `output` - output CSV file with added \"CabinClass\" column