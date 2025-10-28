import os
import subprocess
import shutil


os.environ["PKG_CONFIG_SYSROOT_DIR"] = (
    "/home/mccakit/dev/sysroots/debian-x64"
)
os.environ["PKG_CONFIG_LIBDIR"] = (
    "/home/mccakit/dev/dev-deps/debian-x64/share/pkgconfig:/home/mccakit/dev/dev-deps/debian-x64/lib/x86_64-linux-gnu/pkgconfig:/home/mccakit/dev/dev-deps/debian-x64/lib/pkgconfig:/home/mccakit/dev/dev-deps/debian-x64/lib/x86_64-linux-gnu/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/share/pkgconfig"
)
os.environ["LD_LIBRARY_PATH"] = (
    "/home/mccakit/dev/libcxx/debian-x64/lib:/home/mccakit/dev/dev-deps/debian-x64/lib:/home/mccakit/dev/dev-deps/debian-x64/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"
)
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
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/debian-x64-autotools-shared.sh && ./configure --prefix=/home/mccakit/dev/dev-deps/debian-x64 --enable-shared --disable-static && make -j11 && make install'",
        shell=True,
        check=True
    )
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64",
            "-DBUILD_SHARED_LIBS=ON",
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("libxml2"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/GNOME/libxml2.git",
        ],
        check=True,
    )
    os.chdir("libxml2")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "-Dicu=enabled",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
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
            "https://github.com/facebook/zstd.git",
        ],
        check=True
    )
    os.chdir("zstd")
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/debian-x64-autotools-shared.sh && make -j11 lib-release && make PREFIX=/home/mccakit/dev/dev-deps/debian-x64 install'",
        shell=True,
        check=True
    )
    subprocess.run("make clean", shell=True)
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64"
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64"
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64",
            "-Dtiff-tools=OFF", "-Dtiff-tests=OFF"
        ],
        check=True
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("wayland"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mccakit/wayland.git",
        ]
    )
    os.chdir("wayland")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "-Dscanner=false",
            "-Dtests=false"
        ], check=True
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("wayland-protocols"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mccakit/wayland-protocols.git",
        ]
    )
    os.chdir("wayland-protocols")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("libffi"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:libffi/libffi.git",
        ]
    )
    os.chdir("libffi")
    subprocess.run(["autoreconf", "-i"], check=True)
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/debian-x64-autotools-shared.sh && ./configure --prefix=/home/mccakit/dev/dev-deps/debian-x64 --enable-shared --disable-static && make -j11 && make install'",
        shell=True,
        check=True,
    )
    subprocess.run("make clean", shell=True, check=True)
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
        "bash -c 'source /home/mccakit/dev/toolchains/debian-x64-autotools-shared.sh && ./configure --prefix=/home/mccakit/dev/dev-deps/debian-x64 --enable-shared --disable-static && make -j11 && make install'",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "-Dglib=enabled",
            "-Dgobject=enabled",
            "-Dicu=enabled",
            "-Dfreetype=enabled",
            "-Dtests=disabled",
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64",
            "-DAJANTV2_DISABLE_TESTS=ON",
            "-DAJANTV2_DISABLE_DEMOS=ON"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
if not os.path.exists("libgudev"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "git@github.com:GNOME/libgudev.git",
        ]
    )
    os.chdir("libgudev")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
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
            "git@github.com:FFmpeg/FFmpeg.git",
        ]
    )
    os.chdir("FFmpeg")
    subprocess.run(
        "bash -c 'source /home/mccakit/dev/toolchains/debian-x64-autotools-shared.sh && ./configure --cc=clang --prefix=/home/mccakit/dev/dev-deps/debian-x64 --enable-shared --disable-static --disable-programs && make -j11 && make install'",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
        "bash -c 'source /home/mccakit/dev/toolchains/debian-x64-autotools-shared.sh && ./configure --disable-tcl --prefix=/home/mccakit/dev/dev-deps/debian-x64 --enable-shared --disable-static && make -j11 && make install'",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "-Denable_tests=false",
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64",
            "-DBUILD_SHARED_LIBS=ON",
            "-DPNG_SHARED=ON",
            "-DPNG_TESTS=OFF",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "-Dglycin=disabled",
            "-Dtests=false",
        ]
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("libxft"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://gitlab.freedesktop.org/xorg/lib/libxft.git",
        ]
    )
    os.chdir("libxft")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
        ],
        check=True,
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "-Dtests=disabled"
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64"
        ],
        check=True,
    )
    subprocess.run(["cmake", "--build", "build", "--parallel"], check=True)
    subprocess.run(["cmake", "--install", "build"], check=True)
    shutil.rmtree("build")
    os.chdir(start_dir)
#needs patch
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
        "bash -c 'source /home/mccakit/dev/toolchains/debian-x64-autotools-shared.sh && ./configure --prefix=/home/mccakit/dev/dev-deps/debian-x64 --enable-shared --disable-static && make -j11 && make install'",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64"
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "-DCMAKE_TOOLCHAIN_FILE=/home/mccakit/dev/toolchains/debian-x64-shared.cmake",
            "-DCMAKE_INSTALL_PREFIX=/home/mccakit/dev/dev-deps/debian-x64"
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
        "bash -c 'source /home/mccakit/dev/toolchains/debian-x64-autotools-shared.sh && ./configure --prefix=/home/mccakit/dev/dev-deps/debian-x64 --enable-shared --disable-static && make -j11 && make install'",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "-Ddevtools=disabled", "-Dgst-examples=disabled", "-Dtools=disabled"
        ]
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
if not os.path.exists("util-linux"):
    subprocess.run(
        [
            "git",
            "clone",
            "--recurse-submodules",
            "--shallow-submodules",
            "--depth",
            "1",
            "https://github.com/mccakit/util-linux.git",
        ]
    )
    os.chdir("util-linux")
    subprocess.run(
        [
            "meson",
            "setup",
            "builddir",
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "-Dbuild-libmount=enabled"
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
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
            "--native-file=/home/mccakit/dev/toolchains/native-meson-shared.ini",
            "--cross-file=/home/mccakit/dev/toolchains/debian-x64-meson-shared.ini",
            "--prefix=/home/mccakit/dev/dev-deps/debian-x64",
            "--reconfigure",
        ],
        check=True,
    )
    subprocess.run(["meson", "compile", "-C", "builddir"], check=True)
    subprocess.run(["meson", "install", "-C", "builddir"], check=True)
    shutil.rmtree("builddir")
    os.chdir(start_dir)
