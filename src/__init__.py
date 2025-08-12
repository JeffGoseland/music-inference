"""
Music Code Project - Source Package
"""

from .utils import (
    load_data,
    save_data,
    create_summary_stats,
    plot_music_analysis,
    print_project_info
)

__version__ = "1.0.0"
__author__ = "Music Code Project"

# Make main functions easily accessible
__all__ = [
    'load_data',
    'save_data', 
    'create_summary_stats',
    'plot_music_analysis',
    'print_project_info'
] 