import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# You should change file path as where you downloaded or where you are going to place at
df = pd.read_csv("data/StudentPerformance.csv")


# Cloumn check
print("Column names:", df.columns)

# Column name rep
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

print(" First 5 rows:\n", df.head(), "\n")
print(" Descriptive statistics:\n", df[["math_score","reading_score","writing_score"]].describe(), "\n")

print(" Average Scores by Gender:\n",
      df.groupby("gender")[["math_score","reading_score","writing_score"]].mean(), "\n")

print(" Average Scores by Lunch:\n",
      df.groupby("lunch")[["math_score","reading_score","writing_score"]].mean(), "\n")

print(" Average Scores by Test Preparation Course:\n",
      df.groupby("test_preparation_course")[["math_score","reading_score","writing_score"]].mean(), "\n")

sns.set(style="whitegrid")

plots_dir = os.path.join(os.path.dirname(__file__), "../plots")
os.makedirs(plots_dir, exist_ok=True)

subjects = ["math_score","reading_score","writing_score"]
for subj in subjects:
    plt.figure(figsize=(8,4))
    sns.histplot(df[subj], kde=True, bins=30, color="skyblue")
    plt.title(f"{subj.replace('_',' ').title()} Distribution")
    plt.xlabel(subj.replace('_',' ').title())
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(plots_dir, f"{subj}_distribution.png"))
    plt.show()


# . By Gender (Box Plot)
plt.figure(figsize=(18,5))
for i, subj in enumerate(subjects):
    plt.subplot(1,3,i+1)
    sns.boxplot(x="gender", y=subj, data=df, hue="gender", palette="Set2")
    plt.title(f"{subj.replace('_',' ').title()} by Gender")
    plt.xlabel("Gender")
    plt.ylabel(subj.replace('_',' ').title())
plt.tight_layout()

plt.show()

# By Lunch Type (Box Plot)
plt.figure(figsize=(18,5))
for i, subj in enumerate(subjects):
    plt.subplot(1,3,i+1)
    sns.boxplot(x="lunch", y=subj, data=df, hue="lunch", palette="Pastel1")
    plt.title(f"{subj.replace('_',' ').title()} by Lunch Type")
    plt.xlabel("Lunch")
    plt.ylabel(subj.replace('_',' ').title())
plt.tight_layout()

plt.show()

#  By Test Preparation Course (Violin Plot)
plt.figure(figsize=(18,5))
for i, subj in enumerate(subjects):
    plt.subplot(1,3,i+1)
    sns.violinplot(x="test_preparation_course", y=subj, data=df, hue="test_preparation_course", legend=False, palette="Set3")
    plt.title(f"{subj.replace('_',' ').title()} by Test Prep Course")
    plt.xlabel("Test Preparation")
    plt.ylabel(subj.replace('_',' ').title())
plt.tight_layout()

plt.show()