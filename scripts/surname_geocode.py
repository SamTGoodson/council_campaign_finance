import pandas as pd
import surgeo
import numpy as np

def split_names(df):
    """Splits 'name' into 'first_name' and 'last_name' with handling for unmatched formats."""
    def split_name(name):
        parts = name.split(", ")
        if len(parts) == 2:
            return parts[1], parts[0]  
        else:
            return np.nan, np.nan  

    df[['first_name', 'last_name']] = df.apply(lambda x: split_name(x['NAME']), axis=1, result_type='expand')
    return df

def run_surgeo_analysis(df):
    """Runs Surgeo analysis and appends the results as new columns."""
    fsg = surgeo.BIFSGModel()
    
    first_names = df['first_name'].str.upper()
    surnames = df['last_name'].str.upper()
    zctas = df['ZIP']
    
    fsg_results = fsg.get_probabilities(first_names, surnames, zctas)
    
    return pd.concat([df, fsg_results], axis=1)

def main():
    df = pd.read_csv('../data/cleaned/candidates_cleaned.csv')
    df = split_names(df)
    df = run_surgeo_analysis(df)
    df.to_csv('../data/cleaned/candidates_surgeo.csv', index=False)

if __name__ == "__main__":
    main()
