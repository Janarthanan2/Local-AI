import yaml
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer

with open("qwen35/config.yaml", "r", encoding="utf-8") as f:
    cfg = yaml.safe_load(f)

model_name = cfg["model"]["name"]
train_file = "qwen35/datasets/train.example.jsonl"

if not torch.cuda.is_available():
    raise RuntimeError("CUDA GPU is required for the starter 4-bit training configuration.")

compute_dtype = torch.bfloat16
bnb_config = BitsAndBytesConfig(
    load_in_4bit=cfg["quantization"]["load_in_4bit"],
    bnb_4bit_quant_type=cfg["quantization"]["quant_type"],
    bnb_4bit_compute_dtype=compute_dtype,
    bnb_4bit_use_double_quant=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=True)
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto",
    torch_dtype=compute_dtype,
)

dataset = load_dataset("json", data_files=train_file, split="train")

lora = LoraConfig(
    r=cfg["lora"]["r"],
    lora_alpha=cfg["lora"]["alpha"],
    lora_dropout=cfg["lora"]["dropout"],
    target_modules=cfg["lora"]["target_modules"],
    task_type="CAUSAL_LM",
)

args = SFTConfig(
    output_dir=cfg["model"]["output_dir"],
    num_train_epochs=cfg["training"]["num_train_epochs"],
    per_device_train_batch_size=cfg["training"]["per_device_train_batch_size"],
    gradient_accumulation_steps=cfg["training"]["gradient_accumulation_steps"],
    learning_rate=cfg["training"]["learning_rate"],
    warmup_ratio=cfg["training"]["warmup_ratio"],
    logging_steps=cfg["training"]["logging_steps"],
    save_steps=cfg["training"]["save_steps"],
    gradient_checkpointing=cfg["training"]["gradient_checkpointing"],
    bf16=True,
    max_length=cfg["training"]["max_seq_length"],
    report_to="none",
)

trainer = SFTTrainer(
    model=model,
    args=args,
    train_dataset=dataset,
    processing_class=tokenizer,
    peft_config=lora,
)

trainer.train()
trainer.save_model(cfg["model"]["adapter_dir"])
tokenizer.save_pretrained(cfg["model"]["adapter_dir"])
print("QLoRA adapter saved to", cfg["model"]["adapter_dir"])
