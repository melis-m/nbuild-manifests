import stdlib
import stdlib.build
from stdlib.template import autotools
from stdlib.template.configure import configure
from stdlib.manifest import manifest
from stdlib.split.drain_all import drain_all


@manifest(
    name='pulseaudio',
    category='sys-apps',
    description='''
    PulseAudio is a sound system for POSIX OSes, meaning that it is a proxy for your sound applications.
    ''',
    tags=['sound'],
    maintainer='matteo.melis@epitech.eu',
    licenses=[stdlib.license.License.LGPL],
    upstream_url='https://www.freedesktop.org/wiki/Software/PulseAudio/',
    kind=stdlib.kind.Kind.EFFECTIVE,
    versions_data=[
        {
            'semver': '13.0.0',
            'fetch': [{
                    'url': 'https://www.freedesktop.org/software/pulseaudio/releases/pulseaudio-13.0.tar.xz',
                    'sha256': '961b23ca1acfd28f2bc87414c27bb40e12436efcf2158d29721b1e89f3f28057',
                },
            ],
        },
    ],
    build_dependencies=[
        'sys-libs/libtool-dev',
        'sys-libs/libsndfile-dev',
        'sys-libs/libspeexdsp-dev',
        'sys-libs/openssl-dev',
        'dev-libs/json-c-dev',
        'dev-apps/gettext',
        'sys-apps/dbus-dev',
        'sys-apps/systemd-dev',
    ]
)
def build(build):
    packages = autotools.build(
            configure=lambda: configure(
                '--without-caps',
                '--disable-manpages',
            ),
    )
    return packages

