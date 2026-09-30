#!/usr/bin/env python3
"""Decode a little-endian hexadecimal byte sequence."""

import argparse

def decode_little_endian(hex_bytes: str) -> int:
    cleaned = hex_bytes.replace(" ", "").replace("0x", "")
    if len(cleaned) % 2:
        raise ValueError("Hex input must contain complete bytes.")
    raw = bytes.fromhex(cleaned)
    return int.from_bytes(raw, byteorder="little")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("hex_bytes", help='Example: "00 02"')
    args = parser.parse_args()

    value = decode_little_endian(args.hex_bytes)
    print(f"Decimal: {value}")
    print(f"Hex: 0x{value:X}")

if __name__ == "__main__":
    main()
