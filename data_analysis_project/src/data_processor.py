"""
Data processing and cleaning utilities
"""
import pandas as pd
import numpy as np
from datetime import datetime

class DataProcessor:
    def __init__(self):
        pass
    
    def clean_sales_data(self, df):
        """Clean and validate sales data"""
        # Make a copy to avoid modifying original
        cleaned_df = df.copy()
        
        # Convert date column
        cleaned_df['date'] = pd.to_datetime(cleaned_df['date'])
        
        # Remove negative sales amounts
        cleaned_df = cleaned_df[cleaned_df['sales_amount'] > 0]
        
        # Remove rows with missing essential data
        cleaned_df = cleaned_df.dropna(subset=['product', 'sales_amount'])
        
        # Add derived columns
        cleaned_df['year'] = cleaned_df['date'].dt.year
        cleaned_df['month'] = cleaned_df['date'].dt.month
        cleaned_df['day_of_week'] = cleaned_df['date'].dt.dayofweek
        cleaned_df['total_revenue'] = cleaned_df['sales_amount'] * cleaned_df['quantity']
        
        print(f"Data cleaning complete. Records: {len(df)} -> {len(cleaned_df)}")
        return cleaned_df
    
    def create_summary_stats(self, df):
        """Create summary statistics"""
        summary = {
            'total_records': len(df),
            'date_range': f"{df['date'].min()} to {df['date'].max()}",
            'total_revenue': df['total_revenue'].sum(),
            'average_sale': df['sales_amount'].mean(),
            'top_product': df.groupby('product')['total_revenue'].sum().idxmax(),
            'top_region': df.groupby('region')['total_revenue'].sum().idxmax()
        }
        return summary
