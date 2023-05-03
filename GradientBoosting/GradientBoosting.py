# Import required libraries
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the data
data = pd.read_csv('customer_data.csv')

# Drop the id column
data = data.drop(['id'], axis=1)

# Encode categorical features using one-hot encoding
data = pd.get_dummies(data, columns=['account_status', 'other_behavioral_data'])

# Select the features and target variable
X = data.drop(['churn'], axis=1)
y = data['churn']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the gradient boosting model
model = GradientBoostingClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)

# Load the new data
new_data = pd.read_csv('new_customer_data.csv')

# Drop the id column
new_data = new_data.drop(['id'], axis=1)

# Encode categorical features using one-hot encoding
new_data = pd.get_dummies(new_data, columns=['account_status', 'other_behavioral_data'])

# Select the features
X_new = new_data.drop(['churn'], axis=1)

# Make predictions on the new data
y_pred = model.predict(X_new)

# Print the predicted churn values
print("Predicted churn values:")
print(y_pred)
