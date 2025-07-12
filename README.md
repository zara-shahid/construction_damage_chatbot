# 🏗️ Construction Damage Chatbot

A Gradio-powered AI web app that helps identify and suggest repairs for construction damage based on uploaded images. It uses a lightweight image classifier and an open-source LLM (via Groq API) to provide accurate, structured repair guidance.

🔗 Live Demo: https://huggingface.co/spaces/zarashahid/Construction_Damage_Chatbot

---

## 📌 Features

- **Upload image** of a cracked wall, pipe, or other construction-related damage
- **Detect damage type** using MobileNetV2 image classification (offline)
- **Get smart repair advice** from an LLM (like LLaMA 3 via Groq API):
  - Type of damage
  - Likely cause
  - Suggested repair technique
  - Tools required
  - Estimated repair time
  - Safety precautions
- **Gradio UI** — beginner-friendly, no coding needed

---

## 🧠 Technologies Used

- Python 3.8+
- PyTorch & TorchVision
- Gradio
- Groq API (LLM inference)
- Hugging Face Spaces (for deployment)

---

## 🚀 Deployment on Hugging Face Spaces

1. Create a new Hugging Face Space (Gradio SDK).
2. Upload:
   - app.py
   - requirements.txt
   - README.md
3. In Settings → Secrets, add:
   - Name: GROQ_API_KEY
   - Value: your actual Groq API key

The app will auto-deploy on commit.

---

## 🛠️ Local Development

Clone the repo and run it locally:

```bash
git clone https://github.com/zara-shahid/construction_damage_chatbot.git
cd construction-damage-chatbot
pip install -r requirements.txt
export GROQ_API_KEY=your_groq_api_key
python app.py

📁 File Structure
bash
Copy
Edit
.
├── app.py               # Gradio + LLM + Image classifier logic
├── requirements.txt     # Python dependencies
├── README.md            # You are here!
🔐 API Key Security
This project uses the GROQ_API_KEY secret securely via:

Hugging Face Secrets (for deployed version)

Environment variable (for local use)

Never expose your API key in code.

📄 License
MIT License — feel free to fork, modify, and use with attribution.

