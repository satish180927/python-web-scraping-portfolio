import os
import pandas as pd

def clean_scraped_data():
    print("=== KUMBH AI: PANDAS DATA CLEANER ===\n")
    
    input_file = "/sdcard/Download/kumbh_multipage_quotes.csv"
    output_file = "/sdcard/Download/kumbh_cleaned_quotes.csv"
    
    print("1. Loading raw CSV file using Pandas...")
    df = pd.read_csv(input_file)
    print(f"   Original Rows: {len(df)}")
    
    print("\n2. Cleaning Data (Removing Duplicates)...")
    df = df.drop_duplicates()
    print(f"   Cleaned Rows: {len(df)}")
    
    print("\n3. Processing Data (Adding Quote_Length column)...")
    df['Quote_Length'] = df['Quote Text'].apply(len)
    
    print("\n4. Filtering high-value long quotes (> 60 chars)...")
    filtered_df = df[df['Quote_Length'] > 60]
    
    filtered_df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\nSUCCESS! Cleaned file saved to: {output_file}")
    
    print("\n--- DATA INSIGHTS (Top 3 Most Famous Authors) ---")
    top_authors = df['Author Name'].value_counts().head(3)
    print(top_authors.to_string())

if __name__ == "__main__":
    clean_scraped_data()
