import pandas as pd
import argparse
from datetime import datetime
import os

def compare_monthly_data(current_month_file, previous_month_file, output_file):
    """
    Compare current month data with previous month data and generate comparison results.
    Only includes entities that have changes in either is_false or is_true values.
    Shows only previous count, current count, and the difference.
    
    Args:
        current_month_file (str): Path to the current month CSV file
        previous_month_file (str): Path to the previous month CSV file
        output_file (str): Path to save the output comparison CSV file
    """
    # Read the CSV files
    print(f"Reading current month data from: {current_month_file}")
    current_df = pd.read_csv(current_month_file)
    
    print(f"Reading previous month data from: {previous_month_file}")
    previous_df = pd.read_csv(previous_month_file)
    
    # Ensure both dataframes have the same columns
    if set(current_df.columns) != set(previous_df.columns):
        print("Warning: Current and previous month data have different columns.")
    
    # Assuming 'table_schema' and 'table_name' together form a unique identifier
    # Create a key column for merging
    current_df['key'] = current_df['table_schema'] + '_' + current_df['table_name']
    previous_df['key'] = previous_df['table_schema'] + '_' + previous_df['table_name']
    
    # Merge the dataframes
    merged_df = current_df.merge(
        previous_df,
        on='key',
        how='outer',
        suffixes=('_current', '_previous')
    )
    
    # Create result dataframe
    result_df = pd.DataFrame()
    result_df['table_schema'] = merged_df['table_schema_current'].fillna(merged_df['table_schema_previous'])
    result_df['table_name'] = merged_df['table_name_current'].fillna(merged_df['table_name_previous'])
    
    # Track whether each entity has any changes
    has_changes = pd.Series([False] * len(result_df))
    
    # Compare is_false and is_true columns
    comparison_columns = ['is_false', 'is_true']
    for col in comparison_columns:
        current_col = f"{col}_current"
        previous_col = f"{col}_previous"
        
        # Handle cases where columns might not exist in either dataframe
        if current_col not in merged_df.columns:
            merged_df[current_col] = 0
        if previous_col not in merged_df.columns:
            merged_df[previous_col] = 0
            
        # Fill NaN values with 0 for comparison
        merged_df[current_col] = merged_df[current_col].fillna(0).astype(int)
        merged_df[previous_col] = merged_df[previous_col].fillna(0).astype(int)
        
        # Calculate change
        result_df[f"{col}_previous"] = merged_df[previous_col]
        result_df[f"{col}_current"] = merged_df[current_col]
        result_df[f"{col}_change"] = merged_df[current_col] - merged_df[previous_col]
        
        # Update has_changes flag
        has_changes = has_changes | (result_df[f"{col}_change"] != 0)
    
    # Filter the result to only include entities with changes
    filtered_result = result_df[has_changes].copy()
    
    # Check if there are any changes
    if filtered_result.empty:
        print("No changes found between the datasets!")
    else:
        # Save the filtered results
        print(f"Saving comparison results to: {output_file}")
        print(f"Found {len(filtered_result)} entities with changes (out of {len(result_df)} total entities)")
        filtered_result.to_csv(output_file, index=False)
        print("Comparison completed successfully!")
        
        # Print summary statistics
        print("\nSummary Statistics:")
        for col in comparison_columns:
            print(f"\n{col.upper()} Changes:")
            positive_changes = (filtered_result[f"{col}_change"] > 0).sum()
            negative_changes = (filtered_result[f"{col}_change"] < 0).sum()
            no_changes = (filtered_result[f"{col}_change"] == 0).sum()
            
            print(f"  Increased: {positive_changes}")
            print(f"  Decreased: {negative_changes}")
            print(f"  No change: {no_changes}")
            
            # Calculate total changes
            total_positive = filtered_result[filtered_result[f"{col}_change"] > 0][f"{col}_change"].sum()
            total_negative = filtered_result[filtered_result[f"{col}_change"] < 0][f"{col}_change"].sum()
            print(f"  Total increase: {total_positive}")
            print(f"  Total decrease: {abs(total_negative)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare monthly data files')
    parser.add_argument('current_month', help='Path to the current month CSV file')
    parser.add_argument('previous_month', help='Path to the previous month CSV file')
    parser.add_argument('--output', default=None, help='Path to save the output CSV file (default: comparison_result_YYYYMMDD.csv)')
    
    args = parser.parse_args()
    
    # Generate default output filename if not provided

    if args.output is None:
        current_base = os.path.splitext(os.path.basename(args.current_month))[0]
        previous_base = os.path.splitext(os.path.basename(args.previous_month))[0]
        current_date = datetime.now().strftime("%Y%m%d")
        args.output = f"{current_base}_vs_{previous_base}_comparison_{current_date}.csv"


compare_monthly_data(args.current_month, args.previous_month, args.output)
