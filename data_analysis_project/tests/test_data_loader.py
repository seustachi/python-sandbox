"""
Tests for data loader functionality
"""
import pytest
import pandas as pd
import tempfile
import os
from pathlib import Path
import sys

# Add src to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from data_loader import DataLoader

def test_data_loader_initialization():
    """Test DataLoader initialization"""
    loader = DataLoader()
    assert loader.data_dir == Path("data")
    assert loader.raw_dir == Path("data/raw")
    assert loader.processed_dir == Path("data/processed")

def test_sample_data_creation():
    """Test sample data creation"""
    with tempfile.TemporaryDirectory() as temp_dir:
        loader = DataLoader(temp_dir)
        
        # Create directories
        loader.raw_dir.mkdir(parents=True, exist_ok=True)
        loader.processed_dir.mkdir(parents=True, exist_ok=True)
        
        # Create sample data
        df = loader.create_sample_data()
        
        # Test data properties
        assert len(df) == 1000
        assert 'date' in df.columns
        assert 'product' in df.columns
        assert 'sales_amount' in df.columns
        assert all(df['sales_amount'] > 0)  # All sales amounts should be positive

if __name__ == "__main__":
    pytest.main([__file__])
