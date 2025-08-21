"""
DEAM Annotations Loader
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

def extract_annotation_type(file_path):
    """extract annotation type from filename (e.g., "arousal.csv" -> "arousal")"""
    return Path(file_path).stem

def load_deam_annotations():
    """
    load all DEAM annotation CSV files and concatenate them into a single dataframe.
    each file contains time series annotation data with multiple columns.
    """
    annotations_dir = "../data/DEAM/annotations/annotations averaged per song/dynamic (per second annotations)"
    
    # get all CSV files
    csv_files = get_csv_files(annotations_dir)
    
    # load and concatenate with annotation type extraction
    consolidated_df = load_and_concatenate_csvs(
        csv_files=csv_files,
        id_extractor=extract_annotation_type,
        id_column_name='annotation_type',
        separator=','
    )
    
    return consolidated_df

def print_summary(df):
    """print summary statistics of the consolidated dataframe"""
    print_basic_summary(df, 'song_id', 'song ID')
    
    # print annotation type distribution
    print("\n=== ANNOTATION TYPE DISTRIBUTION ===")
    type_counts = df['annotation_type'].value_counts()
    for annotation_type, count in type_counts.items():
        print(f"{annotation_type}: {count} rows")
    
    print_distribution_summary(df, 'song_id', 'song ID')

def main():
    """main function to load, summarize, and save DEAM annotations"""
    print("loading DEAM annotations...")
    
    # load all annotations
    df = load_deam_annotations()
    
    # print summary
    print_summary(df)
    
    # save consolidated data
    output_path = "../data/processed/deam_annotations_consolidated.csv"
    save_dataframe(df, output_path)
    
    print(f"\nconsolidated DEAM annotations saved to: {output_path}")

if __name__ == "__main__":
    main()
