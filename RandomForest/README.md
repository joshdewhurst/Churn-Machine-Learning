# Random Forest Classifier

This program uses a random forest classifier to predict customer churn based on a set of features. The classifier is built using scikit-learn and the performance of the classifier is evaluated using metrics such as accuracy, precision and recall.

## Dependencies
This program requires the following dependencies to be installed:

* pandas
* scikit-learn

These dependencies can be installed using pip:
`pip install pandas scikit-learn`

# Usage
1. Clone this repo
2. Run `python3 RandomForest.py`

## Input Data
The input data should be in a CSV file named customer_data.csv. The file should contain the following columns:

* **usage_frequency**: The frequency of product usage by the customer.
* **account_status**: The status of the customer's account. This should be a categorical variable with two possible values: "active" or "inactive".
* **other_behavioral_data**: Other behavioral data about the customer.
The target variable that we want to predict is churn, which indicates whether or not the customer has churned.

# Output
The program will output the predictions for the new data set provided in the new_data.csv file. The output will be a list of binary values, where 1 indicates that the customer is predicted to churn, and 0 indicates that the customer is predicted to stay.

# Explanation
The program works by first loading the data from the `customer_data.csv` file and splitting it into training and testing sets. The training set is used to train a random forest classifier using the scikit-learn library. The model is then used to predict churn on the testing set and evaluate the performance of the model using metrics such as accuracy, precision and recall.

Finally, the program loads a new data set from the `new_data.csv` file, preprocesses it using the same methods as the original data, and uses the trained random forest classifier to predict churn for the new data set. The predicted churn values are then printed to the console.

To test the program, simply run the `RandomForest.py` file as described above. The program will output the predicted churn values for the new data set provided in the `new_data.csv` file. You can modify the input data by editing the `customer_data.csv` and `new_data.csv` files to include your own data.
