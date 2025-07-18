# 📈 Task 3: Data Visualization – HR Analytics

## 🔍 Objective

The objective of this task is to transform raw HR data into meaningful visual insights.  
Using charts and graphs, we aim to highlight important relationships and patterns related to employee attrition.

---

## 🧰 Tools & Libraries Used

- Python
- Jupyter Notebook
- matplotlib
- seaborn
- pandas

---

## 📑 Dataset Summary

- Dataset: `WA_Fn-UseC_-HR-Employee-Attrition.csv`
- Rows: 1,470 employees
- Key Columns:
  - Attrition
  - Department
  - Gender
  - OverTime
  - Age
  - MonthlyIncome
  - JobSatisfaction
  - JobRole

---

## 📊 Visualizations Included

| # | Visualization | Description |
|---|---------------|-------------|
| 1 | Attrition Count | Shows how many employees left vs. stayed |
| 2 | Attrition by Department | Reveals which departments have higher turnover |
| 3 | Attrition by Overtime | Highlights impact of overtime on leaving |
| 4 | Job Satisfaction Distribution | Compares satisfaction among those who left vs. stayed |
| 5 | Monthly Income by Job Role | Displays income spread across roles |
| 6 | Correlation Heatmap | Numeric feature correlation including attrition |

---

## 📈 Sample Visuals (Descriptions)

### ✔️ Attrition by Department
```python
sns.countplot(x='Department', hue='Attrition', data=df)
