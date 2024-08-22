"""Import Operating System and UUID"""
import os
import uuid

version = os.environ.get("INPUTS_UUID")
namespace = os.environ.get("INPUTS_NAMESPACE")

versions = [1, 3, 4, 5]

if version >= 1 or version <= 8:
  if version == 1:
    output = uuid.uuid1()
  else:
    if version == 2:
      output = uuid.uuid2()
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
            if version == 6:
              output = uuid.uuid6()
            else:
              if version == 7:
                output = uuid.uuid7()
              else:
                if version == 8:
                  output = uuid.uuid8()
else:
  exit(f"ERROR: version {version} does not exist")

output = str(output)
print(f"::set-output name=uuid::{output}")
