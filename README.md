# Local-AI

A local-first AI assistant project built around Qwen3.5, with support for personal behavior customization, RAG, memory, tools, and eventual Windows/USB portability.

## Goals
- Run Qwen locally with Ollama during development.
- Customize behavior with LoRA/QLoRA instead of modifying base model weights directly.
- Use RAG for private and changing knowledge.
- Keep persistent memory separate from training data.
- Add a controlled tool/action layer.
- Add application-level policy for privacy, accuracy, safety, legality, and sensitive operations.
- Package a portable Windows version later using GGUF + llama.cpp.

## Target hardware
Development target: Windows PC with an NVIDIA RTX 4060 8 GB GPU.

## Repository layout
```text
qwen35/       Training, datasets, configs, and QLoRA scripts
app/          Assistant application and policy configuration
portable/     Portable/USB deployment notes
```

## Important
Model weights, private memories, credentials, API keys, and personal documents must not be committed to GitHub.
