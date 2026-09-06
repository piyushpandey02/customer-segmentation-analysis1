# Customer Segmentation using K-Means Clustering

##  Project Overview

This project addresses the business need to move from a "one-size-fits-all" marketing strategy to a targeted, data-driven approach. By analyzing transactional data, this analysis identifies distinct customer groups based on their purchasing behavior. The resulting segments enable the company to create personalized and cost-effective marketing campaigns, improving customer retention and maximizing ROI.

The core methodology involves **RFM (Recency, Frequency, Monetary) analysis** for feature engineering and the **K-Means clustering** algorithm to group customers into actionable segments.

---

##  Dataset

The analysis uses the **Online Retail Dataset** from the UCI Machine Learning Repository.

-   **Source:** [UCI Machine Learning Repository: Online Retail Data Set](https://archive.ics.uci.edu/ml/datasets/online+retail)
-   **Description:** This is a transnational dataset that contains all the transactions occurring between 12/01/2010 and 12/09/2011 for a UK-based online retail company.

---

##  Setup and Installation

To run this project on your local machine, follow these steps:

1.  **Clone the repository (if applicable) or download the source code.**

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

---

##  How to Run the Project

You can run the analysis in two ways:

1.  **Exploratory Walkthrough (Jupyter Notebooks):**
    For a detailed, step-by-step analysis with explanations and visualizations, run the notebooks in the `notebooks/` directory in the following order:
    - `01_data_exploration_and_cleaning.ipynb`
    - `02_rfm_modeling_and_segmentation.ipynb`

2.  **Automated Script:**
    To run the entire pipeline from raw data to final segmented output automatically, execute the following command in your terminal from the project's root directory:
    ```bash
    python scripts/run_segmentation.py
    ```
    The final output will be saved in `data/processed/`.

---

##  Key Findings: Customer Segments

The analysis successfully identified 3 distinct and actionable customer segments:

-   ** High-Value Champions:** These are the most loyal and profitable customers. They buy frequently, spend the most, and have purchased very recently.
    -   **Strategy:** Retain and reward. Offer loyalty programs, exclusive access, and VIP perks.

-   ** At-Risk Spenders:** This group consists of valuable customers who used to spend and purchase regularly but haven't done so in a while.
    -   **Strategy:** Re-engage and prevent churn. Target them with personalized "we miss you" campaigns and special offers.

-   ** New or Lapsed Customers:** These customers have low frequency and monetary value, and a high recency score (they haven't shopped in a long time). This group includes new customers and those who have become inactive.
    -   **Strategy:** Nurture and reactivate. Use welcome email series for new customers and win-back campaigns for lapsed ones.

### Segment Visualization
![Customer Segments Plot](Reports/Figures/customer_segments(1).png)


---
##  Technologies Used

-   **Python**
-   **Pandas** (for data manipulation)
-   **NumPy** (for numerical operations)
-   **Scikit-learn** (for K-Means clustering)
-   **Matplotlib & Seaborn** (for data visualization)
-   **Jupyter Notebook** (for exploratory analysis)
