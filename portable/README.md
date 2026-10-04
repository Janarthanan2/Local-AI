# Portable Windows Deployment

The long-term portable target is a self-contained Windows folder on a USB 3.x SSD or fast flash drive.

## Planned layout
```text
QWEN_AI_USB/
├── MyQwen.exe
├── Start.bat
├── Runtime/
│   └── llama.cpp/
├── Models/
│   └── Qwen3.5/
├── Adapters/
│   └── personal/
├── Memory/
├── Knowledge/
│   └── documents/
└── Config/
```

Use Ollama for development first. Move to GGUF + llama.cpp when a genuinely portable runtime is required.

Do not put model weights, credentials, or private personal data in the Git repository.
