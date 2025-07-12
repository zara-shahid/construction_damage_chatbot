##🏗️ Construction Damage Chatbot
A Gradio-powered AI web app that helps identify and repair construction-related damage from images. Just upload a photo of a damaged wall, pipe, or other structure, and the chatbot will analyze it using a pre-trained image model and suggest detailed repair solutions using a powerful LLM via Groq API.

🚀 Live Demo: (Add your Hugging Face Space link here)

##🔧 Features

Upload any image of construction damage (e.g., cracked wall, water leak, broken pipe)

Detects damage using MobileNetV2 image classification (offline)

Sends the detected damage to a powerful open-source LLM (like LLaMA 3 via Groq API)

AI responds with:

Type of damage

Likely cause

Repair technique

Tools required

Estimated repair time

Safety tips

Simple Gradio web UI — works in Colab or on Hugging Face Spaces

##🧠 Technologies Used

Python

PyTorch & TorchVision

Gradio

Groq API (LLM Inference)

Hugging Face Spaces (Deployment)

##📦 Installation (for local use)

Clone this repo and install requirements:

pip install -r requirements.txt

Set your Groq API key as an environment variable:

export GROQ_API_KEY=your_key_here

Then run:

python app.py

##🔐 Hugging Face Deployment

Add your Groq API key as a secret named GROQ_API_KEY in your Space settings (Settings → Secrets).

##🖼️ Example Use Case

Upload an image of a cracked wall, and the bot replies with a full repair guide using civil engineering principles.

##📁 File Structure

.
├── app.py → Main app script
├── requirements.txt → Python dependencies
├── README.md → You’re here!

##📜 License

MIT License — free to use and modify.
