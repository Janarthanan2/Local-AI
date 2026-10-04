# Local Assistant Application

The application layer will sit between the local Qwen model and external tools.

## Responsibilities
- Conversation UI
- Model routing
- Persistent memory
- RAG/document retrieval
- Tool execution
- Confirmation for sensitive actions
- Privacy and accuracy policy enforcement

The application should not depend on modifying Qwen's base model weights to enforce these controls.
