![image](https://github.com/user-attachments/assets/4f56ed8a-1bbe-4c4c-9839-ca618e43a3f8)

# Startup-Performance Analysis
Startup performance analysis is the process of evaluating a startup's financial health, market positioning, operational efficiency, and growth potential. This analysis helps identify strengths, weaknesses, opportunities, and threats (SWOT), guiding strategic decision-making.

Why we do it: The primary purpose is to ensure that the startup is on the right path to achieving its goals, whether that involves scaling, profitability, or market dominance. Performance analysis helps founders and stakeholders understand what is working and what needs improvement, enabling them to make informed decisions, optimize resources, and plan for the future.

Startup performance analysis benefits multiple stakeholders: Founders and management gain valuable insights to refine strategies, improve operations, and make data-driven decisions. Investors use the analysis to assess the startup's potential for return on investment (ROI), evaluate risks, and determine its viability for further funding. Employees benefit by understanding the company's direction and stability, enhancing job security and motivation. Customers indirectly gain from the startup's success through better products, services, and overall experience. Potential partners utilize the analysis to gauge the startup's market position, assessing the benefits of collaboration or partnerships.

### Overview

This project aims to predict whether a startup will be successful or fail, utilizing various machine learning techniques. The analysis focuses on identifying key factors that influence startup success, leveraging a dataset with 300 entries and 11 features, including funding amount, number of employees, funding rounds, and more.

The initial phase involved data preprocessing, which included handling missing values by filling in gaps in the 'No. of Employees' column with the mean. Outlier detection and treatment were performed using Z-scores and the Interquartile Range (IQR) method to minimize their impact on model training. Feature engineering also played a crucial role, resulting in new metrics like 'Funding per Employee' and Z-scores for critical financial indicators.

Exploratory Data Analysis (EDA) was conducted to visualize feature distributions and understand relationships through correlation analysis. Non-numeric columns, such as 'Description', were identified and excluded from the modeling process to ensure compatibility with machine learning algorithms.

The modeling phase involved splitting the dataset into training and testing sets and employing a Random Forest Classifier. The model achieved high accuracy, demonstrating its effectiveness in predicting startup success. To address class imbalance in the target variable, the Synthetic Minority Over-sampling Technique (SMOTE) was implemented.

Feature selection techniques, including Univariate Feature Selection and Recursive Feature Elimination (RFE), were explored to retain significant features and enhance model performance.

In conclusion, this project exemplifies a systematic approach to predicting startup success. The integration of data preprocessing, EDA, modeling, and feature selection provides a solid foundation for understanding success factors. Future work may focus on hyperparameter tuning, exploring additional modeling techniques, and refining feature engineering processes to further improve predictive accuracy.


### Dataset

The dataset used in this project is sourced from Kaggle and consists of 300 rows and 11 columns. If additional data is required, a synthetic dataset can be generated. To do this, run the "generate_data.py" file to create another CSV file, which can then be merged with the existing dataset for further analysis.

Dataset are is available in: [CrunchBase](https://www.crunchbase.com/discover/organization.companies),[PitchBook](https://pitchbook.com/).

### Perfromance
Random Forest Classifier has been worked well with the sourced data.

Future work could include hyperparameter tuning to optimize model performance, exploring additional machine learning algorithms, and refining feature engineering processes. Moreover, generating synthetic data may further enrich the analysis, providing a more comprehensive understanding of the startup landscape. Overall, this project lays a solid foundation for ongoing research into the dynamics of startup success, contributing to informed decision-making for entrepreneurs and investors alike.
