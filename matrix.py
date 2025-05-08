#!/usr/bin/env python3

import yaml

# Define the matrix for building zlib-ng
matrix = []

# Define versions to build
versions = ["2.0.0", "2.1.5", "2.2.4"]

# Define distributions to build for
distributions = [
    "debian-11",
    "ubuntu-22.04",
    "debian-12",
    "ubuntu-24.04"
]

# Generate matrix entries
for version in versions:
    for distro in distributions:
        matrix.append({
            "version": version,
            "os": distro
        })

# Output the matrix in GitHub Actions compatible format
print(yaml.safe_dump({"include": matrix}, sort_keys=False))
