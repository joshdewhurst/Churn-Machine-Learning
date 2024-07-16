# Churn-Machine-Learning

In this project, I developed a predictive model to identify employees who are at risk of churning, using machine learning algorithms. This work was instrumental in my current HR role, helping to uncover underlying factors contributing to employee churn and enabling targeted interventions to reduce churn rates by 8%.

## Overview

To begin, I utilized demo data on employee behavior, such as tenure, performance metrics, and engagement levels, which was previously analyzed using spreadsheet tools like Excel or Google Sheets.

I implemented machine learning algorithms such as logistic regression, decision trees, neural networks, gradient boosting, and random forests to create a predictive model that can identify which employees are most likely to churn. The model was trained using historical data and evaluated for accuracy and performance on a holdout set of data.

The insights from the predictive model were crucial in identifying key factors influencing employee churn. As a result, I was able to implement strategies that reduced churn by 8% across the organization. The linked GitHub repository provides an overview of the code used to identify these trends. Due to confidentiality, the exact code cannot be shared.

## Code and Approach

I used Python for this project, creating separate folders for each of the following machine learning algorithms:

1. Decision Trees
2. Neural Networks
3. Gradient Boosting
4. Random Forests
5. Logistic Regression

### Decision Trees

Decision trees are a type of supervised learning algorithm used for classification and regression. In this approach, a tree-like model is built where each internal node represents a test on an attribute, each branch represents the outcome of the test, and each leaf node represents a class label. The goal is to create a model that predicts the value of a target variable based on several input variables.

In the Decision Trees folder, I implemented the decision tree algorithm using the scikit-learn library. The README file in the folder explains the code and how the algorithm works in detail.

### Neural Networks

Neural networks are a set of algorithms modeled after the human brain. They are used to recognize patterns and to cluster and classify data. Neural networks consist of layers of interconnected nodes that process information, with each layer processing information in a hierarchical way.

In the Neural Networks folder, I implemented a simple neural network using the TensorFlow library. The README file in the folder explains the code and how the algorithm works in detail.

### Gradient Boosting

Gradient Boosting is a machine learning technique used for regression and classification problems. It builds an ensemble of weak learners (usually decision trees) and combines them to produce a strong learner. The model is built in a stage-wise manner, with each subsequent model trying to correct the errors of the previous model.

In the Gradient Boosting folder, I implemented the gradient boosting algorithm using the XGBoost library. The README file in the folder explains the code and how the algorithm works in detail.

### Random Forests

Random Forests are a type of ensemble learning method that combine multiple decision trees to improve the accuracy of the model. In a random forest, each tree is built on a random sample of the data and a random subset of the features. The final prediction is then made by aggregating the predictions of all the trees.

In the Random Forests folder, I implemented the random forest algorithm using the scikit-learn library. The README file in the folder explains the code and how the algorithm works in detail.

### Logistic Regression

Logistic Regression is a type of regression analysis used to predict the outcome of a categorical dependent variable based on one or more independent variables. It is a simple and widely used algorithm for binary classification problems.

In the Logistic Regression folder, I implemented the logistic regression algorithm using the scikit-learn library. The README file in the folder explains the code and how the algorithm works in detail.

## Further Applications

The techniques used in this project can be applied to many other domains such as finance, healthcare, and marketing. By predicting employee churn, organizations can take proactive steps to retain their employees and improve overall organizational health and performance.
