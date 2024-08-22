# Generate UUID
Generates a random UUID using the `uuid` module in python.

## Inputs
* `version` - REQIURED - Version of UUID to generate. Versions are 1, 3, 4, and 5.
> Note: Version 1 may pose a safety risk because it uses your network info.
* `namespace` - optional - namespace of the UUID. Can be DNS, URL, OID, or X500.
* `name` - optional - string that will be used to create the UUID.

## Outputs
* `uuid` - The generated UUID
* `safe` - The safeness of the UUID. `safe` means the UUID was generated by the platform in a multiprocessing-safe way, `unsafe` means the UUID was not generated in a multiprocessing-safe way, and `unknown` means the platform did not provide information on whether the UUID was generated safely or not.
<sup>Source: [[1]](https://docs.python.org/3/library/uuid.html#uuid.SafeUUID)</sup>

## Usage
```yaml
- uses: actions/checkout@v5
- uses: bossOfCode/generate-uuid@v1 #Use current version
  with: 
    - version: 5 #v1, 3, 4, snd 5 are avaliable
```

<footer> [1]: docs.python.org </footer>