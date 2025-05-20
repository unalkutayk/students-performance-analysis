
#  Students Performance Analysis

This project performs exploratory data analysis (EDA) on student exam performance data. The dataset includes scores in Math, Reading, and Writing along with demographic and background information.

---

##  Project Structure

```
students-performance-analysis/
│
├── data/
│   └── StudentsPerformance.csv
│
├── src/
│   └── analysis.py
│
├── .gitignore
├── requirements.txt
└── README.md

```

---

##  How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/unalkutayk/students-performance-analysis.git
   cd students-performance-analysis
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # on Windows: .venv\Scripts\activate
   ```

3. Install requirements in terminal:
   ```bash
   pip install -r requirements.txt
   ```

4. Change the file path as yours:
   ```bash
   line 10: (students-performance-analysis/data/StudentsPerformance.csv) to (yours)
   ```

5. Run the analysis script:
   ```bash
    src/analysis.py
   ```

---
##  Objectives

- Load and explore the Students Performance dataset
- Clean and prepare the data
- Analyze performance based on:
   .Gender
   .Lunch type
   .Test preparation course
- Generate visualizations to better understand distributions and differences

##  Dataset Description

This dataset contains information on 1000 students and includes the following features:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score

Source: [Kaggle - Students Performance](https://www.kaggle.com/spscientist/students-performance-in-exams)


##  Technologies Used

Python
pandas
matplotlib
seaborn


##  Key Findings

Gender: Male students score higher in math, while females outperform in reading and writing.
Lunch type: Students with standard lunch perform significantly better overall.
Test preparation: Completing a test prep course correlates with higher scores in all subjects.


##  Author

- Unal Kutay KILIC
- GitHub: [unalkutayk]
- LinkedIn [https://www.linkedin.com/in/unalkutaykilic/]
