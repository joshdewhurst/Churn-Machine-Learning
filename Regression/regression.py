import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the data
data = pd.read_csv('customer_data.csv')

# Map the 'Yes' and 'No' values to 1 and 0 for the 'status' column
data['status'] = data['status'].map({'Yes': 1, 'No': 0})

# Select the features and target variable
X = data[['usage_frequency', 'status', 'other_behavioral_data']]

# Fit the logistic regression model on the entire dataset
lr = LogisticRegression()
lr.fit(X, data['churn'])

# Make predictions on the dataset
y_pred = lr.predict(X)

# Add the predicted churn values to the DataFrame as a new column
data['churn_prediction'] = y_pred

# Write the updated DataFrame to a new CSV file
data.to_csv('customer_data_predicted.csv', index=False)

# Evaluate the model's performance
accuracy = lr.score(X_test, y_test)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

# Print the predicted values
print(y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
