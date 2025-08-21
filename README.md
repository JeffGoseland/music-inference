# Music Inference - Python Jupyter Project

This is a Python Jupyter project for music data analysis and inference using the DEAM (Database for Emotional Analysis in Music) dataset.

## Setup Instructions

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Connect to Jupyter Server:**
   - Server URL: http://localhost:8889/lab
   - Token: c0c173e9c652493f7cf798ed418d1cbd856f9f2d5d673c99
   - Full URL: http://localhost:8889/lab?token=c0c173e9c652493f7cf798ed418d1cbd856f9f2d5d673c99

3. **Project Structure:**
   ```
   music_code/
   ├── notebooks/          # Jupyter notebooks
   ├── data/              # Raw data files
   │   ├── DEAM/         # DEAM dataset
   │   │   ├── features/ # Audio features (1802 CSV files)
   │   │   └── annotations/ # Emotional annotations
   │   └── processed/    # Processed consolidated data
   ├── src/               # Source code
   │   ├── deam_features_loader.py    # Load and consolidate features
   │   ├── deam_annotations_loader.py # Load and consolidate annotations
   │   └── deam_utils.py              # Common utility functions
   ├── requirements.txt   # Python dependencies
   └── README.md         # This file
   ```

## Loading DEAM Data

### Option 1: Using the Loader Scripts

1. **Load Features Data:**
   ```bash
   cd src
   python3 deam_features_loader.py
   ```
   This creates `data/processed/deam_features_consolidated.csv` (457,622 rows, 262 columns)

2. **Load Annotations Data:**
   ```bash
   cd src
   python3 deam_annotations_loader.py
   ```
   This creates `data/processed/deam_annotations_consolidated.csv` (3,604 rows, 1,226 columns)

### Option 2: Using Jupyter Notebook

1. Open the Jupyter Lab URL above
2. Navigate to `notebooks/DEAM_features_analysis.ipynb`
3. Run the cells to load and explore the data

## Data Description

- **Features Data**: Audio features extracted from 1,802 music files
  - Each file contains time-series data with 261 features
  - Features include spectral, MFCC, and audio descriptors
  - Total: ~457K rows, 262 columns, ~0.9 GB

- **Annotations Data**: Emotional ratings for the same 1,802 music files
  - Arousal and valence ratings at 500ms intervals
  - Time points from 15s to 626.5s
  - Total: 3,604 rows, 1,226 columns, ~0.03 GB

## Getting Started

1. Open your browser and navigate to the Jupyter Lab URL above
2. Run the loader scripts to consolidate the data
3. Use the analysis notebook to explore the data
4. Import utility functions from the `src/` directory

## Audio File Conversion

### Converting MP3 to WAV Format

The DEAM dataset includes MP3 audio files that need to be converted to WAV format for easier processing with audio analysis libraries.

#### Prerequisites

1. **Install FFmpeg (required for MP3 processing):**
   ```bash
   # On macOS with Homebrew
   brew install ffmpeg
   
   # On Ubuntu/Debian
   sudo apt-get install ffmpeg
   
   # On Windows
   # Download from https://ffmpeg.org/download.html
   ```

2. **Install Python audio packages:**
   ```bash
   pip install pydub librosa
   ```

#### Running the Converter

1. **Convert all MP3 files to WAV:**
   ```bash
   cd src
   python3 deam_mp3_converter.py
   ```

   This script will:
   - Process all MP3 files in `data/DEAM/MEMD_audio/`
   - Create a `wav/` subdirectory in the same location
   - Convert each MP3 to WAV format
   - Verify conversions using librosa
   - Skip files that have already been converted

2. **Output:**
   - Original MP3 files remain unchanged
   - WAV files saved to `data/DEAM/MEMD_audio/wav/`
   - Each WAV file maintains the same filename (with .wav extension)

#### Manual Conversion

To convert a single file:
```python
from pydub import AudioSegment

# Load MP3 file
audio = AudioSegment.from_mp3("path/to/file.mp3")

# Export as WAV
audio.export("path/to/output.wav", format="wav")
```

## Available Packages

- **Jupyter**: Interactive computing environment
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib/Seaborn**: Data visualization
- **Requests**: HTTP library for API calls
- **Python-dotenv**: Environment variable management
- **Pydub**: Audio file manipulation and conversion
- **Librosa**: Audio and music signal processing
