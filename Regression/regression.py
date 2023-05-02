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

# Evaluate the model's performance
accuracy = lr.score(X_test, y_test)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# Load the data
new_data = pd.read_csv('new_data.csv')

# Preprocess the data (if necessary) - this should include the same preprocessing steps used on the training data
new_data['status'] = new_data['status'].map({'Yes': 1, 'No': 0})

# Select the features
X_new = new_data[['usage_frequency', 'status', 'other_behavioral_data']]

# Load the trained logistic regression model
lr = LogisticRegression()

# Fit the logistic regression model to the training data
lr.fit(X_train, y_train)

# Make predictions on the new data set
y_pred_new = lr.predict(X_new)

# Print the predictions
print(y_pred_new)
