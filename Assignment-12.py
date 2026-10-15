import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("customer_churn.csv")

print("Dataset Preview")
print(data.head())

print("\nDataset Details")
data.info()

print("\nNull Values in Each Column")
print(data.isna().sum())

if "Age" in data.columns:
    data["Age"] = data["Age"].fillna(data["Age"].median())

if "MonthlyCharges" in data.columns:
    data["MonthlyCharges"] = data["MonthlyCharges"].fillna(
        data["MonthlyCharges"].median()
    )

if "InternetService" in data.columns:
    data["InternetService"] = data["InternetService"].fillna(
        data["InternetService"].mode()[0]
    )

data = data.drop_duplicates()

print("\nStatistical Summary")
print(data.describe())

print("\nNumber of Customers in Each Churn Category")
print(data["Churn"].value_counts())

print("\nChurn Rate in Percentage")
print((data["Churn"].value_counts(normalize=True) * 100).round(2))

print("\nMonthly Charges Based on Churn")
print(data.groupby("Churn")["MonthlyCharges"].mean())

print("\nCustomer Tenure Based on Churn")
print(data.groupby("Churn")["Tenure"].mean())

churn_data = data["Churn"].value_counts()

churn_data.plot(kind="bar", color="skyblue")
plt.title("Customer Churn Analysis")
plt.xlabel("Churn Status")
plt.ylabel("Customer Count")
plt.tight_layout()
plt.show()

data.boxplot(column="MonthlyCharges", by="Churn")
plt.title("Monthly Charges by Churn Status")
plt.suptitle("")
plt.xlabel("Churn Status")
plt.ylabel("Monthly Charges")
plt.tight_layout()
plt.show()

data.boxplot(column="Tenure", by="Churn")
plt.title("Tenure Comparison by Churn Status")
plt.suptitle("")
plt.xlabel("Churn Status")
plt.ylabel("Tenure")
plt.tight_layout()
plt.show()

contract_data = pd.crosstab(data["Contract"], data["Churn"])
contract_data.plot(kind="bar")
plt.title("Contract Type and Churn")
plt.xlabel("Contract Type")
plt.ylabel("Customer Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

internet_data = pd.crosstab(data["InternetService"], data["Churn"])
internet_data.plot(kind="bar")
plt.title("Internet Service and Churn")
plt.xlabel("Internet Service")
plt.ylabel("Customer Count")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()