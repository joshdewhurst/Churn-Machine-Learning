# Logical Regression
Below is an explanation of analyzing Customer Churn using Logical Regression

## Explanation of the `Regression.py` code
* Import the necessary libraries: pandas for data manipulation, scikit-learn for machine learning algorithms.

* Load the data from a CSV file called 'customer_data.csv' using pandas' read_csv function.

* Define the feature matrix X and target vector y. The feature matrix is a subset of the columns in the data, containing 'usage_frequency', 'account_status', and 'other_behavioral_data'. The target vector contains the 'churn' column.

* Split the data into training and testing sets using the train_test_split function from scikit-learn. The testing set size is set to 20% of the total data, and the random_state parameter is set to 42 for reproducibility.

* Fit a logistic regression model to the training data using scikit-learn's LogisticRegression class.

* Use the trained model to make predictions on the testing data by calling the predict function on the fitted logistic regression model.

* Evaluate the model's performance on the testing set. The accuracy score is computed using the score function on the fitted logistic regression model. The precision and recall scores are computed using the precision_score and recall_score functions from the metrics module of scikit-learn.

# Explanation of CSV columns:

1. usage_frequency: This column represents how often the customer uses the service or product offered by the company. The values are numerical and can range from 1 to 6.5, with higher values indicating a more frequent usage of the service.
2. account_status: This column represents the current status of the customer's account. The values can either be "Active" or "Inactive", indicating whether the customer is actively using the service or not.
3. other_behavioral_data: This column represents additional behavioral data about the customer that might be relevant to predicting churn. The values can either be "Yes" or "No".
4. churn: This column represents whether the customer has churned or not. The values can either be "Yes" or "No", with "Yes" indicating that the customer has churned and "No" indicating that the customer is still using the service.
