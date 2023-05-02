import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the data
data = pd.read_csv('customer_data.csv')

# Convert categorical variables to numerical format using one-hot encoding
data = pd.get_dummies(data, columns=['account_status'])

# Select the features and target variable
X = data.drop(['churn'], axis=1)
y = data['churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the random forest model
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# Load the new data
new_data = pd.read_csv('new_data.csv')

# Convert categorical variables to numerical format using one-hot encoding
new_data = pd.get_dummies(new_data, columns=['account_status'])

# Make predictions on the new data set
X_new = new_data  # rename the variable for consistency
y_pred_new = rf.predict(X_new)

# Print the predictions
print(y_pred_new)
