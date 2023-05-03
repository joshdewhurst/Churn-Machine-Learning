# Churn-Machine-Learning

In this project, I will be developing a predictive model to identify customers who are at risk of churning, using machine learning algorithms.

To begin, I will utilize demo data on customer behavior, such as the frequency of usage, the types of features used, and the length of time since they last used the service, which was previously analyzed using spreadsheet tools like Excel or Google Sheets.

I will then implement machine learning algorithms such as logistic regression, decision trees, and random forests to create a predictive model that can identify which customers are most likely to churn. I will train the model using historical data and evaluate its accuracy and performance on a holdout set of data.

Finally, I will use the insights from the predictive model to take proactive steps to retain customers who are at risk of churning. These actions could include targeted emails or special promotions to incentivize them to continue using the service.

By using machine learning algorithms, I will develop a powerful predictive model that helps to retain customers and improve the overall health of the business. While I will not be creating pivot tables in this project, I will still utilize previously conducted spreadsheet analysis to inform my approach.

# Logistic Regression

In this code, we first import the necessary libraries (pandas, scikit-learn's logistic regression model, and the train_test_split function for splitting the data into training and testing sets).

We then load the data from a CSV file and select the relevant features and target variable. We split the data into training and testing sets using the train_test_split function.

We then create an instance of the logistic regression model and fit it to the training data using the fit method. We then use the predict method to make predictions on the test set.

Finally, we evaluate the performance of the model using metrics like accuracy, precision, and recall.

# Decision Tree

In this code, we first import the necessary libraries (pandas, scikit-learn's decision tree model, and the train_test_split function for splitting the data into training and testing sets).

We then load the data from a CSV file and select the relevant features and target variable. We split the data into training and testing sets using the train_test_split function.

We then create an instance of the decision tree classifier and fit it to the training data using the fit method. We then use the predict method to make predictions on the test set.

Finally, we evaluate the performance of the model using metrics like accuracy, precision, and recall.

## How to run this code

1. Ensure that the required libraries are installed. You can use pip to install them if they are not already installed:
`pip install pandas scikit-learn`

2. Create a CSV file with customer data. The file should have columns for usage_frequency, account_status, other_behavioral_data, and churn.

3. Save the CSV file in the same directory as the Python script and name it customer_data.csv.

4. Run the Python script. It will load the customer data from the CSV file, split it into training and testing sets, fit a decision tree model to the training set, make predictions on the testing set, and evaluate the model's performance.

5. The script will output the accuracy, precision, and recall scores for the model. You can use these scores to evaluate how well the model is performing.

# Random Forest

This loads customer data from a CSV file, trains a Random Forest Classifier model on the data, and evaluates the model's performance by comparing the predicted target variable with the actual target variable. The goal of the model is to predict which customers are most likely to churn.

# Gradient Boosting
This builds a predictive model using a Gradient Boosting Classifier from the scikit-learn library. The code loads the customer data from a CSV file, selects the relevant features and target variable, splits the data into training and testing sets, fits the gradient boosting model to the training data, makes predictions on the test set, and evaluates the model's performance using accuracy, precision, and recall metrics. The model is trained to identify which customers are most likely to churn based on their usage frequency, account status, and other behavioral data.

# Neutrel Network

This code builds a predictive model using a multi-layer perceptron (MLP) neural network from the scikit-learn library. The code loads the customer data from a CSV file, selects the relevant features and target variable, splits the data into training and testing sets, defines the neural network architecture, fits the model to the training data, makes predictions on the test set, and evaluates the model's performance using accuracy, precision, and recall metrics.
