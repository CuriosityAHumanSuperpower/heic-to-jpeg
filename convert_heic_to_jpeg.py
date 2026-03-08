#!/usr/bin/env python3
"""
Convert HEIC images to JPEG format.
Converts all HEIC files from an input folder to JPEG files in an output folder.
"""

import os
import sys
import argparse
from pathlib import Path
from PIL import Image
import pillow_heif

def register_heif_opener():
    """Register HEIF opener with Pillow."""
    pillow_heif.register_heif_opener()

def convert_heic_to_jpeg(input_folder, output_folder, quality=95):
    """
    Convert all HEIC images in input_folder to JPEG in output_folder.
    
    Args:
        input_folder (str): Path to folder containing HEIC images
        output_folder (str): Path to folder where JPEG images will be saved
        quality (int): JPEG quality (1-100, default 95)

    Example : python convert_heic_to_jpeg.py --input_folder "C:\Users\alexa\Desktop\photos" --output_folder "C:\Users\alexa\Desktop\photos\heic-converted-to-jpeg"   
    """
    input_path = Path(input_folder).resolve()
    output_path = Path(output_folder).resolve()
    
    # Create output folder if it doesn't exist
    output_path.mkdir(parents=True, exist_ok=True)
    
    if not input_path.exists():
        print(f"Error: Input folder does not exist: {input_path}")
        return False
    
    if not input_path.is_dir():
        print(f"Error: Input path is not a directory: {input_path}")
        return False
    
    # Find all HEIC files
    heic_files = list(input_path.glob("*.heic")) + list(input_path.glob("*.HEIC"))
    
    if not heic_files:
        print(f"No HEIC files found in: {input_path}")
        return True
    
    print(f"Found {len(heic_files)} HEIC file(s) to convert")
    print(f"Input folder: {input_path}")
    print(f"Output folder: {output_path}")
    print("-" * 50)
    
    converted_count = 0
    failed_count = 0
    
    for heic_file in heic_files:
        try:
            # Open HEIC image
            img = Image.open(heic_file)
            
            # Convert to RGB if necessary (for JPEG compatibility)
            if img.mode in ("RGBA", "LA", "P"):
                # Create white background
                background = Image.new("RGB", img.size, (255, 255, 255))
                background.paste(img, mask=img.split()[-1] if img.mode == "RGBA" else None)
                img = background
            elif img.mode != "RGB":
                img = img.convert("RGB")
            
            # Create output filename
            output_filename = heic_file.stem + ".jpg"
            output_file = output_path / output_filename
            
            # Save as JPEG
            img.save(output_file, "JPEG", quality=quality, optimize=True)
            
            print(f"✓ Converted: {heic_file.name} → {output_filename}")
            converted_count += 1
            
        except Exception as e:
            print(f"✗ Failed to convert {heic_file.name}: {str(e)}")
            failed_count += 1
    
    print("-" * 50)
    print(f"Conversion complete!")
    print(f"  Successful: {converted_count}")
    print(f"  Failed: {failed_count}")
    
    return failed_count == 0

def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Convert HEIC images to JPEG format.")
    parser.add_argument('-i', '--input_folder', default='.', help='Path to folder containing HEIC images')
    parser.add_argument('-o', '--output_folder', default='./heic-converted-to-jpeg', help='Path to folder where JPEG images will be saved')
    parser.add_argument('-q', '--quality', type=int, default=95, help='JPEG quality (1-100)')
    
    args = parser.parse_args()
    
    # Validate quality parameter
    if not 1 <= args.quality <= 100:
        print("Error: Quality must be between 1 and 100")
        sys.exit(1)
    
    # Register HEIF opener
    register_heif_opener()
    
    # Convert images
    success = convert_heic_to_jpeg(args.input_folder, args.output_folder, args.quality)
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
