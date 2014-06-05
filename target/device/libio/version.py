import sys
import re
fileName = sys.argv[1]

# Get version number
fp = open(fileName, "r")
version = fp.readline();
version = re.match("\d+\.\d+\.\d+", version).group()
fp.close
print version

# Generate version.h
fp = open("./src/version.h", "w+")
fp.write("extern char *version();")
fp.close()

# Generate version.cpp
fp = open("./src/version.cpp", "w+")
s = '''char *version() {
  return "%s";
}''' %(version)
fp.write(s)
fp.close()

# Generate version_export.h
fp = open("./export/version_export.h", "w+")
fp.write("extern char *version_addon();")
fp.close()

# Generate version_export.cpp
fp = open("./export/version_export.cpp", "w+")
s = '''char *version_addon() {
  return "%s";
}''' %(version)
fp.write(s)
fp.close()
