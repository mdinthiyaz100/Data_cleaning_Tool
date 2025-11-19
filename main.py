import pandas as pd
import os

def clean_data(input_file, output_file="cleaned_data.csv"):
    if not os.path.exists(input_file):
        print("Error: File not found. Please check the filename.")
        return

    print(" Reading input file...")
    df = pd.read_csv(input_file)

    print("\n Original Data Preview:")
    print(df.to_string())

    print("\n Removing duplicates...")
    df = df.drop_duplicates()

    print(" Removing rows with missing values...")
    df = df.dropna()

    print("\n Generating summary report...")
    summary = df.describe(include='all')

    # Save cleaned data
    df.to_csv(output_file, index=False)

    # Save summary to text file
    with open("summary_report.txt", "w") as f:
        f.write("Summary Statistics:\n")
        f.write(str(summary))

    print("\n Cleaning Complete!")
    print(" Cleaned file saved as:", output_file)
    print(" Summary saved as summary_report.txt")


if __name__ == "__main__":
    user_file = input("Enter your CSV file name or full path: ")
    clean_data(user_file)
