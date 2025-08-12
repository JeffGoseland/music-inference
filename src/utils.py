"""
Utility functions for the music code project.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, List, Dict, Any


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from various file formats.
    
    Args:
        file_path (str): Path to the data file
        
    Returns:
        pd.DataFrame: Loaded data
    """
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def save_data(df: pd.DataFrame, file_path: str) -> None:
    """
    Save data to various file formats.
    
    Args:
        df (pd.DataFrame): Data to save
        file_path (str): Path where to save the file
    """
    if file_path.endswith('.csv'):
        df.to_csv(file_path, index=False)
    elif file_path.endswith('.json'):
        df.to_json(file_path, orient='records')
    elif file_path.endswith('.xlsx'):
        df.to_excel(file_path, index=False)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")


def create_summary_stats(df: pd.DataFrame, numeric_columns: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Create summary statistics for a dataframe.
    
    Args:
        df (pd.DataFrame): Input dataframe
        numeric_columns (List[str], optional): List of numeric columns to analyze
        
    Returns:
        Dict[str, Any]: Summary statistics
    """
    if numeric_columns is None:
        numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
    
    summary = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'dtypes': df.dtypes.to_dict(),
        'missing_values': df.isnull().sum().to_dict(),
        'numeric_summary': df[numeric_columns].describe().to_dict() if numeric_columns else {},
        'categorical_summary': {}
    }
    
    # Add categorical column summaries
    categorical_columns = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_columns:
        summary['categorical_summary'][col] = df[col].value_counts().to_dict()
    
    return summary


def plot_music_analysis(df: pd.DataFrame, 
                       x_col: str, 
                       y_col: str, 
                       title: str = "Music Analysis",
                       figsize: tuple = (12, 8)) -> None:
    """
    Create a standardized music analysis plot.
    
    Args:
        df (pd.DataFrame): Data to plot
        x_col (str): Column for x-axis
        y_col (str): Column for y-axis
        title (str): Plot title
        figsize (tuple): Figure size
    """
    plt.figure(figsize=figsize)
    
    # Create the plot
    if df[y_col].dtype in ['int64', 'float64']:
        # Numeric y-axis - use bar plot
        sns.barplot(data=df, x=x_col, y=y_col)
    else:
        # Categorical y-axis - use count plot
        sns.countplot(data=df, x=x_col)
    
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel(x_col.replace('_', ' ').title(), fontsize=12)
    plt.ylabel(y_col.replace('_', ' ').title(), fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def print_project_info():
    """
    Print information about the project setup.
    """
    print("🎵 Music Code Jupyter Project")
    print("=" * 40)
    print("📊 Server URL: http://localhost:8889/lab")
    print("🔑 Token: c0c173e9c652493f7cf798ed418d1cbd856f9f2d5d673c99")
    print("🔗 Full URL: http://localhost:8889/lab?token=c0c173e9c652493f7cf798ed418d1cbd856f9f2d5d673c99")
    print("\n📁 Project Structure:")
    print("  ├── notebooks/     # Jupyter notebooks")
    print("  ├── data/         # Data files")
    print("  ├── src/          # Source code")
    print("  └── requirements.txt")
    print("\n🚀 Ready to start coding!") 