import os
import subprocess
import shutil
import urllib.request
import zipfile

os.environ["PKG_CONFIG_SYSROOT_DIR"] = (
    "/home/mccakit/dev/sysroots/llvm-mingw-x64/x86_64-w64-mingw32"
)
os.environ["PKG_CONFIG_LIBDIR"] = (
    "/home/mccakit/dev/dev-deps/mingw-x64/lib/pkgconfig"
)
os.environ["LD_LIBRARY_PATH"] = (
    "/home/mccakit/dev/libcxx/mingw-x64/lib:/home/mccakit/dev/dev-deps/mingw-x64/lib/pkgconfig"
)
os.environ["VULKAN_SDK"] = "/home/mccakit/dev/sysroots/VulkanSDK/Windows/1.4.313.1"
start_dir = os.getcwd()
if not os.path.exists("icu"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:unicode-org/icu.git",
        ]
    )
    os.chdir("icu/icu4c/source")
    os.mkdir("native")
    os.chdir("native")
    subprocess.run(
        "bash -c 'export LD_LIBRARY_PATH=/home/mccakit/dev/libcxx/native/lib && source /home/mccakit/dev/toolchains/native-autotools-shared.sh && ../configure --prefix=/home/mccakit/dev/dev-deps/mingw-x64 --enable-shared --disable-static && make -j11'",
        shell=True,
        check=True
    )
    os.chdir("../")
    abs_native = os.path.abspath("native")
    subprocess.run(
        f"bash -c 'export LD_LIBRARY_PATH=/home/mccakit/dev/libcxx/native/lib && source /home/mccakit/dev/toolchains/mingw-x64-autotools-shared.sh && ./configure --host=x86_64-w64-mingw32 --with-cross-build={abs_native} --prefix=/home/mccakit/dev/dev-deps/mingw-x64 --enable-shared --disable-static && make -j11 && make install'",
        shell=True,
        check=True
    )
    subprocess.run("make clean", shell=True, check=True)
    os.chdir("native")
    subprocess.run("make clean", shell=True, check=True)
    os.chdir(start_dir)
if not os.path.exists("xz"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/tukaani-project/xz.git",
        ],
        check=True,
    )
    os.chdir("xz")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
#libiconv needs binaries
if not os.path.exists("libxml2"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mccakit/libxml2.git",
        ],
        check=True,
    )
    os.chdir("libxml2")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64",
            "-DLIBXML2_WITH_ICU=ON"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("zstd"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mccakit/zstd.git",
        ],
        check=True
    )
    os.chdir("zstd/build/cmake")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("libdeflate"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/ebiggers/libdeflate.git",
        ]
    )
    os.chdir("libdeflate")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64"
        ],
        check=True
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("libwebp"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mccakit/libwebp.git"
        ]
    )
    os.chdir("libwebp")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64"
        ],
        check=True
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("libtiff"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://gitlab.com/libtiff/libtiff.git",
        ]
    )
    os.chdir("libtiff")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dtiff-tools=OFF", "-Dtiff-tests=OFF"
        ],
        check=True
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
#libffi needs binaries
if not os.path.exists("zlib"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/madler/zlib.git",
        ],
        check=True,
    )
    os.chdir("zlib")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("pcre2"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:PCRE2Project/pcre2.git",
        ]
    )
    os.chdir("pcre2")
    subprocess.run(["autoreconf", "-i"], check=True)
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/mingw-x64-autotools-shared.sh && ./configure --host=x86_64-w64-mingw32 --prefix=/home/mccakit/dev/dev-deps/mingw-x64 --enable-shared --disable-static && make -j11 && make install'",
        shell=True,
        check=True,
    )
    subprocess.run("make clean", shell=True)
    os.chdir(start_dir)
if not os.path.exists("glib"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/glib.git",
        ]
    )
    os.chdir("glib")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("libjpeg-turbo"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:libjpeg-turbo/libjpeg-turbo.git",
        ]
    )
    os.chdir("libjpeg-turbo")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64",
            "-DENABLE_SHARED=ON"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("freetype"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:freetype/freetype.git",
        ]
    )
    os.chdir("freetype")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("harfbuzz"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:harfbuzz/harfbuzz.git",
        ]
    )
    os.chdir("harfbuzz")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dglib=enabled",
            "-Dgobject=enabled",
            "-Dicu=enabled",
            "-Dfreetype=enabled",
            "-Dtests=disabled",
            "-Ddocs=disabled"
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("libajantv2"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/libajantv2.git",
        ]
    )
    os.chdir("libajantv2")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64",
            "-DAJANTV2_DISABLE_TESTS=ON",
            "-DAJANTV2_DISABLE_DEMOS=ON"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("FFmpeg"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/FFmpeg.git",
        ]
    )
    os.chdir("FFmpeg")
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/mingw-x64-autotools-shared.sh && ./configure --enable-cross-compile --arch=x86_64 --target-os=mingw32 --cc=clang --as=clang --nm=llvm-nm --ar=llvm-ar --prefix=/home/mccakit/dev/dev-deps/mingw-x64 --enable-shared --disable-static --disable-programs --disable-decoder=mlp --disable-encoder=mlp --disable-parser=mlp --disable-demuxer=mlp && make -j11 && make install'",
        shell=True,
        check=True,
    )
    subprocess.run("make clean", shell=True, check=True)
    os.chdir(start_dir)
if not os.path.exists("fontconfig"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:arthenica/fontconfig.git",
        ]
    )
    os.chdir("fontconfig")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dtests=disabled",
            "-Ddoc=disabled",
        ]
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("orc"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://gitlab.freedesktop.org/gstreamer/orc.git",
        ]
    )
    os.chdir("orc")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dtests=disabled", "-Dgst-plugins-base:xvideo=disabled"
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("fdk-aac"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/fdk-aac.git",
        ]
    )
    os.chdir("fdk-aac")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64",
            "-DBUILD_SHARED_LIBS=ON",
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("openh264"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/openh264.git",
        ]
    )
    os.chdir("openh264")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dtests=disabled",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("sqlite"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:sqlite/sqlite.git",
        ]
    )
    os.chdir("sqlite")
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/mingw-x64-autotools-shared.sh && ./configure --host=x86_64-w64-mingw32 --disable-tcl --prefix=/home/mccakit/dev/dev-deps/mingw-x64 --enable-shared --disable-static && make -j11 && make install'",
        shell=True,
        check=True,
    )
    subprocess.run("make clean", shell=True, check=True)
    os.chdir(start_dir)
if not os.path.exists("dav1d"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://code.videolan.org/videolan/dav1d.git",
        ]
    )
    os.chdir("dav1d")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Denable_tests=false"
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("libpng"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:pnggroup/libpng.git",
        ]
    )
    os.chdir("libpng")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64"
            "-DBUILD_SHARED_LIBS=ON",
            "-DPNG_SHARED=ON",
            "-DPNG_TESTS=OFF"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("gdk-pixbuf"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/GNOME/gdk-pixbuf.git",
        ]
    )
    os.chdir("gdk-pixbuf")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dglycin=disabled",
            "-Dtests=false",
        ]
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("lerc"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:Esri/lerc.git",
        ]
    )
    os.chdir("lerc")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64",
            "-DBUILD_SHARED_LIBS=ON",
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("cairo"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://gitlab.com/saiwp/cairo.git",
        ]
    )
    os.chdir("cairo")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dtests=disabled"
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("fribidi"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/fribidi/fribidi.git",
        ]
    )
    os.chdir("fribidi")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Ddocs=false", "-Dbin=false", "-Dtests=false"
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("pango"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/GNOME/pango.git",
        ]
    )
    os.chdir("pango")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dbuild-testsuite=false",
            "-Dbuild-examples=false",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("librsvg"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/librsvg.git",
        ]
    )
    os.chdir("librsvg")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Drsvg-convert=disabled",
            "-Dtests=false",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("libvpx"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://gitlab.freedesktop.org/gstreamer/meson-ports/libvpx.git",
        ]
    )
    os.chdir("libvpx")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dtools=disabled"
        ]
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("aom"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://aomedia.googlesource.com/aom",
        ]
    )
    os.chdir("aom")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64",
            "-DENABLE_TESTS=OFF"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("nettle"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://git.lysator.liu.se/nettle/nettle.git",
        ]
    )
    os.chdir("nettle")
    subprocess.run(["autoreconf", "-i"], check=True)
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/mingw-x64-autotools-shared.sh && ./configure --host=x86_64-w64-mingw32 --prefix=/home/mccakit/dev/dev-deps/mingw-x64 --enable-shared --disable-static && make -j11 && make install'",
        shell=True,
        check=True,
    )
    subprocess.run("make clean", shell=True, check=True)
    os.chdir(start_dir)
if not os.path.exists("libpsl"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/rockdaboot/libpsl.git",
        ]
    )
    os.chdir("libpsl")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dtests=false"
        ]
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("libssh2"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/libssh2/libssh2.git",
        ]
    )
    os.chdir("libssh2")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("curl"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/curl/curl.git",
        ]
    )
    os.chdir("curl")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64",
            "-DBUILD_CURL_EXE=OFF"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("Little-CMS"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mm2/Little-CMS.git",
        ]
    )
    os.chdir("Little-CMS")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dtests=disabled"
        ]
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("libde265"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/strukturag/libde265.git",
        ]
    )
    os.chdir("libde265")
    subprocess.run(
        [
            "cmake",
            "-B",
            "build",
            "-G",
            "Ninja",
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/mingw-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/mingw-x64"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("libusb"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/libusb/libusb.git",
        ]
    )
    os.chdir("libusb")
    subprocess.run(["autoreconf", "-i"], check=True)
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/mingw-x64-autotools-shared.sh && ./configure --host=x86_64-w64-mingw32 --prefix=/home/mccakit/dev/dev-deps/mingw-x64 --enable-shared --disable-static && make -j11 && make install'",
        shell=True,
        check=True,
    )
    subprocess.run("make clean", shell=True, check=True)
    os.chdir(start_dir)
if not os.path.exists("gstreamer"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/gstreamer.git",
        ]
    )
    os.chdir("gstreamer")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Ddevtools=disabled", "-Dgst-examples=disabled", "-Dtools=disabled"
        ]
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("gtk"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mccakit/gtk.git",
        ]
    )
    os.chdir("gtk")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("glibmm"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/glibmm.git",
        ]
    )
    os.chdir("glibmm")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("cairomm"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mccakit/cairomm.git",
        ]
    )
    os.chdir("cairomm")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "-Dbuild-examples=false", "-Dbuild-tests=false"
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("pangomm"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/pangomm.git",
        ]
    )
    os.chdir("pangomm")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("gtkmm"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:mccakit/gtkmm.git",
        ]
    )
    os.chdir("gtkmm")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-static.ini",
            "--cross-file=/home/mccakit/dev/toolchains/mingw-x64-shared-meson.ini",
            "--prefix=/home/mccakit/dev/dev-deps/mingw-x64",
            "--reconfigure",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
