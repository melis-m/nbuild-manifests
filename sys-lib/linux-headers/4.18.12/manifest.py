from nbuild.cmd import cmd
from nbuild.log import ilog
from nbuild.stdenv.package import package, get_package
from nbuild.stdenv.fetch import fetch_url
from nbuild.stdenv.extract import extract_tarballs
from nbuild.stdenv.autotools.make import do_make


@package(
    id="stable::sys-lib/linux-headers#4.18.12",
    run_dependencies={
        "stable::kernel/linux": ">=4.18.12",
    },
)
def build_linux_header():
    package = get_package()

    ilog("Step 1/3: Fetch kernel sources", indent=False)
    fetch_url(
            url=f"https://www.kernel.org/pub/linux/kernel/v4.x/linux-{package.version}.tar.xz",
            sha256="846a5ad9cbe576f66aeeb188c9bd45d14eee0783aebfc4ea853dac09a7159fc5",
        ),

    ilog("Step 2/4: Extract kernel sources", indent=False)
    extract_tarballs()

    ilog("Step 3/4: Install kernel headers", indent=False)
    do_make(
        target="headers_install",
        extra_args=[f'INSTALL_HDR_PATH={package.install_dir}/usr/'],
    )

    ilog("Step 4/4: Remove useless files", indent=False)
    cmd(f'find {package.install_dir} \\( -name .install -o -name ..install.cmd \\) -delete')
