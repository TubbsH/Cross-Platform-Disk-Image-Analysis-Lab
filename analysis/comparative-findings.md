# Comparative Findings

The NTFS and HFS/HFSX labs highlight important differences and similarities between Windows and macOS forensic examination.

## Similarities

- Both require interpretation of volume metadata.
- Both depend on sector/block sizing for correct navigation.
- Both can be examined through forensic image tools such as FTK Imager.
- Both benefit from verification at the raw-hex level.

## Differences

- NTFS places strong emphasis on structures such as the `$MFT` and `$MFTMirr`.
- HFS/HFSX uses different volume structures and terminology.
- File-system metadata layouts and endianness conventions vary.

The major lesson from the coursework was that a forensic examiner should understand underlying file-system structures rather than depend exclusively on one tool's graphical interface.
