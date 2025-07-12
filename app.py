import torch
from torchvision import models, transforms
from PIL import Image
import gradio as gr
import requests
import os

# Load MobileNetV2 model
model = models.mobilenet_v2(pretrained=True)
model.eval()

# Load ImageNet labels
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
imagenet_classes = requests.get(LABELS_URL).text.strip().split("\n")

# Define transform
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

# Image classification
def classify_image(img):
    image = Image.fromarray(img).convert("RGB")
    input_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = model(input_tensor)
    predicted_idx = output.argmax(1).item()
    predicted_label = imagenet_classes[predicted_idx]
    return predicted_label

# Query Groq API
def query_groq(prompt):
    api_key = os.getenv("GROQ_API_KEY")  # ✅ Comes from HF Secret

    if not api_key:
        return "🚨 Error: GROQ_API_KEY not found in secrets!"

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a Civil Engineering Assistant specialized in construction damage. "
                    "When given a description like 'cracked wall' or 'rusted pipe', provide:\n"
                    "- Type of damage\n- Cause of damage\n- Suggested repair technique\n"
                    "- Tools required\n- Estimated repair time\n- Safety precautions."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=body)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ API Error: {response.status_code} - {response.text}"

# Main function
def analyze_image(image):
    label = classify_image(image)
    prompt = f"The uploaded image shows: {label}. Please analyze it."
    ai_response = query_groq(prompt)
    return f"🔍 **Detected Damage**: {label}\n\n🧠 **AI Repair Suggestion**:\n{ai_response}"

# Gradio Interface
iface = gr.Interface(
    fn=analyze_image,
    inputs=gr.Image(type="numpy", label="Upload Damage Image"),
    outputs=gr.Markdown(label="AI Assistant Response"),
    title="🏗️ Construction Damage Chatbot",
    description="Upload an image of a cracked wall, water leak, or damaged structure to get AI-powered repair suggestions."
)

# Launch
if __name__ == "__main__":
    iface.launch()
