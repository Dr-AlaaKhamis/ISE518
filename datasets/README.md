# Datasets for Reliability and Maintenance

A curated collection of **publicly available datasets**—both from open repositories and Kaggle—for:

- **Reliability Engineering** → degradation modeling, survival analysis, Remaining Useful Life (RUL) prediction  
- **Industrial Maintenance** → predictive maintenance, condition monitoring, anomaly detection  

Each dataset link has been verified and is active as of August 2025.

---

##  Dataset Library

| Dataset | Domain / Type | Applications | Highlights |
|---------|---------------|--------------|-------------|
| [🔧 Machine Predictive Maintenance Classification (Kaggle)](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification) | Industrial machines (synthetic) | Failure classification | Includes machine operating parameters and failure types |
| [⏱ Predictive Maintenance Dataset AI4I 2020 (Kaggle)](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020) | Synthetic industrial machines | Classification, regression | Well-known UCI dataset republished on Kaggle |
| [⚙️ Machine Failure Prediction (Kaggle)](https://www.kaggle.com/datasets/saquib7hussain/machine-failure-prediction-dataset) | Industrial sensor data (synthetic) | Failure event prediction | Includes temperature, pressure, vibration, humidity, power consumption  |
| [💾 Hard Drive Reliability Data Set (Kaggle)](https://www.kaggle.com/datasets/thedevastator/hard-drive-reliability-data-set) | Storage hardware | Failure prediction | Real-world drive health data from Backblaze |
| [🤖 Preventive-to-Predictive Maintenance (Kaggle)](https://www.kaggle.com/datasets/prognosticshse/preventive-to-predicitve-maintenance) | Industrial scenarios | Prognostics & diagnostics | Created by Bosch for real-world maintenance benchmarking |
| [🛠️ Engine Failure Detection (Kaggle)](https://www.kaggle.com/datasets/ziya07/engine-failure-detection-dataset) | Engine sensor data | Predictive maintenance | Includes sensor readings and fault conditions  |
| [✈️ C-MAPSS (Turbofan Engine Simulation)](https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data) | Simulated aircraft engines | RUL prediction, degradation modeling | Benchmark dataset in prognostics research with multiple scenarios |
| [🚆 MetroPT-3 (Air Compressor)](https://archive.ics.uci.edu/dataset/791/metropt%2B3%2Bdataset) | Metro train compressor | Predictive maintenance, anomaly detection | Real sensor data (15 signals at 1 Hz) with failure events |
| [🎛 NASA Prognostics Data Repository](https://data.phmsociety.org/nasa/) | Run-to-failure experiments | Reliability & prognostics across components | Includes bearings, composites, milling, batteries, turbofan, etc. |
| [📈 MetroPT (Zenodo/Nature)](https://www.nature.com/articles/s41597-022-01877-3) | Train APU with GPS | Predictive maintenance, anomaly benchmarking | Multimodal sensor data with labeled anomalies |

---

## 📊 Sample Analytics Notebook

👉 To help you get started, we provide a **[sample Jupyter notebook](Sample.ipynb)**:

This notebook demonstrates **EDA** for the AI4I 2020 dataset (or similar CSVs):

- Load and inspect the dataset  
- Summary statistics and missing values  
- Class distribution plots  
- Histograms & boxplots for numeric features  
- Correlation heatmap (matplotlib)  
- Outlier checks  

You can easily adapt it to any dataset from the list above (e.g., MetroPT-3, C-MAPSS, or Kaggle datasets).

---

##  Contribution & Licensing

- **Contributions welcome!** Feel free to submit PRs to add new datasets or analysis examples.  
- **Licenses vary per dataset**—please review each source before using in academic or production settings.