from sentence_transformers import SentenceTransformer, util
import torch
import json

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load your destination dataset
with open("app/data.json", "r") as f:
    destination_data = json.load(f)

# Preprocess for embedding
dest_texts = [f"{d['description']} in {d['destination']}" for d in destination_data]
dest_embeddings = model.encode(dest_texts, convert_to_tensor=True)

def recommend_trip(sentiment: str, location: str, budget: int):
    query = f"{sentiment} places near {location}"
    query_embedding = model.encode(query, convert_to_tensor=True)

    # Find best match
    scores = util.pytorch_cos_sim(query_embedding, dest_embeddings)
    best_idx = torch.argmax(scores).item()

    # Get result
    match = destination_data[best_idx]

    if match["estimated_cost"] > budget:
        return {
            "destination": match["destination"],
            "reason": f"{match['description']}. Might exceed your budget though.",
            "estimated_cost": match["estimated_cost"]
        }
    else:
        return {
            "destination": match["destination"],
            "reason": match["description"],
            "estimated_cost": match["estimated_cost"]
        }
