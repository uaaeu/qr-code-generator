# QR Code Generator

## Overview
This Python application generates QR codes for any given website link. It's simple to use and customizable, allowing you to specify the version, size, and border of the QR code.

## Requirements
- Python 3.x
- `qrcode` library

## Installation
To use this QR Code Generator, you need to install the `qrcode` library if you haven't already. Run the following command:

```bash
pip install qrcode[pil]
```

## Usage
1. Run the script.
2. Enter the website link when prompted.
3. Specify the QR code version (1-40).
4. Choose the box size for the QR code.
5. Set the border size for the QR code.
After these steps, the QR code will be generated and saved as ‘qr_code.png’ in the current directory.
