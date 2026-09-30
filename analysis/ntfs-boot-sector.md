# NTFS Boot Sector Analysis

The NTFS coursework focused on extracting and interpreting key volume parameters directly from the boot sector.

Important fields included:

- OEM ID
- Bytes per sector
- Sectors per cluster
- Total sectors
- `$MFT` cluster location
- `$MFTMirr` cluster location
- Volume serial number
- Boot-sector signature

Many NTFS numeric fields are stored in little-endian format, so the raw bytes must be reversed before conversion to decimal.

The lab reinforced the importance of validating graphical tool output with the underlying on-disk structure.
