import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("student_data.csv")

# Style
sns.set_style("whitegrid")

# Create Dashboard
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1. Student Marks
sns.barplot(
    x="Name",
    y="Marks",
    data=df,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Student Marks Analysis", fontsize=14, fontweight="bold")
axes[0, 0].set_ylabel("Marks")
axes[0, 0].set_ylim(0, 100)

# 2. Student Attendance
sns.barplot(
    x="Name",
    y="Attendance",
    data=df,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Student Attendance Analysis", fontsize=14, fontweight="bold")
axes[0, 1].set_ylabel("Attendance (%)")
axes[0, 1].set_ylim(0, 100)

# 3. Attendance vs Marks
sns.scatterplot(
    x="Attendance",
    y="Marks",
    data=df,
    s=150,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Attendance vs Marks", fontsize=14, fontweight="bold")
axes[1, 0].set_xlabel("Attendance (%)")
axes[1, 0].set_ylabel("Marks")

# 4. Marks Distribution
sns.histplot(
    df["Marks"],
    bins=5,
    kde=True,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Marks Distribution", fontsize=14, fontweight="bold")
axes[1, 1].set_xlabel("Marks")
axes[1, 1].set_ylabel("Number of Students")

# Dashboard title
fig.suptitle(
    "Student Performance Dashboard",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save image for website
plt.savefig("dashboard.png", dpi=300)

# Show dashboard
plt.show()