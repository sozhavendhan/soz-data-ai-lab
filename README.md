# soz-data-ai-lab

Hands-on experiments in Data Engineering, AI, Snowflake, Fabric, Databricks, GitHub and Enterprise Architecture.

This repository is organized so you can learn by reading short guides and running small, focused examples.

## Repository structure

- foundations/
  - sql/        — SQL examples and exercises
  - python/     — Python examples, scripts, and notebooks
  - pyspark/    — PySpark jobs and examples

- platforms/
  - snowflake/  — Snowflake-specific examples and SQL
  - fabric/     — Microsoft Fabric recipes and notes
  - databricks/ — Databricks notebooks and jobs

- ai-engineering/
  - machine-learning/ — classical ML examples (scikit-learn)
  - deep-learning/    — deep learning examples (TensorFlow/PyTorch)
  - llm/              — LLM usage patterns and quickstarts
  - rag/              — Retrieval-Augmented Generation examples
  - agents/           — Agent patterns and demos

- architecture/   — Reference architecture, diagrams, and notes

## Quickstart

1. Browse the top-level folders above and open the README.md in the area you want to learn.
2. Each subfolder contains a short README plus a small runnable example (Python scripts or SQL files).
3. To run Python examples: create a virtual environment and install the packages listed in the example files' header (e.g., scikit-learn, pandas).

Example:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt  # if a requirements file is provided for a folder
python foundations/python/example_script.py
```

## Contributing

This repo is for learning and documenting common patterns. See CONTRIBUTING.md for details on how to contribute.

## License

This project is available under the MIT License - see LICENSE for details.
