import os
from gguf import GGUFReader, GGUFWriter

model_path = "model/qwen2.5-1.5b-instruct-q4_k_m.gguf"
fixed_path = "model/qwen2.5-1.5b-instruct-q4_k_m.gguf"

if not os.path.exists(model_path):
    print(f"Error: Could not find model weight asset at {model_path}")
    exit(1)

print("Reading GGUF model properties...")
reader = GGUFReader(model_path)

# Initialize a clean metadata writer configuration
writer = GGUFWriter(fixed_path, str(model_path))

print("Patching metadata header keys...")
# Cleanly override the context boundary entry value natively
writer.add_uint32("qwen2.context_length", 2048)

# Safely copy over all matching properties without key format breaks
for field in reader.fields.values():
    if field.name == "qwen2.context_length":
        continue  # Skip the old 32K tracking key
    
    # Use the official data-type conversion array mappings to prevent crashes
    writer.add_key_value(field.name, field.parts, field.types)

print("Writing patched weights block directly to file storage...")
writer.write_header_to_file()
writer.write_kv_data_to_file()
writer.close()

print("Header update completed successfully!")
