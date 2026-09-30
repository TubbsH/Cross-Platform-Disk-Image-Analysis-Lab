# Examination Workflow

## NTFS Image

1. Open the image in FTK Imager or a hex-capable forensic tool.
2. Locate the NTFS boot sector.
3. Record OEM ID.
4. Decode bytes per sector.
5. Decode sectors per cluster.
6. Calculate bytes per cluster.
7. Decode total sectors.
8. Identify `$MFT` and `$MFTMirr` starting clusters.
9. Record the volume serial number.
10. Confirm the `55 AA` boot signature.

## Mac HFS/HFSX Image

1. Add the forensic image to FTK Imager.
2. Identify the volume and file-system type.
3. Record sector and block information.
4. Navigate the root and user directories.
5. Identify the primary user.
6. Review Documents and Desktop contents.
7. Record observations and screenshots.
8. Preserve the original image unchanged.
