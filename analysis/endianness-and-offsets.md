# Endianness and Offset Interpretation

Low-level file-system analysis requires careful interpretation of byte order and offsets.

In NTFS exercises, multi-byte values were commonly stored in little-endian format. For example, a raw byte sequence such as:

`00 02`

must be interpreted as:

`0x0200 = 512`

when decoded as little endian.

Hex offsets were also used to locate fields within the boot sector and relate raw disk positions to file-system metadata.

Understanding endianness helps prevent one of the most common mistakes in manual disk analysis: reading the correct bytes but interpreting their numeric value incorrectly.
