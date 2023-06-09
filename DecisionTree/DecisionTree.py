# Import required libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the data
data = pd.read_csv('customer_data.csv')

# Select the features and target variable
X = data[['age', 'gender', 'income', 'credit_score', 'previous_purchases']]
y = data['churn']

# Convert the categorical variable gender to numerical using one-hot encoding
X = pd.get_dummies(X, columns=['gender'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit the decision tree model
dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)

# Make predictions on the test set
y_pred = dt.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recal:", recall)

# Load the new data
new_data = pd.read_csv('new_data.csv')

# Select the features in the same order as the model was trained on
X_new = new_data[['age', 'gender', 'income', 'credit_score', 'previous_purchases']]

# Convert the categorical variable gender to numerical using one-hot encoding
X_new = pd.get_dummies(X_new, columns=['gender'])

# Make predictions on the new data
y_pred_new = dt.predict(X_new)

# Print the predicted values
print("Predicted values for new data:")
print(y_pred_new)
