def main():
    print("Hello from my-repo!")


if __name__ == "__main__":
    main()
from seaborn import load_dataset
df = load_dataset('penguins')
print(df.head())
#Mahesh-Repo Owner
from sklearn.model_selection import train_test_split
X = df.drop('species', axis=1)
y = df['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
