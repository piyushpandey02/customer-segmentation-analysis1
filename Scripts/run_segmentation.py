# scripts/run_segmentation.py

import pandas as pd
import numpy as np
import datetime as dt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def load_and_clean_data(file_path):
    """Loads the raw data and performs initial cleaning."""
    print("Loading and cleaning data...")
    df = pd.read_excel(file_path)

    # --- Data Cleaning ---
    df.dropna(subset=['CustomerID'], inplace=True)
    df['CustomerID'] = df['CustomerID'].astype(int)
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    
    print("Data cleaned successfully.")
    return df

def create_rfm_features(df):
    """Creates RFM features from the cleaned transaction data."""
    print("Creating RFM features...")
    
    # Create 'TotalPrice'
    df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

    # Set snapshot date
    snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

    # Calculate RFM
    rfm_df = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda date: (snapshot_date - date.max()).days,
        'InvoiceNo': 'nunique',
        'TotalPrice': 'sum'
    })
    rfm_df.rename(columns={'InvoiceDate': 'Recency', 'InvoiceNo': 'Frequency', 'TotalPrice': 'Monetary'}, inplace=True)
    
    print("RFM features created.")
    return rfm_df

def preprocess_rfm(rfm_df):
    """Applies log transformation and scaling to RFM features."""
    print("Preprocessing RFM data...")
    
    # Log transformation
    rfm_log = rfm_df.apply(np.log1p)

    # Scaling
    scaler = StandardScaler()
    rfm_scaled = scaler.fit_transform(rfm_log)
    rfm_scaled = pd.DataFrame(rfm_scaled, index=rfm_df.index, columns=rfm_df.columns)
    
    print("Preprocessing complete.")
    return rfm_scaled

def run_clustering(scaled_df, original_rfm_df):
    """Runs K-Means clustering and adds labels to the original RFM dataframe."""
    print("Running K-Means clustering...")
    
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans.fit(scaled_df)
    
    # Add cluster labels
    segmented_rfm = original_rfm_df.copy()
    segmented_rfm['Cluster'] = kmeans.labels_
    
    print("Clustering complete.")
    return segmented_rfm

def main():
    """Main function to run the entire segmentation pipeline."""
    # Define file paths based on the project structure
    raw_data_path = 'data/raw/Online Retail.xlsx'
    output_path = 'data/processed/rfm_segmented_customers_from_script.csv'

    # Run the pipeline
    cleaned_df = load_and_clean_data(raw_data_path)
    rfm_df = create_rfm_features(cleaned_df)
    rfm_scaled = preprocess_rfm(rfm_df)
    final_segmented_df = run_clustering(rfm_scaled, rfm_df)
    
    # Save the final output
    final_segmented_df.to_csv(output_path)
    print(f"✅ Segmentation complete! Final data saved to '{output_path}'.")
    print("\nFinal Segment Analysis:\n", final_segmented_df.groupby('Cluster')[['Recency', 'Frequency', 'Monetary']].mean().round(1))


# This makes the script runnable from the command line
if __name__ == "__main__":
    main()
