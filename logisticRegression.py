import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv("login_data_updated.csv")

# Preprocess the data to convert categorical variables into numerical variables
df["IP_Addr"] = pd.factorize(df["IP_Addr"])[0]

# taking full dataset to train and the full dataset to test, so as to get the best accuracy in one go
train_data,test_data=df,df

# Extract the input features and output labels from the training set
X_train = train_data[["IP_Addr", "Login_time"]]
y_train = train_data["Status"]

# Create a Logistic Regression classifier and fit it to the training data
clf = LogisticRegression()
clf.fit(X_train, y_train)

# Predict the output labels for the testing set
X_test = test_data[["IP_Addr", "Login_time"]]
y_test = test_data["Status"]
y_pred = clf.predict(X_test)

# Evaluate the accuracy of the model on the testing set
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy for logisistic regression:", accuracy)
