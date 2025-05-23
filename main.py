def main():
    print("Hello from my-repo!")


if __name__ == "__main__":
    main()
from seaborn import load_dataset
df = load_dataset('penguins')
print(df.head())
