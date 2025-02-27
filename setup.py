# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import os
from typing import List

from setuptools import find_packages, setup
from torchsnapshot import __version__


def current_path(file_name: str) -> str:
    return os.path.abspath(os.path.join(__file__, os.path.pardir, file_name))


def read_requirements(file_name: str) -> List[str]:
    with open(current_path(file_name), encoding="utf8") as f:
        return f.read().strip().split()


if __name__ == "__main__":
    with open(current_path("README.md"), encoding="utf8") as f:
        readme: str = f.read()

    setup(
        name="torchsnapshot",
        version=__version__,
        author="torchsnapshot team",
        author_email="yifu@fb.com",
        description="A library for persisting PyTorch program state",
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://github.com/facebookresearch/torchsnapshot",
        license="BSD-3",
        keywords=["pytorch", "snapshot", "checkpoint"],
        python_requires=">=3.7",
        install_requires=read_requirements("requirements.txt"),
        packages=find_packages(exclude=("examples", "benchmarks")),
        zip_safe=True,
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
        extras_require={"dev": read_requirements("dev-requirements.txt")},
    )
