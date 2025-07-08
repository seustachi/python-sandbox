import os
import subprocess
import sys

def create_data_analysis_project():
    """
    Create a complete project structure with virtual environment for data analysis
    """
    print("=== Day 5: Creating Data Analysis Project Structure ===")
    
    project_name = "data_analysis_project"
    
    # Project structure
    directories = [
        f"{project_name}",
        f"{project_name}/data",
        f"{project_name}/data/raw",
        f"{project_name}/data/processed", 
        f"{project_name}/notebooks",
        f"{project_name}/src",
        f"{project_name}/tests",
        f"{project_name}/docs",
        f"{project_name}/output",
        f"{project_name}/config"
    ]
    
    # Create directories
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"Created directory: {directory}")
    
    # Create essential files
    files_content = {
        f"{project_name}/README.md": """# Data Analysis Project

## Overview
This project analyzes sales and customer data to provide business insights.

## Project Structure
```
data_analysis_project/
├── data/
│   ├── raw/          # Original, immutable data
│   └── processed/    # Cleaned and transformed data
├── notebooks/        # Jupyter notebooks for exploration
├── src/             # Source code
├── tests/           # Unit tests
├── docs/            # Documentation
├── output/          # Generated reports and visualizations
├── config/          # Configuration files
├── requirements.txt # Project dependencies
└── README.md       # This file
```

## Setup
1. Create virtual environment: `python -m venv venv`
2. Activate virtual environment: `source venv/bin/activate` (Linux/Mac) or `venv\\Scripts\\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Place raw data in `data/raw/`
2. Run data processing scripts in `src/`
3. Use notebooks for exploration and analysis
4. Check `output/` for generated reports
""",
        
        f"{project_name}/requirements.txt": """# Data Science Core
numpy>=1.21.0
pandas>=1.5.0
matplotlib>=3.5.0
seaborn>=0.11.0
scipy>=1.9.0

# Machine Learning
scikit-learn>=1.2.0

# Jupyter and Analysis
jupyter>=1.0.0
ipykernel>=6.0.0

# Data Visualization
plotly>=5.0.0

# Utilities
requests>=2.28.0
python-dotenv>=0.19.0

# Development and Testing
pytest>=7.0.0
black>=22.0.0
flake8>=4.0.0

# Optional: Database connectivity
# sqlalchemy>=1.4.0
# psycopg2-binary>=2.9.0  # PostgreSQL
# pymongo>=4.0.0          # MongoDB
""",
        
        f"{project_name}/.gitignore": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual Environment
venv/
env/
ENV/

# Jupyter Notebook
.ipynb_checkpoints

# Data files (optional - be careful with large files)
data/raw/*.csv
data/raw/*.xlsx
data/raw/*.json

# Output files
output/*.png
output/*.pdf
output/*.html

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Environment variables
.env
""",
        
        f"{project_name}/src/__init__.py": "",
        
        f"{project_name}/src/data_loader.py": """\"\"\"
Data loading utilities for the project
\"\"\"
import pandas as pd
import numpy as np
from pathlib import Path

class DataLoader:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.raw_dir = self.data_dir / "raw"
        self.processed_dir = self.data_dir / "processed"
    
    def load_csv(self, filename, data_type="raw"):
        \"\"\"Load CSV file from raw or processed directory\"\"\"
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
        \"\"\"Save processed data to processed directory\"\"\"
        filepath = self.processed_dir / filename
        df.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}")
    
    def create_sample_data(self):
        \"\"\"Create sample data for testing\"\"\"
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
""",
        
        f"{project_name}/src/data_processor.py": """\"\"\"
Data processing and cleaning utilities
\"\"\"
import pandas as pd
import numpy as np
from datetime import datetime

class DataProcessor:
    def __init__(self):
        pass
    
    def clean_sales_data(self, df):
        \"\"\"Clean and validate sales data\"\"\"
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
        \"\"\"Create summary statistics\"\"\"
        summary = {
            'total_records': len(df),
            'date_range': f"{df['date'].min()} to {df['date'].max()}",
            'total_revenue': df['total_revenue'].sum(),
            'average_sale': df['sales_amount'].mean(),
            'top_product': df.groupby('product')['total_revenue'].sum().idxmax(),
            'top_region': df.groupby('region')['total_revenue'].sum().idxmax()
        }
        return summary
""",
        
        f"{project_name}/tests/__init__.py": "",
        
        f"{project_name}/tests/test_data_loader.py": """\"\"\"
Tests for data loader functionality
\"\"\"
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
    \"\"\"Test DataLoader initialization\"\"\"
    loader = DataLoader()
    assert loader.data_dir == Path("data")
    assert loader.raw_dir == Path("data/raw")
    assert loader.processed_dir == Path("data/processed")

def test_sample_data_creation():
    \"\"\"Test sample data creation\"\"\"
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
""",
        
        f"{project_name}/config/config.py": """\"\"\"
Configuration settings for the project
\"\"\"
import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUT_DIR = PROJECT_ROOT / "output"

# Data processing settings
DEFAULT_DATE_FORMAT = "%Y-%m-%d"
RANDOM_SEED = 42

# Visualization settings
FIGURE_SIZE = (12, 8)
DPI = 300

# API settings (if needed)
API_TIMEOUT = 30
MAX_RETRIES = 3
""",
        
        f"{project_name}/notebooks/01_data_exploration.ipynb": """{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Exploration\\n",
    "\\n",
    "This notebook explores the sales data and provides initial insights."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "import sys\\n",
    "sys.path.append('../src')\\n",
    "\\n",
    "import pandas as pd\\n",
    "import numpy as np\\n",
    "import matplotlib.pyplot as plt\\n",
    "import seaborn as sns\\n",
    "\\n",
    "from data_loader import DataLoader\\n",
    "from data_processor import DataProcessor\\n",
    "\\n",
    "# Load data\\n",
    "loader = DataLoader('../data')\\n",
    "processor = DataProcessor()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Load and Clean Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "source": [
    "# Create sample data if it doesn't exist\\n",
    "df = loader.create_sample_data()\\n",
    "\\n",
    "# Clean the data\\n",
    "clean_df = processor.clean_sales_data(df)\\n",
    "\\n",
    "# Display basic info\\n",
    "print(clean_df.info())\\n",
    "clean_df.head()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}"""
    }
    
    # Write all files
    for filepath, content in files_content.items():
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created file: {filepath}")
    
    # Instructions for virtual environment
    print(f"\n=== Virtual Environment Setup Instructions ===")
    print(f"1. Navigate to project directory:")
    print(f"   cd {project_name}")
    print(f"")
    print(f"2. Create virtual environment:")
    print(f"   python -m venv venv")
    print(f"")
    print(f"3. Activate virtual environment:")
    print(f"   # Windows:")
    print(f"   venv\\Scripts\\activate")
    print(f"   # macOS/Linux:")
    print(f"   source venv/bin/activate")
    print(f"")
    print(f"4. Install dependencies:")
    print(f"   pip install -r requirements.txt")
    print(f"")
    print(f"5. Test the setup:")
    print(f"   python -c 'import numpy, pandas, matplotlib; print(\"Setup successful!\")'")
    print(f"")
    print(f"6. Run tests:")
    print(f"   python -m pytest tests/")
    print(f"")
    print(f"7. Start Jupyter notebook:")
    print(f"   jupyter notebook notebooks/")
    
    # Demonstrate virtual environment creation (commented out to avoid actual creation)
    print(f"\n=== Virtual Environment Demo ===")
    print("# The following commands would create and setup the virtual environment:")
    print("# (Run these manually in your terminal)")
    commands = [
        f"cd {project_name}",
        "python -m venv venv",
        "# Activate: venv\\Scripts\\activate (Windows) or source venv/bin/activate (macOS/Linux)",
        "pip install --upgrade pip",
        "pip install -r requirements.txt",
        "python -m pytest tests/",
        "jupyter notebook notebooks/"
    ]
    
    for cmd in commands:
        print(f"  {cmd}")
    
    return project_name

# Create the project
project_name = create_data_analysis_project()
print(f"\n=== Project '{project_name}' created successfully! ===")
