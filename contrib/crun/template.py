pkgname = "crun"
pkgver = "1.8.7"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-systemd"]
# broken presently
configure_gen = []
make_cmd = "gmake"
# full testsuite fails in netns
make_check_target = "tests/tests_libcrun_errors.log"
hostmakedepends = [
    "gmake",
    "go-md2man",
    "pkgconf",
    "python",
]
makedepends = [
    "argp-standalone",
    "libcap-devel",
    "libseccomp-devel",
    # -static for test build from all target
    "libunwind-devel-static",
    "yajl-devel",
]
pkgdesc = "Fast and lightweight OCI runtime"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later AND LGPL-2.1-or-later"
url = "https://github.com/containers/crun"
source = f"{url}/releases/download/{pkgver}/crun-{pkgver}.tar.xz"
sha256 = "6bc96545e1054f36254e7a84dd55c21ac591d17151bc194ec48fc0bd335b1c93"


def post_install(self):
    # useless lib that nothing uses and doesn't even come with headers
    self.rm(self.destdir / "usr/lib/libcrun.a")