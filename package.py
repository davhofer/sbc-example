# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PySbcExample(PythonPackage):
    """A minimal example scikit-build-core package (with pybind11)"""

    # FIXME: add homepage
    # homepage = ""
    url = "https://api.github.com/repos/davhofer/sbc-example/tarball/v0.0.1"
    git = "https://github.com/davhofer/sbc-example.git"

    # FIXME: check license
    license("MIT License")

    # FIXME: add github names for maintainers
    # maintainers("...")
    # Authors:
    # My Name, me@email.com

    version("0.0.1", sha256="fe0358e21b81eb6e7bd263e6e3e9c640fc18fd5cb488f3b4a2d858c1aed773d9")

    variant("test", default=False)

    with default_args(type="build"):
        depends_on("py-pybind11")
        depends_on("py-scikit-build-core")

    with default_args(type=("build", "run")):
        depends_on("python@3.7:")
        depends_on("py-pytest", when="+test")


