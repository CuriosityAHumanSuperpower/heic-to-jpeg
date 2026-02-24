# HEIC to JPEG Converter

A Python script to convert HEIC images to JPEG format in batch.

## Features

- Converts all HEIC images in a folder to JPEG format
- Customizable input and output folders
- Adjustable JPEG quality (default: 95)
- Handles transparency by adding white background
- Progress reporting

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic usage (current directory as input):
```bash
python convert_heic_to_jpeg.py
```
This will:
- Search for HEIC files in the current directory
- Save JPEG files to `./heic-converted-to-jpeg/`

### Custom input folder:
```bash
python convert_heic_to_jpeg.py /path/to/input
```

### Custom input and output folders:
```bash
python convert_heic_to_jpeg.py /path/to/input /path/to/output
```

### Custom input, output, and quality:
```bash
python convert_heic_to_jpeg.py /path/to/input /path/to/output 90
```

## Command Line Arguments

1. **Input folder** (optional): Path to folder containing HEIC files
   - Default: Current directory (`.`)

2. **Output folder** (optional): Path to folder where JPEG files will be saved
   - Default: `./heic-converted-to-jpeg/`

3. **Quality** (optional): JPEG quality level (1-100)
   - Default: `95`

## Examples

```bash
# Convert HEIC files from current directory
python convert_heic_to_jpeg.py

# Convert from specific input folder, use default output folder
python convert_heic_to_jpeg.py "./input"

# Convert with custom input and output folders
python convert_heic_to_jpeg.py "./input" "./output"

# Convert with custom quality (lower = smaller file, worse quality)
python convert_heic_to_jpeg.py "./input" "./output" 85
```

## Requirements

- Python 3.6+
- Pillow (PIL)
- pillow-heif (for HEIC support)

## Notes

- The script automatically creates the output folder if it doesn't exist
- Transparent images (PNG, RGBA) are composited onto a white background for JPEG compatibility
- The script is case-insensitive for .heic and .HEIC files
- Original HEIC files are not modified
