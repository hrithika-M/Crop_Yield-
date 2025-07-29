# Crop_Yield-
This project focuses on performing statistical hypothesis testing using independent two-sample t-tests to evaluate the effect of water levels on crop yield under different fertilizer conditions. The goal is to determine whether the variation in crop yield is statistically significant between high and low water usage within each fertilizer type.
# T-Test Crop Yield Analysis

This project is part of the "Computer Oriented Statistical Methods" coursework and explores the use of **independent two-sample t-tests** to analyze the effect of fertilizer type and water levels on crop yield using Python and scientific libraries.

---

## 📊 Dataset

The dataset (`crop_yield.csv`) contains:
- Fertilizer Type (`Fert`): A or B
- Water Level (`Water`): High or Low
- Crop Yield (`Yield`): Measured yield value

---

## 🧪 Objective

To determine if there's a **statistically significant difference** in yield:
- Between high and low water levels within the same fertilizer type (A and B).

---

## 🔧 Libraries Used

- **Pandas** - Data manipulation
- **Scipy** - For performing the t-tests
- **Statsmodels** (for context)
- **Matplotlib / Seaborn** (for optional visualization)

---

## 🧬 Hypothesis

- **Null Hypothesis (H₀)**: There is **no significant difference** in yield between high and low water usage for a given fertilizer type.
- **Alternative Hypothesis (H₁)**: There **is a significant difference**.

---

## 🧑‍💻 Code Overview

The Jupyter notebook or Python script performs:
1. Data loading and preprocessing.
2. Splitting the dataset by Fertilizer and Water group.
3. Performing t-tests between high and low water groups.
4. Drawing statistical conclusions.

---

## 📈 Results

- **Group A**: p = 0.418 → Fail to reject H₀ (No significant difference)
- **Group B**: p = 0.047 → Reject H₀ (Significant difference)

---

## 📂 Files

- `crop_yield.csv` – The dataset
- `t_test_analysis.ipynb` – Code implementation in Jupyter
- `README.md` – Project description
- `crop_yield.docx` – Word document with detailed explanation

---

## 🧾 Author

**M. Hrithika**  
Roll No: 22XV1M6710
