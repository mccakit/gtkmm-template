import subprocess
import os
import sys
import shutil

def get_dll_deps(file_path):
    """Get DLL dependencies using llvm-objdump"""
    result = subprocess.run(['llvm-objdump', '-p', file_path],
                          capture_output=True, text=True)
    if result.returncode != 0:
        return []

    deps = []
    for line in result.stdout.split('\n'):
        line = line.strip()
        if 'DLL Name:' in line:
            dll_name = line.split('DLL Name:')[1].strip()
            deps.append(dll_name)

    return deps

def find_dll(dll_name, search_paths):
    """Search for a DLL in given paths"""
    for path in search_paths:
        dll_path = os.path.join(path, dll_name)
        if os.path.isfile(dll_path):
            return dll_path
    return None

def collect_all_deps(file_path, search_paths, seen=None):
    """Recursively collect all DLL dependencies"""
    if seen is None:
        seen = set()

    result = []
    dll_names = get_dll_deps(file_path)

    for dll_name in dll_names:
        if dll_name in seen:
            continue

        dll_path = find_dll(dll_name, search_paths)
        if not dll_path:
            continue

        seen.add(dll_name)
        result.append(dll_path)

        # Recursively get dependencies of this DLL
        result.extend(collect_all_deps(dll_path, search_paths, seen))

    return result

def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <exe_or_dll> <output_folder> [search_path1] [search_path2] ...")
        sys.exit(1)

    target_file = os.path.abspath(sys.argv[1])
    output_folder = os.path.abspath(sys.argv[2])

    if not os.path.isfile(target_file):
        print(f"Error: {target_file} not found")
        sys.exit(1)

    # Create output folder
    os.makedirs(output_folder, exist_ok=True)

    # Default search paths (C++ libs first, then dev-deps, then sysroot)
    search_paths = [
        '/home/mccakit/dev/libcxx/mingw-x64/bin',
        '/home/mccakit/dev/dev-deps/mingw-x64/bin',
        '/home/mccakit/dev/sysroots/llvm-mingw-x64/x86_64-w64-mingw32/bin',
    ]

    # Add user-provided search paths
    if len(sys.argv) > 3:
        search_paths.extend([os.path.abspath(p) for p in sys.argv[3:]])

    print(f"Analyzing: {target_file}")
    print(f"Search paths: {search_paths}")
    print(f"Output folder: {output_folder}\n")

    deps = collect_all_deps(target_file, search_paths)

    if not deps:
        print("No dependencies found")
    else:
        print(f"Found {len(deps)} dependencies:\n")
        for dep in deps:
            dest = os.path.join(output_folder, os.path.basename(dep))
            shutil.copy2(dep, dest)
            print(f"  {dep} -> {dest}")

        print(f"\nDone! Copied {len(deps)} DLLs to {output_folder}")

if __name__ == "__main__":
    main()
