- To build, 'source get-gtk.sh', then run cmake, then copy deps with python to a folder named lib, put the binary in the bin folder.

- To build gtkmm, first build gtk, then gtkmm then replace system libs until libstdc++ dependency is gone

- If you have issue with version mismatches, use -force-fallback-for option in meson

- I recommend using the latest version of meson, and an llvm toolchain.
