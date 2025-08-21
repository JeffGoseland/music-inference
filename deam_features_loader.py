#!/usr/bin/env python3
"""
DEAM Features Loader - Single Script

Reads all CSV files from data/DEAM/features and creates a consolidated dataframe
where each row represents one file, with the file number as ID and contents as metadata.

Author: Jeff Goseland
Date: 2025
"""

import pandas as pd
from pathlib import Path
from deam_utils import (
    get_csv_files, 
    load_and_concatenate_csvs, 
    save_dataframe, 
    print_basic_summary, 
    print_distribution_summary
)

def extract_file_id(file_path):
    """extract file ID from filename (e.g., "2.csv" -> 2)"""
    return int(Path(file_path).stem)

def load_deam_features():
    """
    load all DEAM feature CSV files and concatenate them into a single dataframe.
    each file contains time series data with multiple rows.
    """
    features_dir = "data/DEAM/features"
    
    # get all CSV files
    csv_files = get_csv_files(features_dir)
    
    # load and concatenate with file ID extraction
    consolidated_df = load_and_concatenate_csvs(
        csv_files=csv_files,
        id_extractor=extract_file_id,
        id_column_name='file_id',
        separator=';'
    )
    
    return consolidated_df

def print_summary(df):
    """print summary statistics of the consolidated dataframe"""
    print_basic_summary(df, 'file_id', 'file ID')
    print_distribution_summary(df, 'file_id', 'file ID')

def main():
    """main function to load, summarize, and save DEAM features"""
    print("loading DEAM features...")
    
    # load all features
    df = load_deam_features()
    
    # print summary
    print_summary(df)
    
    # save consolidated data
    output_path = "data/deam_features_consolidated.csv"
    save_dataframe(df, output_path)
    
    print(f"\nconsolidated DEAM features saved to: {output_path}")

if __name__ == "__main__":
    main()
