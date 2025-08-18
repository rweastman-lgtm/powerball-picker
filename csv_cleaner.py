import pandas as pd

def clean_powerball_csv(file_path: str, output_path: str = "cleaned_powerball.csv") -> pd.DataFrame:
    try:
        df = pd.read_csv(file_path)

        # ✅ Validate required columns
        required = {"Draw Date", "Winning Numbers", "Powerball"}
        if not required.issubset(df.columns):
            raise ValueError(f"Missing columns. Found: {df.columns.tolist()}")

        # 🧹 Strip whitespace and drop NaNs
        df["Winning Numbers"] = df["Winning Numbers"].astype(str).str.strip()
        df["Powerball"] = pd.to_numeric(df["Powerball"], errors="coerce")
        df.dropna(subset=["Winning Numbers", "Powerball"], inplace=True)

        # 🔢 Parse winning numbers into list of ints
        def parse_numbers(row):
            try:
                nums = [int(n) for n in row.split() if n.isdigit()]
                return nums if len(nums) == 5 else None
            except:
                return None

        df["Parsed Numbers"] = df["Winning Numbers"].apply(parse_numbers)
        df.dropna(subset=["Parsed Numbers"], inplace=True)

        # 🧾 Save cleaned version
        df.to_csv(output_path, index=False)
        print(f"✅ Cleaned CSV saved to {output_path}")
        return df

    except Exception as e:
        print(f"❌ Error cleaning CSV: {e}")
        return pd.DataFrame()

# Run it
if __name__ == "__main__":
    clean_powerball_csv("powerball_last_year.csv")

