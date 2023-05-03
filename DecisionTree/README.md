# Decision Tree Classifier for Customer Churn Prediction
This Python code uses a Decision Tree Classifier to predict customer churn using customer demographic and purchase data. The program first loads the customer data from a CSV file, selects the relevant features and target variable, and then performs one-hot encoding to convert the categorical variable 'gender' into numerical data.

Next, the program splits the data into training and testing sets, and fits the decision tree model to the training data. The program then uses the trained model to make predictions on the testing set, and evaluates the performance of the model using accuracy, precision, and recall metrics.

Finally, the program loads new data from another CSV file, applies the same one-hot encoding to the 'gender' variable, and uses the trained model to make predictions on the new data.

## Testing the Code
To test the code, you need to have two CSV files: customer_data.csv and new_data.csv. customer_data.csv should contain the customer demographic and purchase data, including the target variable 'churn'. new_data.csv should contain the same features as customer_data.csv, but without the 'churn' variable.

Follow these steps to run the program:

1. Install the required libraries: `pandas` `scikit-learn`
2. Save the `customer_data.csv` and `new_data.csv` files in the same directory as the program.
3. Open the Python code editor of your choice and copy the code into a new file.
4. Run the program and examine the output. The program should display the accuracy, precision, and recall metrics of the trained model, as well as the predicted values for the new data.

# Other Applications

This code can be modified to apply the decision tree classifier to other datasets with similar features and target variables. It can also be extended to include other machine learning algorithms, such as random forests or support vector machines, to improve the predictive performance of the model.
