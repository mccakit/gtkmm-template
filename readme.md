EXAMPLE

.. code-block:: bash

   EXAMPLE
   export PKG_CONFIG_LIBDIR="/home/mccakit/dev/dev-deps/native/share/pkgconfig:/home/mccakit/dev/dev-deps/native/lib/x86_64-linux-gnu/pkgconfig:/home/mccakit/dev/dev-deps/native/lib/pkgconfig:/home/mccakit/dev/dev-deps/native/lib/x86_64-linux-gnu/pkgconfig:/usr/lib/x86_64-linux-gnu/pkgconfig:/usr/share/pkgconfig"
   export LD_LIBRARY_PATH="/home/mccakit/dev/libcxx/native/lib:/home/mccakit/dev/dev-deps/native/lib:/home/mccakit/dev/dev-deps/native/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"
   cmake -B build -G Ninja -DCMAKE_TOOLCHAIN_FILE=$HOME/dev/toolchains/native-shared.cmake
   source $HOME/dev/pyvenv/bin/activate
   python3 ./copy_deps.py ./build/main ./output
   mkdir -p ./output/bin
   cp ./build/main ./output/bin/main
