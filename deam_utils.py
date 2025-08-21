"""
DEAM Data Loading Utilities
Common functions for loading and processing DEAM dataset files.

Author: Jeff Goseland
Date: 2025
"""

import pandas as pd
import os
import glob
from pathlib import Path

def save_dataframe(df, output_path):
    """save the consolidated dataframe to CSV"""
    # purpose: save a pandas dataframe to CSV file with automatic directory creation
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"saving to {output_path}...")
    df.to_csv(output_path, index=False)
    print("save completed!")

def print_basic_summary(df, id_column, id_label):
    """print basic summary statistics of the consolidated dataframe"""
    # purpose: display basic dataset statistics including rows, columns, memory usage, and sample data
    print("\n=== DATASET SUMMARY ===")
    print(f"total rows: {len(df):,}")
    print(f"total columns: {len(df.columns)}")
    print(f"memory usage: {df.memory_usage(deep=True).sum() / 1024**3:.2f} GB")
    
    print(f"\nunique {id_label}: {df[id_column].nunique()}")
    print(f"rows per {id_label} (avg): {len(df) / df[id_column].nunique():.1f}")
    
    print("\n=== SAMPLE DATA ===")
    print(df.head())
    
    print("\n=== COLUMN NAMES (first 10) ===")
    print(list(df.columns[:10]))

def print_distribution_summary(df, id_column, id_label):
    """print distribution statistics for the ID column"""
    # purpose: display distribution statistics (min, max, mean) for the specified ID column
    print(f"\n=== {id_label.upper()} DISTRIBUTION ===")
    id_counts = df[id_column].value_counts().sort_index()
    print(f"min rows per {id_label}: {id_counts.min()}")
    print(f"max rows per {id_label}: {id_counts.max()}")
    print(f"mean rows per {id_label}: {id_counts.mean():.1f}")

def get_csv_files(directory_path):
    """get all CSV files from a directory"""
    # purpose: find and return all CSV files in a directory with error handling
    directory = Path(directory_path)
    
    if not directory.exists():
        raise FileNotFoundError(f"directory not found: {directory}")
    
    # get all CSV files
    csv_files = sorted(glob.glob(str(directory / "*.csv")))
    
    if not csv_files:
        raise FileNotFoundError(f"no CSV files found in {directory}")
    
    print(f"found {len(csv_files)} CSV files")
    return csv_files

def load_and_concatenate_csvs(csv_files, id_extractor, id_column_name, separator=','):
    """
    load multiple CSV files and concatenate them with an ID column
    
    Args:
        csv_files: list of CSV file paths
        id_extractor: function to extract ID from file path
        id_column_name: name for the ID column
        separator: CSV separator (default: comma)
    """
    # purpose: load multiple CSV files, add an ID column to each, and concatenate into one dataframe
    all_dataframes = []
    
    for file_path in csv_files:
        # extract ID using the provided function
        file_id = id_extractor(file_path)
        
        try:
            # read CSV with specified separator
            df = pd.read_csv(file_path, sep=separator)
            
            # add ID column
            df[id_column_name] = file_id
            
            all_dataframes.append(df)
            
            # print progress for features (every 100 files)
            if len(all_dataframes) % 100 == 0:
                print(f"processed {len(all_dataframes)} files...")
                
        except Exception as e:
            print(f"error processing {file_path}: {e}")
            continue
    
    # concatenate all dataframes
    print("concatenating all dataframes...")
    consolidated_df = pd.concat(all_dataframes, ignore_index=True)
    
    return consolidated_df
