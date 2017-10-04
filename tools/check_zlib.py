#! env python3
# license: Apatch 2.0
import sys
import os
import tempfile

src = """#include <zlib.h>

void main() {
    const char* ver = zlib_version;
}
"""
fd, fname = tempfile.mkstemp(suffix=".c", text=True)
with open(fname, "w") as fp:
    fp.write(src)
os.close(fd)

ret = os.system("gcc -lz %s" % fname)
os.remove(fname)
if ret != 0:
    sys.exit(1)
sys.exit(0)
# vi: ft=python
