# 🏭 Time-Series Datasets for Reliability Engineering & Industrial Maintenance

This repository curates **publicly available datasets** that support two primary use cases:
- **Reliability Engineering** → degradation modeling, survival analysis, Remaining Useful Life (RUL) prediction.  
- **Industrial Maintenance** → predictive maintenance, condition monitoring, anomaly detection.  

All dataset links were verified as of **August 2025**.

---

## 📂 Dataset Library

| Dataset | Domain / Type | Applications | Highlights |
|---------|---------------|--------------|-------------|
| [✈️ C-MAPSS (Turbofan Engine Simulation)](https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data) | Simulated aircraft engines | RUL prediction, degradation modeling | Standard in prognostics research, multi-scenario simulations |
| [🚆 MetroPT-3 (Air Compressor)](https://archive.ics.uci.edu/dataset/791/metropt%2B3%2Bdataset) | Metro train compressor | Predictive maintenance, anomaly detection | Real sensor data (15 signals at 1 Hz), failure reports included |
| [🎛 NASA Prognostics Data Repository](https://data.phmsociety.org/nasa/) | Various run-to-failure experiments | Reliability & prognostics across components | Bearings, composites, milling, batteries, turbofan, etc. |
| [📈 MetroPT (Zenodo/Nature)](https://www.nature.com/articles/s41597-022-01877-3) | Metro train APU with GPS | Predictive maintenance, anomaly benchmarking | Rich analog, digital, and GPS signals; labeled failures |

---

## 🚀 Usage Guide

- **For RUL & Reliability Research**:  
  Use **C-MAPSS** or datasets from the **NASA Prognostics Data Repository** for physics-based modeling and benchmarking.  

- **For Industrial Maintenance & Anomaly Detection**:  
  Use **MetroPT-3** or the richer **MetroPT (Zenodo/Nature)** dataset, which includes multiple sensor modalities and real operational fault data.

---

## 🤝 Contribution & Licensing

- **Contributions welcome!** Submit pull requests to add new datasets or example notebooks.  
- **Licenses vary per dataset** — please check each source before use in research or production.  

---

## ✅ Verified Availability (Aug 2025)

- **C-MAPSS** → accessible via NASA’s Open Data Portal.  
- **MetroPT-3** → available via UCI Machine Learning Repository.  
- **NASA PHM Repository** → multiple datasets downloadable via PHM Society.  
- **MetroPT (Zenodo/Nature)** → published in 2022 and accessible via Nature & Zenodo.  

---

## 🔎 Quick Summary

- **Reliability Engineering**:  
  • C-MAPSS (RUL/simulated engines)  
  • NASA PHM Repository (bearings, batteries, composites, etc.)  

- **Maintenance / Anomaly Detection**:  
  • MetroPT-3 (compressor logs)  
  • MetroPT (APU + GPS multimodal dataset)  
