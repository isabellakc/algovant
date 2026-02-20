import pandas as pd
import numpy as np
import glob
import os

DATA_PATH = "../data/daily/us"

def load_data(symbol, base_path=DATA_PATH):
    """Load stock data from Stooq files"""
    search_patterns = [
        os.path.join(base_path, "**", f"{symbol.lower()}.us.txt"),
        os.path.join(base_path, "nyse stocks", "**", f"{symbol.lower()}.us.txt"),
        os.path.join(base_path, "nasdaq stocks", "**", f"{symbol.lower()}.us.txt"),
    ]
    
    files = []
    for pattern in search_patterns:
        files = glob.glob(pattern, recursive=True)
        if files:
            break
    
    if not files:
        return None
    
    try:
        df = pd.read_csv(files[0])
        df.columns = [c.replace('<', '').replace('>', '').capitalize() for c in df.columns]
        
        if 'Vol' in df.columns:
            df.rename(columns={'Vol': 'Volume'}, inplace=True)
        
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'], format='%Y%m%d')
            df.set_index('Date', inplace=True)
        elif 'Time' in df.columns:
            df['Time'] = pd.to_datetime(df['Time'], format='%Y%m%d')
            df.set_index('Time', inplace=True)
            df.index.name = 'Date'
        
        if 'Volume' not in df.columns:
            df['Volume'] = 0
            
        return df.dropna(subset=['Open', 'High', 'Low', 'Close'])
        
    except:
        return None

def load_all_stocks(symbols):
    """Load multiple stocks at once"""
    stock_data = {}
    for s in symbols:
        df = load_data(s)
        if df is not None:
            stock_data[s] = df
    return stock_data
