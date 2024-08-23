"""Import Operating System and UUID"""
import os
import sys
import uuid

VERSION = os.environ.get("INPUT_VERSION")
namespace = os.environ.get("INPUT_NAMESPACE")
name = os.environ.get("INPUT_NAME")

OUTPUT = ""
VERSION = getattr(uuid, f"uuid{VERSION}")

versions = ["uuid1", "uuid3", "uuid4", "uuid5"]
namespaces = ["DNS", "URL", "OID", "X500"]

def print_in_os(argument):
    "print in both terminal and action logs"
    print(f"{argument}")
    os.system(f"{argument}")

print_in_os(f"Version: {VERSION}")

if VERSION in versions or namespace in namespaces:
    OUTPUT = str(VERSION())
else:
    if namespace in namespaces:
        sys.exit(f"ERROR: namespace cannot be {namespace}; must be either DNS, URL, OID, or X500.")
    else:
        if VERSION in versions:
            sys.exit(f"ERROR: VERSION {VERSION} does not exist")

SAFE = uuid.SafeUUID

print_in_os(f"echo 'uuid={OUTPUT}' >> $GITHUB_OUTPUT")
print_in_os(f"echo 'safe={str(SAFE)}' >> $GITHUB_OUTPUT")

if SAFE == "unsafe":
    print_in_os("::warning title=UNSAFE::Your UUID may be unsafe for public use because" +
                " it may contain some of your device's personal info.")
