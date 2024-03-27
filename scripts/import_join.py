import pandas as pd
import glob
import os

def read_and_concat_csv_files(directory_path):
    all_files = glob.glob(os.path.join(directory_path, "*.csv"))
    df_list = []
    
    for filename in all_files:
        df = pd.read_csv(filename)
        df_list.append(df)
    
    full_df = pd.concat(df_list, ignore_index=True)
    return full_df

def main():
    candidates_path = "../data/candidates"
    orgs_path = "../data/orgs"
    output_path = "../data/cleaned"
    
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    candidates_df = read_and_concat_csv_files(candidates_path)
    candidates_df.to_csv(os.path.join(output_path, "candidates_cleaned.csv"), index=False)
    
    orgs_df = read_and_concat_csv_files(orgs_path)
    orgs_df.to_csv(os.path.join(output_path, "orgs_cleaned.csv"), index=False)

if __name__ == "__main__":
    main()
