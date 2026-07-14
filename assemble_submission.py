import json
import numpy as np

# 1. Load the pre-compiled guidelines array file from disk
# Protocol index map: 0=Malaria, 1=Typhoid, 2=Hypertension, 3=Co-presentation, 4=TB/Respiratory
guidelines = np.load("clinical_guidelines.npy")

malaria_typhoid_protocol = guidelines[0] + "\n" + guidelines[1] + "\n" + guidelines[3]
tb_respiratory_protocol = guidelines[4]

# 2. Build the structural layout for your official metadata configuration
metadata = {
  "team_id": "YOUR_ACTUAL_TEAM_ID",
  "domain": "healthcare_medical",
  "language_scope": ["en", "ha"],
  "african_alpha_claim": True,
  "budget_laptop_claim": True,
  "submitter": {
    "name": "Muhammad Hamza",
    "email": "hamza.00dev1@gmail.com",
    "github_handle": "Hamza1610"
  },
  "cross_disciplinary_pairing": {
    "discipline": "healthcare",
    "load_bearing": True,
    "description": "Provides zero-database offline clinical decision support for Nigerian CHEWs using localized FMOH symptom-mapping arrays."
  },
  "test_prompts": [
    {
      "prompt_id": "tp_001",
      "prompt": f"<|im_start|>user\nContext: [{malaria_typhoid_protocol}] Patient presents with axillary temperature of 39.1C, watery stooling, and acute lower back pain for 4 days. No rigid neck or yellow sclera found. Task: Determine primary triage category, differential indicator vs malaria, and immediate worker action.<|im_end|>\n<|im_start|>assistant\n"
    },
    {
      "prompt_id": "tp_002",
      "prompt": f"<|im_start|>user\nContext: [{tb_respiratory_protocol}] Adult patient presents with heavy cough for over 25 days, persistent night sweats, and standard fatigue. Patient verbalizes: 'Ina tari da jini kuma jiki na yana zafi' (I am coughing blood and my body is hot). Task: Identify active public health safety warnings, isolation urgency level, and immediate healthcare facility referral directions.<|im_end|>\n<|im_start|>assistant\n"
    }
  ],
  "model": {
    "name": "Qwen2.5-0.5B-Instruct-Q4_0-GGUF",
    "runtime": "llama.cpp",
    "quantization": "GGUF Q4_0",
    "parameters_estimate": "0.5B",
    "packaging": "binary_bundle"
  },
  "_runtime": {
    "model_path": "model/qwen2.5-0.5b-instruct-q4_0.gguf"
  }
}

# 3. Write out the final compliant file directly to your submission directory
with open("metadata.json", "w") as f:
    json.dump(metadata, f, indent=2)

print("Success! Integrated metadata.json generated natively with embedded RAG contexts.")
