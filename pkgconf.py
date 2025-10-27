#!/home/mccakit/dev/python/bin/python3
import os
import subprocess
import sys

sysroot = os.environ.get("PKG_CONFIG_SYSROOT_DIR")
cmd = ["pkgconf"] + sys.argv[1:]
cin = subprocess.run(cmd, capture_output=True, text=True, check=True).stdout
flags = [flag.strip() for flag in cin.split(" ")]
output = ""

flags = [flag.strip() for flag in cin.split(" ") if flag.strip()]
output = ""

for flag in flags:
    if flag.startswith('-I') or flag.startswith('-L'):
        path = flag[2:]
    else:
        path = flag

    # Only attempt to remove sysroot if it's defined and the path doesn't exist
    if sysroot and not os.path.exists(path):
        flag = flag.replace(sysroot, "")

    output += flag + " "

print(output.strip())
