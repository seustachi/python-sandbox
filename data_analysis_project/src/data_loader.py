"""
Data loading utilities for the project
"""
import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.raw_dir = self.data_dir / "raw"
        self.processed_dir = self.data_dir / "processed"
    
    def load_csv(self, filename, data_type="raw"):
        """Load CSV file from raw or processed directory"""
        if data_type == "raw":
            filepath = self.raw_dir / filename
        else:
            filepath = self.processed_dir / filename
        
        try:
            return pd.read_csv(filepath)
        except FileNotFoundError:
            print(f"File {filepath} not found")
            return None
    
    def save_processed_data(self, df, filename):
        """Save processed data to processed directory"""
        filepath = self.processed_dir / filename
        df.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}")
    
    def create_sample_data(self):
        """Create sample data for testing"""
        # Sales data
        np.random.seed(42)
        n_records = 1000
        
        sales_data = pd.DataFrame({
            'date': pd.date_range('2023-01-01', periods=n_records, freq='D')[:n_records],
            'product': np.random.choice(['Laptop', 'Phone', 'Tablet', 'Headphones'], n_records),
            'sales_amount': np.random.normal(500, 150, n_records),
            'quantity': np.random.randint(1, 10, n_records),
            'region': np.random.choice(['North', 'South', 'East', 'West'], n_records)
        })
        
        # Ensure positive sales amounts
        sales_data['sales_amount'] = np.abs(sales_data['sales_amount'])
        
        # Save sample data
        sales_data.to_csv(self.raw_dir / "sample_sales.csv", index=False)
        print(f"Sample sales data created: {len(sales_data)} records")
        
        return sales_data
