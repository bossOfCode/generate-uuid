"""Import Operating System and UUID"""
import os
import sys
import uuid

version = os.environ.get("INPUTS_UUID")
namespace = os.environ.get("INPUTS_NAMESPACE")
name = os.environ.get("INPUTS_NAME")

versions = [1, 3, 4, 5]
namespaces = ["DNS", "URL", "OID", "X500"]

def print_in_os(argument):
    "print in both terminal and action logs"
    print(f"{argument}")
    os.system(f"{argument}")

if version in versions or namespace in namespaces:
    if version == 1:
        output = str(uuid.uuid1())
    else:
        if version == 3:
            output = str(uuid.uuid3(str("NAMESPACES_" + namespace), name))
        else:
            if version == 4:
                output = str(uuid.uuid4())
            else:
                if version == 5:
                    output = str(uuid.uuid5(str("NAMESPACES_" + namespace), name))
else:
    if namespace in namespaces:
        sys.exit(f"ERROR: namespace cannot be {namespace}; must be either DNS, URL, OID, or X500.")
    else:
        if version in versions:
            sys.exit(f"ERROR: version {version} does not exist")

SAFE = uuid.SafeUUID

print_in_os(f"echo 'uuid={output}' >> $GITHUB_OUTPUT")
print_in_os(f"echo 'safe={SAFE}' >> $GITHUB_OUTPUT")

if SAFE == "unsafe":
    print_in_os("::warning title=UNSAFE::Your UUID may be unsafe for public use because" +
                " it may contain some of your device's personal info.")
