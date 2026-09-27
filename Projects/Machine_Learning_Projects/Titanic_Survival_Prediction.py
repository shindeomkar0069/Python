import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# ---------------------------------------------------------------------------
#   Function Name: DataLoad
#   Description :  Load the data from csv
#   Input :        Name of the csv file
#   Output :       DataFrame
#   Author :       Omkar Dnyandev Shinde
#   Date :         16-08-2026
# ---------------------------------------------------------------------------

def DataLoad(filename):
    df = pd.read_csv(filename)

    print("Data Load Successfully")
    print(df.head())

    return df


# ---------------------------------------------------------------------------
#   Function Name: PreprocessData
#   Description :  It performs data preprocessing
#   Input :        DataFrame
#   Output :       Updated DataFrame
# ---------------------------------------------------------------------------

def PreprocessData(df):

    df = df.drop(
        ["Passengerid",
         "zero",
         "name"],
        axis=1,
        errors="ignore"
    )

    # Handle missing values

    df["Age"] = df["Age"].fillna(df["Age"].median())

    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(
        df["Embarked"].mode()[0]
    )

    # Convert categorical data into numerical data

    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )

    print("Data Preprocessing Completed")
    print(df.head())

    return df


# ---------------------------------------------------------------------------
#   Function Name: SplitData
#   Description :  It performs splitting activity
#   Input :        DataFrame
#   Output :       Training and testing data
# ---------------------------------------------------------------------------

def SplitData(df):

    X = df.drop("Survived", axis=1)

    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Data Set Splitting Successfully")

    return X_train, X_test, Y_train, Y_test


# ---------------------------------------------------------------------------
#   Function Name: Trainmodel
#   Description :  It performs model training
#   Input :        Training features and target
#   Output :       Trained model
# ---------------------------------------------------------------------------

def Trainmodel(X_train, Y_train):

    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train, Y_train)

    print("Model Trained Successfully")

    return model


# ---------------------------------------------------------------------------
#   Function Name: Evaluatemodel
#   Description :  It performs model testing
#   Input :        Model, testing features and target
#   Output :       None
# ---------------------------------------------------------------------------

def Evaluatemodel(model, X_test, Y_test):

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy :", accuracy * 100, "%")

    print("Confusion Matrix :")
    print(confusion_matrix(Y_test, Y_pred))


# ---------------------------------------------------------------------------
#   Function Name: Main
#   Description :  Entry Point Function
#   Input :        None
#   Output :       None
# ---------------------------------------------------------------------------

def main():

    # Step 1 : Load Data

    df = DataLoad("MarvellousTitanicDataset.csv")

    # Step 2 : Preprocess Data

    df = PreprocessData(df)

    # Step 3 : Split Data

    X_train, X_test, Y_train, Y_test = SplitData(df)

    # Step 4 : Train Model

    model = Trainmodel(X_train, Y_train)

    # Step 5 : Evaluate Model

    Evaluatemodel(model, X_test, Y_test)


if __name__ == "__main__":
    main()
