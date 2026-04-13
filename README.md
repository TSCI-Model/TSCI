# Ω-TSCI Numerical Verification Suite

## 介绍 (Introduction)
本仓库包含了论文《Ω-TSCI: A Unified Geometric Framework...》的所有数值验证代码。通过单一的标度指数 $\gamma$，我们实现了对宇宙学常数、MOND 临界加速度以及暗物质比例的统一推导。

This repository contains the numerical verification suite for the Ω-TSCI paper. It demonstrates how a single scaling index $\gamma$ governs the cosmic dark sector.

## 项目结构 (Project Structure)
- **`simulation/`**: 理论核心模块。
  - `params.py`: **全局参数中心**。修改此处的 $\gamma$ 将同步更新所有实验结果。
  - `core_scaling.py`: 复现 Fig 3。通过泊松洒点验证标度律。
  - `fig1_diamond.py`: 绘制因果钻石几何示意图。
- **`verification/`**: 数值审计模块。
  - `cosmo_audit.py`: 生成 96% 吻合度的数值报告（Table 1）。
- **`observations/`**: 天文观测模块。
  - `galactic_dynamics.py`: 复现 Fig 4。对比预测曲线与星系转动观测数据。
- **`predictions/`**: 实验预言模块。
  - `gw_spectrum.py`: 复现 Fig 5。预言引力波张量谱指数 $n_T \approx -0.5$。

## 如何使用 (Usage)
1. 确保安装了 `numpy`, `matplotlib`, `scipy`。
2. 首先配置 `simulation/params.py` 中的核心常数。
3. 运行 `verification/cosmo_audit.py` 以获取完整的审计报告。
4. 运行 `observations/` 或 `predictions/` 下的脚本生成论文图表。

## 核心预言 (Core Predictions)
基于 $\gamma = 0.4977$，本模型给出以下精确预言：
- **MOND $a_0$**: $1.16 \times 10^{-10} \text{ m/s}^2$ (Match: 96.6%)
- **$\Omega_{DM}/\Omega_\Lambda$**: $0.366$ (Match: 96.4%)
- **$n_T$**: $-0.49$ (Theoretical Target: $-0.50$)
