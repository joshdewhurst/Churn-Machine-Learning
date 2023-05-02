# Import required libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.neural_network import MLPClassifier

# Load the data
data = np.loadtxt("customer_data.csv", delimiter=",")

# Select the features and target variable
X = data[:,0:3]
y = data[:,3]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the neural network architecture
model = MLPClassifier(hidden_layer_sizes=(8, 4), activation='relu', solver='adam', random_state=42)

# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:" accuracy)
print("Precision:" precision)
print("Recall:" accuracy)
