# ​ Time-Series Datasets for Reliability Engineering & Industrial Maintenance

This repository curates **publicly available datasets** that support two primary use cases:
- **Reliability Engineering**: Degradation modeling, survival analysis, Remaining Useful Life (RUL) prediction.
- **Industrial Maintenance**: Predictive maintenance, condition monitoring, anomaly detection.

Each dataset is verified for availability as of August 2025.

---

##  Dataset Library

| Dataset | Domain / Type | Applications | Highlights |
|---------|---------------|--------------|-------------|
| [✈️ C-MAPSS (Turbofan Engine Simulation)](https://data.nasa.gov/dataset/cmapss-jet-engine-simulated-data) | Simulated aircraft engines | RUL prediction, degradation modeling | Standard in prognostics research, multi-scenario simulations :contentReference[oaicite:1]{index=1} |
| [🚆 MetroPT-3 (Air Compressor)](https://archive.ics.uci.edu/dataset/791/metropt%2B3%2Bdataset) | Metro train compressor | Predictive maintenance, anomaly detection | Real sensor data (15 signals at 1 Hz), failure reports included :contentReference[oaicite:2]{index=2} |
| [🎛 NASA Prognostics Data Repository](https://data.phmsociety.org/nasa/) | Various runs-to-failure experiments | Reliability & prognostics across components | Bearings, CFRP composites, Milling, Batteries, Turbofan, etc. :contentReference[oaicite:3]{index=3} |
| [📈 MetroPT (Zenodo via Nature)](https://www.nature.com/articles/s41597-022-01877-3) | Metro train APU with GPS | Predictive maintenance, anomaly benchmarking | Rich analog, digital, and GPS signals from 2022; labeled failures :contentReference[oaicite:4]{index=4} |

---

##  Usage Guide

- **For RUL & Reliability Research**: Go with **C-MAPSS** or datasets from the **NASA Prognostics** repository for physics-based modeling and benchmark development.
- **For Industrial Maintenance & Anomaly Detection**: Use **MetroPT-3** or the richer **MetroPT via Nature/Zenodo**, with multiple sensor modalities and real operational faults.

---

##  Contribution & Licensing

- **Contributions welcome!** Feel free to submit pull requests to add new datasets or example notebooks.
- **Licenses vary per dataset**—please check each original source to ensure compliance with usage in research or production.

---

##  Notes on Dataset Availability

- **C-MAPSS**: Available via NASA’s Open Data Portal—confirmed accessible as of May 2025. :contentReference[oaicite:5]{index=5}
- **MetroPT-3 (UCI)**: Active and functional as of early 2025. :contentReference[oaicite:6]{index=6}
- **NASA PHM Repository**: Various datasets actively downloadable via PHM Society mirror. :contentReference[oaicite:7]{index=7}
- **MetroPT via Nature/Zenodo**: Published in 2022, downloadable from journal site and Zenodo mirror. :contentReference[oaicite:8]{index=8}

---

> *All links and dataset sources were verified to work on August 24, 2025.*

---

##  Quick Summary

- **Reliability Engineering**:  
  • C-MAPSS (RUL/simulated engines)  
  • NASA PHM Repo (bearings, batteries, composites, etc.)

- **Maintenance / Anomaly Detection**:  
  • MetroPT-3 (compressor logs)  
  • MetroPT (rich APU + GPS)

Let me know if you'd like help with **download scripts**, **data loaders in Python**, or **example analyses** for any of these datasets!
::contentReference[oaicite:9]{index=9}
