# Ω-TSCI Numerical Verification Suite

[![Field: Theoretical Physics](https://img.shields.io/badge/Field-Theoretical%20Physics-blue)](https://arxiv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/TSCI-Model/TSCI)

## 1. 简介 (Introduction)
本仓库包含了论文 **《Ω-TSCI: A Unified Geometric Framework for Dark Energy, Dark Matter, and the Cosmic Dark Sector Ratio》** 的完整数值验证代码。通过分析因果集（Causal Set）拓扑标度指数 $\gamma$，我们实现了对宇宙学常数、MOND 临界加速度 $a_0$ 以及暗物质/暗能量比例的统一推导。

This repository provides the numerical suite for the Ω-TSCI framework, demonstrating how a single topological scaling index $\gamma$ derived from causal set fluctuations governs the cosmic dark sector.

---

## 2. 快速开始 (Quick Start for Google Colab)

在 Google Colab 或终端中，执行以下一键命令即可完成：**环境配置 -> 仓库克隆 -> 核心数值审计**。

**One-line Execution:**
```bash
git clone https://github.com/TSCI-Model/TSCI.git && cd TSCI && pip install numpy matplotlib scipy && python3 verification/cosmo_audit.py
