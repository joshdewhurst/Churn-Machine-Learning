# Import required libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_score, recall_score


# Load the data
data = pd.read_csv('customer_data.csv')

data['status'] = data['status'].map({'Yes': 1, 'No': 0})


# Select the features and target variable
X = data[['usage_frequency', 'status', 'other_behavioral_data']]
y = data['churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the logistic regression model
lr = LogisticRegression()
lr.fit(X_train, y_train)

# Make predictions on the test set
y_pred = lr.predict(X_test)

# Predict the values of y for new data points
new_data = pd.read_csv('new_data.csv')
new_data['status'] = new_data['status'].map({'Yes': 1, 'No': 0})
X_new = new_data[['usage_frequency', 'status', 'other_behavioral_data']]
y_pred = lr.predict(X_new)

# Evaluate the model's performance
accuracy = lr.score(X_test, y_test)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

