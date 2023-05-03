# Decision Tree Classifier for Customer Churn Prediction
This Python code uses a Decision Tree Classifier to predict customer churn using customer demographic and purchase data. The program first loads the customer data from a CSV file, selects the relevant features and target variable, and then performs one-hot encoding to convert the categorical variable 'gender' into numerical data.

Next, the program splits the data into training and testing sets, and fits the decision tree model to the training data. The program then uses the trained model to make predictions on the testing set, and evaluates the performance of the model using accuracy, precision, and recall metrics.

Finally, the program loads new data from another CSV file, applies the same one-hot encoding to the 'gender' variable, and uses the trained model to make predictions on the new data.

## Testing the Code
To test the code, follow these steps:

1. Ensure that you have Python and the necessary libraries (pandas, scikit-learn) installed on your machine.

2, Download the "customer_data.csv" and "new_data.csv" files and save them in the same directory as the code.

3. Open your terminal and navigate to the directory where the code and data files are saved.

4. Type "python3" followed by the name of the file, and press enter. For example, if the file name is "DecisionTree.py", type:

`python3 DecisionTree.py`

5. Press enter to run the script. The program will load the customer data, split it into training and testing sets, fit a decision tree model, and evaluate its performance on the test set. It will then make predictions on the new data and print the predicted values.

6. Check the output in the terminal to see the accuracy, precision, and recall scores of the model on the test set, as well as the predicted values for the new data.

**Note**: You can modify the code to use your own dataset. Simply replace the "customer_data.csv" and "new_data.csv" files with your own data files, making sure that they are in the correct format (CSV) and that the feature names and order match the code.


# Other Applications

This code can be modified to apply the decision tree classifier to other datasets with similar features and target variables. It can also be extended to include other machine learning algorithms, such as random forests or support vector machines, to improve the predictive performance of the model.
