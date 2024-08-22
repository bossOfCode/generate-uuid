"""Import Operating System and UUID"""
import os
import uuid

version = os.environ.get("INPUTS_UUID")

if version >= 1 or version <= 8:
  if version = 1:
    output = uuid.uuid1()
    break
  else:
    if version = 2:
      output = uuid.uuid2()
      break
    else:
      if version = 3:
        output = uuid.uuid3()
        break
      else:
        if version = 4:
          output = uuid.uuid4()
          break
        else:
          if version = 5:
            output = uuid.uuid5()
            break
          else:
            if version = 6:
              output = uuid.uuid6()
              break
            else:
              if version = 7:
                output = uuid.uuid7()
                break
              else:
                if version = 8:
                  output = uuid.uuid8()
                  break
else:
  exit(f"ERROR: version {version} does not exist")

output = str(output)
print(f"::set-output name=uuid::{output}")
