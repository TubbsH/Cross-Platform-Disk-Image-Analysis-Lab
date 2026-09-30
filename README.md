# Cross-Platform Disk Image Analysis Lab

A digital forensics portfolio project based on coursework analyzing **NTFS** and **Mac HFS/HFSX** forensic images with **FTK Imager** and hex-level file-system interpretation.

## Coursework Focus

This project combines two areas of earlier digital forensics coursework:

- NTFS boot-sector and file-system structure analysis
- Mac OS X Tiger HFS/HFSX image examination with FTK Imager

The goal is to demonstrate the ability to identify file-system structures across different operating systems and interpret low-level forensic metadata.

## Skills Demonstrated

- FTK Imager
- NTFS boot-sector analysis
- HFS/HFSX image examination
- Hexadecimal interpretation
- Endianness
- Sector and cluster calculations
- File-system metadata analysis
- Evidence navigation
- Cross-platform forensic examination
- Technical documentation

## NTFS Concepts Examined

Coursework included decoding:

- OEM ID
- Bytes per sector
- Sectors per cluster
- Bytes per cluster
- Total sector count
- `$MFT` location
- `$MFTMirr` location
- Volume serial number
- Partition offset / LBA
- `55 AA` boot signature

## Mac HFS/HFSX Concepts Examined

Using the `Mac_OS_X4_Tiger.001` forensic image in FTK Imager, coursework included identifying:

- Volume name
- HFS+/HFSX file-system type
- Block / cluster size
- Sector size
- Sector count
- Cluster count
- Primary user
- Documents folder contents
- Desktop folder contents

## Repository Structure

```text
Cross-Platform-Disk-Image-Analysis-Lab/
├── README.md
├── analysis/
│   ├── ntfs-boot-sector.md
│   ├── hfs-image-analysis.md
│   ├── endianness-and-offsets.md
│   └── comparative-findings.md
├── docs/
│   ├── examination-workflow.md
│   └── resume-project-entry.md
├── scripts/
│   └── little_endian_decoder.py
└── sample-data/
    └── example_hex_values.csv
```

## Important Note

This repository documents methods and concepts from coursework. It does not redistribute the original course forensic images.
