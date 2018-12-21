#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
"""
Build manifest for the Ncurses library and it's headers
"""

from textwrap import dedent
import nbuild

NCURSES_VERSION = '6.1'


@nbuild.package(
    id=f'stable::sys-lib/ncurses#{NCURSES_VERSION}.0',
    description=dedent('''
        Shared library providing an API for text-based user interfaces in a
        terminal-independant manner.
    '''),
)
def build_ncurses():
    nbuild
    package = nbuild.current_build().current_package
    nbuild.build_autotools_package(
        configure=lambda: nbuild.do_configure(
            extra_configure_flags=[
                '--with-shared',
                '--with-normal',
                '--without-debug',
            ]
        ),
        fetch=lambda: nbuild.fetch_urls([
            {
                'url': f'ftp://ftp.invisible-island.net/ncurses/ncurses-{NCURSES_VERSION}.tar.gz',
                'sha256': 'aa057eeeb4a14d470101eff4597d5833dcef5965331be3528c08d99cebaa0d17',
            },
        ]),
        install=lambda: nbuild.do_make(
            target='',
            extra_args=['install.progs', 'install.libs', 'install.data', 'install.man', f'DESTDIR={package.install_dir}'],
        )
    )
    # Exclude these directories (keep them for ncurses-dev)
    nbuild.exclude_dirs('/usr/include', '/usr/share/man/man3')


@nbuild.package(
    id=f'stable::sys-lib/ncurses-dev#{NCURSES_VERSION}.0',
    description=dedent('''
        Headers and manuals to write or compile softwares based on the ncurses library.
    '''),
    run_dependencies={
        'stable::sys-lib/ncurses': f'={NCURSES_VERSION}.0',
    },
)
def build_ncurses_dev():
    package = nbuild.current_build().current_package

    nbuild.build_autotools_package(
        configure=None,
        install=lambda: nbuild.do_make(
            target='',
            extra_args=['install.includes', 'install.man', f'DESTDIR={package.install_dir}'],
        )
    )
    # We don't want the other mans, they are provided by the main package.
    nbuild.keep_only('man3', base='/usr/share/man')
