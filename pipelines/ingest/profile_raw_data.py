import pandas as pd

FILE_PATH = "./data/raw/OnlineRetail.csv"

def main():
	df=pd.read_csv(FILE_PATH,encoding="ISO-8859-1")
	print("=== BASIC INFO ===")
	print(df.info())
	
	print("\n=== SAMPLE ROWS ===")
	print(df.head())

	print("\n=== MISSING VALUES PER COLUMN ===")
	print(df.isnull().sum())

	print("\n=== NEGATIVE QUANTITIES ===")
	print((df["Quantity"]<0).sum())
	
	print("\n=== NEGATIVE PRICES ===")
	print((df["UnitPrice"] < 0).sum())
	
	print("\n=== UNIQUE COUNTS ===")
	print(df.nunique())


if __name__ == "__main__":
    main()
