"""Import Operating System and UUID"""
import os
import uuid

version = os.environ.get("INPUTS_UUID")
namespace = os.environ.get("INPUTS_NAMESPACE")

versions = [1, 3, 4, 5]

def printInOs(input):
    print(f"{input}")
    os.system(f"{input}")

if version in versions:
    if version == 1:
        output = uuid.uuid1()
    else:
        if version == 3:
            output = uuid.uuid3(namespace)
        else:
            if version == 4:
                output = uuid.uuid4()
            else:
                if version == 5:
                    output = uuid.uuid5(namespace)
else:
    exit(f"ERROR: version {version} does not exist")

output = str(output)
printInOs(f"::set-output name=uuid::{output}")

printInOs(f"Generated UUID {output}")

