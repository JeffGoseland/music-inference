#!/usr/bin/env python3
"""
DEAM MP3 to WAV Converter

Converts MP3 files from the MEMD_audio folder to WAV format for easier processing.
Creates a wav/ folder in the same directory as the source files.

Author: Jeff Goseland
Date: 2025
"""

import os
import glob
from pathlib import Path
from pydub import AudioSegment
import librosa
import numpy as np

def convert_mp3_to_wav(mp3_path, wav_path):
    """
    convert a single MP3 file to WAV format
    
    Args:
        mp3_path: path to the input MP3 file
        wav_path: path for the output WAV file
    """
    try:
        # check if input file exists
        if not Path(mp3_path).exists():
            print(f"✗ Error: Input file not found: {Path(mp3_path).name}")
            return False
        
        # load MP3 using pydub
        audio = AudioSegment.from_mp3(mp3_path)
        
        # export to WAV format
        audio.export(wav_path, format="wav")
        
        # verify the conversion by loading with librosa
        y, sr = librosa.load(wav_path)
        
        print(f"✓ Converted: {Path(mp3_path).name} -> {Path(wav_path).name}")
        print(f"  Duration: {len(y)/sr:.2f}s, Sample rate: {sr}Hz")
        
        return True
        
    except Exception as e:
        print(f"✗ Error converting {Path(mp3_path).name}: {e}")
        # remove partial file if it exists
        if Path(wav_path).exists():
            try:
                Path(wav_path).unlink()
                print(f"  Removed partial file: {Path(wav_path).name}")
            except:
                pass
        return False

def convert_all_mp3_files(force_overwrite=False):
    """
    convert all MP3 files in the MEMD_audio folder to WAV format
    
    Args:
        force_overwrite: if True, overwrite existing WAV files
    """
    # define paths
    memd_audio_dir = Path("../data/DEAM/MEMD_audio")
    wav_dir = memd_audio_dir / "wav"
    
    # check if source directory exists
    if not memd_audio_dir.exists():
        print(f"Error: MEMD_audio directory not found at {memd_audio_dir}")
        return
    
    # create wav directory if it doesn't exist
    wav_dir.mkdir(exist_ok=True)
    print(f"Created WAV output directory: {wav_dir}")
    
    # get all MP3 files
    mp3_files = sorted(glob.glob(str(memd_audio_dir / "*.mp3")))
    
    if not mp3_files:
        print("No MP3 files found in MEMD_audio directory")
        return
    
    print(f"Found {len(mp3_files)} MP3 files to convert")
    if force_overwrite:
        print("Force overwrite mode: will overwrite existing WAV files")
    print("=" * 50)
    
    # convert each file
    successful_conversions = 0
    failed_conversions = 0
    skipped_conversions = 0
    
    for mp3_file in mp3_files:
        mp3_path = Path(mp3_file)
        wav_filename = mp3_path.stem + ".wav"
        wav_path = wav_dir / wav_filename
        
        # check if WAV file already exists
        if wav_path.exists() and not force_overwrite:
            print(f"⏭ Skipped (already exists): {wav_filename}")
            skipped_conversions += 1
            continue
        
        # convert the file
        if convert_mp3_to_wav(mp3_path, wav_path):
            successful_conversions += 1
        else:
            failed_conversions += 1
    
    # print summary
    print("=" * 50)
    print(f"Conversion complete!")
    print(f"Successful: {successful_conversions}")
    print(f"Failed: {failed_conversions}")
    print(f"Skipped: {skipped_conversions}")
    print(f"Total: {len(mp3_files)}")
    print(f"WAV files saved to: {wav_dir}")

def main():
    """main function to run the MP3 to WAV conversion"""
    import sys
    
    print("DEAM MP3 to WAV Converter")
    print("=" * 50)
    
    # check for help flag
    if "--help" in sys.argv or "-h" in sys.argv:
        print("Usage: python3 deam_mp3_converter.py [--force] [--help]")
        print("  --force, -f: Overwrite existing WAV files")
        print("  --help, -h: Show this help message")
        return
    
    # check for force overwrite flag
    force_overwrite = "--force" in sys.argv or "-f" in sys.argv
    
    convert_all_mp3_files(force_overwrite=force_overwrite)

if __name__ == "__main__":
    main()
