---
name: ml-experiment-log
description: Document, track, and benchmark machine learning experiments in 02_KNOWLEDGE/ML/EXPERIMENTS/. Enforces reproducible scientific records (hypotheses, mathematical formulations, model architecture, data hash, training loss/metric curves, ablation results, and theoretical takeaways).
---

# ML Experiment Log Protocol

Mission: Ensure that all machine learning skill-building, prototype models, and algorithmic experiments maintain full scientific reproducibility and yield concrete conceptual progress.

## Experiment Entry Schema

Save each run to `02_KNOWLEDGE/ML/EXPERIMENTS/EXP_[NNN]_[TOPIC_SLUG].md`:

```markdown
# Experiment [NNN]: [Title / Objective]

- **Date**: YYYY-MM-DD
- **Author**: Sahand (Master's in AI)
- **Domain**: Deep Learning / Time Series / NLP / Reinforcement Learning
- **Repository / Script**: `path/to/script.py`

---

## 1. Problem Statement & Theoretical Hypothesis
- **Question**: What specific behavior or architectural hypothesis is being tested?
- **Hypothesis**: "Replacing standard MultiheadAttention with Linear Attention will reduce memory footprint from O(N^2) to O(N) while maintaining validation perplexity within 2% on sequences > 2048."
- **Mathematical Invariant**: Equations and loss functions involved.

---

## 2. Model & Data Configuration
- **Architecture**: Number of layers, hidden dimension, heads, activation functions
- **Dataset / Synthetic Generator**: Name, token count, train/val/test split ratios
- **Optimizer & Schedule**: AdamW (lr=3e-4, beta=(0.9, 0.98), weight_decay=0.01, cosine annealing)
- **Batch Size & Precision**: 64, bfloat16 / float32

---

## 3. Results & Empirical Metrics
| Metric | Baseline | Experiment | Delta |
|---|---|---|---|
| Train Loss | X.XXX | X.XXX | -X.XX |
| Val Loss | X.XXX | X.XXX | -X.XX |
| Throughput (tok/s) | N | N | +X% |
| Memory Peak (MB) | N | N | -X% |

---

## 4. Key Takeaways & Theoretical Analysis
- **Did the hypothesis hold?**:
- **Surprising Behaviors / Failure Modes**: (e.g. gradient vanishing, loss spikes during warmup)
- **Next Iteration / Open Questions**:
```
