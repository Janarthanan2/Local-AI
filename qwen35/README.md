# Qwen3.5 Customization

This directory contains the starter workflow for customizing a local Qwen3.5 model.

## Recommended approach
1. Keep the base model unchanged.
2. Use QLoRA/LoRA for behavior, style, and task specialization.
3. Use RAG for changing or private factual knowledge.
4. Keep long-term memory in a separate store.
5. Evaluate the adapter before using it in the assistant.

## Local setup

Create the project environment on the Windows development drive, then install:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r qwen35\requirements-training.txt
python qwen35\scripts\check_gpu.py
python qwen35\scripts\validate_dataset.py
```

## Training

The starter script uses 4-bit NF4 quantization and LoRA. Before a real run, replace the example dataset with a sufficiently large, high-quality dataset and verify that the selected base model is available in your Transformers environment.

```powershell
python qwen35\scripts\train_qlora.py
```

Never place passwords, API keys, private documents, or raw personal memory into the Git repository.
