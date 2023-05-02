# Logical Regression

Logistic Regression is a statistical method used for binary classification problems, where the dependent variable (target variable) is binary, taking values of 0 or 1. The goal of Logistic Regression is to find a relationship between the independent variables (features) and the binary dependent variable, by estimating the probability of the target variable being 1, given the values of the independent variables.

In the context of customer churn analysis, Logistic Regression can be used to identify the factors that contribute to a customer's decision to leave a service or product, based on the features that may be relevant to the customer's behavior, such as usage frequency, account status, and other behavioral data. The logistic regression algorithm will generate a model that predicts the probability of a customer churning based on these features, allowing businesses to identify the most important factors that contribute to churn and develop strategies to retain customers.

To use the Logistic Regression algorithm to analyze customer churn, a dataset with relevant features such as usage frequency, account status, and other behavioral data can be collected and prepared. The data can then be split into training and testing sets, with the training set used to train the model, and the testing set used to evaluate its performance. The Logistic Regression model can be fit to the training data, and the resulting model can be used to predict the probability of churn for new customers. The model's performance can be evaluated by measuring its accuracy, precision, and recall on the testing set. By analyzing the model's coefficients, businesses can identify the most important factors that contribute to customer churn and develop targeted strategies to retain customers.

# Test this code
Here's a step-by-step guide on how to use the code to analyze customer churn:

* **Prepare the CSV file**: You'll need to have a CSV file containing customer data, with one row per customer and columns for various features like usage frequency, account status, and other behavioral data. The last column of the CSV file should be the "churn" column, which indicates whether or not each customer has churned (i.e., stopped using your product or service). One has already been provided as a guide in this repo.

* **Save the CSV file in your working directory**: Save the CSV file in the same directory as the Python script containing the code.

* **Open the Python script and check the libraries**: Make sure that the required libraries (pandas, scikit-learn) are installed and imported at the beginning of the code.

* **Update the CSV filename**: Update the line of code that loads the CSV file with the name of your file: data = pd.read_csv('customer_data.csv')

* **Update the feature and target variable columns**: Update the line of code that selects the features and target variable with the names of the columns in your CSV file that correspond to these variables: X = data[['usage_frequency', 'account_status', 'other_behavioral_data']] and y = data['churn']

* **Run the code**: Once you've made these changes, run the code to fit the logistic regression model, make predictions on the test set, and evaluate the model's performance using metrics like accuracy, precision, and recall.


**To run the code, you'll need to follow these steps: **

1. Make sure you have Python installed on your computer.
2. Open a text editor (e.g., Atom, Sublime Text, VS Code) and create a new file.
3. Copy the code provided into the file.
4. Save the file with a .py extension
5. Save the CSV file with customer data in the same directory as the Python script.
6. Open a command prompt or terminal window and navigate to the directory where the Python script and CSV file are saved.
7. Type "python regression.py" and hit Enter to run the script.
8. The script will execute and print the results to the console.

* **Interpret the results**: The output of the code will include the accuracy, precision, and recall scores, which will give you an idea of how well the logistic regression model is predicting customer churn based on the selected features. You can use these scores to guide your decisions about which customers to target with retention strategies, and to refine your understanding of which features are most predictive of churn in your customer base.

## Explanation of the `Regression.py` code
* Import the necessary libraries: pandas for data manipulation, scikit-learn for machine learning algorithms.

* Load the data from a CSV file called 'customer_data.csv' using pandas' read_csv function.

* Define the feature matrix X and target vector y. The feature matrix is a subset of the columns in the data, containing 'usage_frequency', 'account_status', and 'other_behavioral_data'. The target vector contains the 'churn' column.

* Split the data into training and testing sets using the train_test_split function from scikit-learn. The testing set size is set to 20% of the total data, and the random_state parameter is set to 42 for reproducibility.

* Fit a logistic regression model to the training data using scikit-learn's LogisticRegression class.

* Use the trained model to make predictions on the testing data by calling the predict function on the fitted logistic regression model.

* Evaluate the model's performance on the testing set. The accuracy score is computed using the score function on the fitted logistic regression model. The precision and recall scores are computed using the precision_score and recall_score functions from the metrics module of scikit-learn.

# Explanation of CSV columns:

1. **usage_frequency**: This column represents how often the customer uses the service or product offered by the company. The values are numerical and can range from 1 to 6.5, with higher values indicating a more frequent usage of the service.
2. **account_status**: This column represents the current status of the customer's account. The values can either be "Active" or "Inactive", indicating whether the customer is actively using the service or not.
3. **other_behavioral_data**: This column represents additional behavioral data about the customer that might be relevant to predicting churn. The values can either be "Yes" or "No".
4. **churn**: This column represents whether the customer has churned or not. The values can either be "Yes" or "No", with "Yes" indicating that the customer has churned and "No" indicating that the customer is still using the service.
