# 🐭 MABe Challenge — Social Action Recognition in Mice

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)]()
[![PyTorch](https://img.shields.io/badge/PyTorch-2.x-red.svg)]()
[![Kaggle](https://img.shields.io/badge/Kaggle-Notebooks-important)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()

---

## 📖 Overview
This repo contains my work on the **MABe Challenge (Kaggle 2025)**, where the goal is to detect and classify **30+ mouse social and non-social behaviors** from pose trajectories.  
The challenge advances **machine learning for behavior science**, with applications in **neuroscience, ethology, and AI for biology**.

---

## 🛠 Tools & Stack
- **Python 3.10+**
- **PyTorch 2.x** (training & inference)
- **NumPy / Pandas** (feature engineering)
- **Matplotlib / Seaborn** (visualization)
- **Kaggle Notebooks** (end-to-end pipeline)
- **YAML configs** (reproducibility)

---

## 📂 Repo Layout
```text
mabe-mouse-behavior/
├─ README.md
├─ .gitignore
├─ configs/ # training configs
├─ src/mabe/ # data, models, metrics, utils
│ ├─ data/ # loaders & preprocessing
│ ├─ models/ # TCN, Transformer, etc.
│ ├─ metrics.py
│ └─ postprocess.py
├─ notebooks/ # Kaggle notebooks
│ ├─ 00_bootstrap_repo.ipynb
│ ├─ 01_train.ipynb
│ └─ 02_inference_submit.ipynb
├─ experiments/ # checkpoints & results
└─ kaggle/ # minimal inference script for submission
```


---

## 🚀 Workflow
1. **Training (01_train.ipynb)**  
   - Train temporal models (TCN / LSTM / Transformer) on Kaggle GPU.  
   - Save weights + meta as a Kaggle Dataset.  

2. **Validation (local)**  
   - Evaluate frame-level & segment F-score.  
   - Tune post-processing (smoothing, hysteresis, NMS).  

3. **Submission (02_inference_submit.ipynb)**  
   - Attach the trained weights dataset.  
   - Run inference on test videos.  
   - Generate `submission.csv`.  

---

## 📊 Competition
- **Host**: Kaggle  
- **Challenge**: [MABe Challenge 2025](https://www.kaggle.com/competitions/MABe-mouse-behavior-detection)  
- **Deadline**: Dec 15, 2025  
- **Prizes**: $50k total  

---

## 📜 License
MIT License.  
You are free to use, modify, and distribute this code with attribution.

---
