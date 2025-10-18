#!/usr/bin/env python3
import subprocess
import os
import shutil
import sys

def get_deps(lib_path):
    result = subprocess.run(['ldd', lib_path], capture_output=True, text=True)
    if result.returncode != 0:
        return []
    deps = []
    for line in result.stdout.split('\n'):
        if '=>' not in line:
            continue
        parts = line.split('=>')
        if len(parts) != 2:
            continue
        path = parts[1].strip().split()[0]
        if path.startswith('(') or path == 'not' or not os.path.isfile(path):
            continue
        deps.append(path)
    return deps

def is_system_lib(path):
    return path.startswith('/lib') or path.startswith('/usr/lib')

def collect_deps(lib_path, seen=None):
    if seen is None:
        seen = set()
    result = []
    for dep in get_deps(lib_path):
        if dep in seen or is_system_lib(dep):
            continue
        seen.add(dep)
        result.append(dep)
        result.extend(collect_deps(dep, seen))
    return result

def patch_rpath(file_path):
    subprocess.run(['patchelf', '--set-rpath', '.:$ORIGIN', file_path],
                  capture_output=True)

def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    binary = os.path.abspath(sys.argv[1])
    output_dir = os.path.abspath(sys.argv[2] if len(sys.argv) > 2 else "lib")

    if not os.path.isfile(binary):
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    deps = collect_deps(binary)
    for dep in deps:
        dest = os.path.join(output_dir, os.path.basename(dep))
        shutil.copy2(dep, dest)

    for filename in os.listdir(output_dir):
        if '.so' in filename:
            patch_rpath(os.path.join(output_dir, filename))

if __name__ == "__main__":
    main()
