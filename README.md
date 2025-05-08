# zlib-ng Builds

This repository contains pre-built zlib-ng packages for various Linux distributions. zlib-ng is a zlib replacement with optimizations for "next generation" systems.

## 🎯 Features

- Pre-compiled zlib-ng packages
- Multiple distribution support
- Automated builds via GitHub Actions
- JSON metadata for automated installations
- Optimized for MediaEase applications

## 📦 Supported Versions

| Version | Debian 11 | Ubuntu 22 | Debian 12 | Ubuntu 24 |
|---------|-----------|-----------|-----------|-----------|
| 2.0.0   | ✅        | ✅        | ✅        | ✅        |
| 2.1.5   | ✅        | ✅        | ✅        | ✅        |
| 2.2.4   | ✅        | ✅        | ✅        | ✅        |

## 📋 Installation

### Manual Installation
1. Download the appropriate .deb package for your distribution
2. Install using: `sudo dpkg -i package_name.deb`
3. Fix any dependencies if needed: `sudo apt-get install -f`

## 🔍 Package Details

The packages include:
- zlib-ng library
- Development files
- System-wide installation in `/usr`

## 📄 Metadata

Each package is accompanied by its JSON metadata file containing:
- Package information
- Checksums
- Dependencies
- Build configuration
- Distribution details

## 📝 License

zlib-ng is distributed under the [zlib License](https://github.com/zlib-ng/zlib-ng/blob/develop/LICENSE.md). 
