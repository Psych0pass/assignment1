import pandas as pd


def clean(input1, input2, output):
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    df = pd.merge(df1, df2, left_on = "respondent_id", right_on = "id").drop('respondent_id', axis =1)
    df.dropna(inplace=True)
    insur = df['job'].str.contains('insurance|Insurance')
    df = df[~insur]
    return df



if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help = 'Data file (CSV)')
    parser.add_argument('input2', help = 'Data file (CSV)')
    parser.add_argument('output', help = 'Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2, args.output)
    cleaned.to_csv(args.output, index = False)