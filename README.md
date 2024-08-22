## Generate UUID
Generates a random UUID using the `uuid` module in python.

# Inputs
* `version` - Version of UUID to generate. Versions are 1 to 8.
> Note: Version 1 may pose a safety risk because it uses your network info.

# Outputs
* `uuid` - The generated UUID

# Usage
```yaml
- uses: actions/checkout@v5
- uses: bossOfCode/generate-uuid@v1 #Use current version
  with: 
    version: 5 #any number between 1 to 8
```
