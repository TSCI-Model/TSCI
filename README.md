# Ω-TSCI Numerical Verification Suite

[![Field: Theoretical Physics](https://img.shields.io/badge/Field-Theoretical%20Physics-blue)](https://arxiv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TSCI-Model/TSCI)

## 1. 简介 (Introduction)
This repository contains the complete numerical validation suite for the Ω-TSCI framework, including code and data accompanying the following papers:

Ω-TSCI: A Unified Geometric Framework for Dark Energy, Dark Matter, and the Cosmic Dark Sector Ratio
GNSS clock anomalies as a test of non‑factorizable geometry: a discrete causal prediction
Objective Quantum Decoherence from Non‑factorizable Geometry: a First‑Principles Extension of the Ω‑TSCI Framework
The suite demonstrates how a single topological scaling index γ simultaneously governs the cosmological constant, the MOND critical acceleration a₀, the dark‑matter‑to‑dark‑energy ratio, the GNSS noon‑midnight clock anomaly, and the anisotropic decoherence rate, providing a unified, first‑principles description of the dark sector and the quantum‑classical transition.


本仓库包含 Ω-TSCI 框架的完整数值验证代码集，涵盖以下论文：

《Ω-TSCI：暗能量、暗物质与宇宙暗区比率的统一几何框架》
《GNSS 钟差异常作为非因子化几何的检验：离散因果预言》
《基于非因子化几何的客观量子退相干：Ω-TSCI 框架的第一性原理扩展》
本代码集展示了单一拓扑标度指数 γ 如何同时决定宇宙学常数、MOND 临界加速度 a₀、暗物质与暗能量密度比、GNSS 正午‑午夜钟差异常以及各向异性退相干率，从而以统一的第一性原理描述暗区及量子‑经典过渡。
---

## 2. 快速开始 (Quick Start for Google Colab)

在 Google Colab 或终端中，执行以下一键命令即可完成：**环境配置 -> 仓库克隆 -> 核心数值审计**。

**One-line Execution:**
```bash
# [Step 1] 克隆仓库 (Clone Repository)
!git clone https://github.com/TSCI-Model/TSCI.git

# [Step 2] 进入目录并执行审计 (Change dir and run Audit)
%cd TSCI
!python3 verification/cosmo_audit.py

# [Step 3] 生成验证图表 (Generate Verification Plots)
!python3 observations/galactic_dynamics.py
