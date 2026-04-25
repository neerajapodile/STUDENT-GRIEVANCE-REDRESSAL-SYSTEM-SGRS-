# WEEK 12

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- SAMPLE DATA ----------------

data = {
    "Department": ["CSE", "ECE", "MECH", "CSE", "ECE", "CSE"],
    "Category": ["Academic", "Exam", "Hostel", "Fees", "Academic", "Exam"],
    "Status": ["Resolved", "Pending", "Resolved", "Pending", "Resolved", "Pending"],
    "Days": [2, 5, 3, 6, 1, 4]
}

df = pd.DataFrame(data)

print("\nFULL DATAFRAME")
print(df)

# ---------------- NUMPY ----------------

days_array = np.array(df["Days"])

print("\nAverage Resolution Days :", np.mean(days_array))
print("Maximum Days :", np.max(days_array))
print("Minimum Days :", np.min(days_array))

# ---------------- PANDAS GROUPBY ----------------

print("\nCATEGORY COUNT")
print(df.groupby("Category").size())

print("\nDEPARTMENT COUNT")
print(df.groupby("Department").size())

print("\nSTATUS COUNT")
print(df.groupby("Status").size())

# ---------------- BAR CHART ----------------

category_count = df["Category"].value_counts()

plt.bar(category_count.index, category_count.values)
plt.title("Category Wise Grievances")
plt.xlabel("Category")
plt.ylabel("Count")
plt.show()

# ---------------- PIE CHART ----------------

status_count = df["Status"].value_counts()

plt.pie(status_count.values,
        labels=status_count.index,
        autopct="%1.1f%%")

plt.title("Status Distribution")
plt.show()

# ---------------- LINE CHART ----------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
counts = [5, 8, 6, 10, 7]

plt.plot(months, counts, marker="o")
plt.title("Monthly Grievance Trend")
plt.xlabel("Month")
plt.ylabel("Count")
plt.show()
