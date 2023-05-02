# Import required libraries
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('customer_data.csv')

# Rename the column to match the one-hot encoding column name
data = data.rename(columns={'status': 'account_status'})

# One-hot encode the categorical features
data = pd.get_dummies(data, columns=['account_status'], drop_first=True)


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
