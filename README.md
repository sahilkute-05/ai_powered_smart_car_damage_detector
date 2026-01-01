# 🚗 AI Powered Smart Car Damage Detector 
An AI-powered computer vision application that detects and classifies vehicle damage in real-time.

## 🌟 Overview
This project uses a fine-tuned **YOLOv8** model to identify three types of car damage:
- **Dent** 🔨: Structural depressions in the bodywork.
- **Scratch** 🖌️: Surface-level paint damage.
- **Crack** ⚡: Splits in bumpers or body panels.
- **Glass Shatter** 💎: Broken or spider-webbed windows/windshields.
- **Lamp Broken** 💡: Damaged headlights or taillights.
- **Tire Flat** 🛞: Deflated or damaged tires.

The system provides a "Clean vs. Damaged" status update and draws bounding boxes around detected issues with high confidence.

## 🚀 How to Run
1. **Clone the repository**:
   git clone [https://github.com/sahilkute-05/ai_powered_smart_car_damage_detector.git](https://github.com/sahilkute-05/ai_powered_smart_car_damage_detector.git)

2. **Install Dependencies**:
   pip install ultralytics gradio pillow

3. **Download Model Weights**:
   Click here to download car_damage_best.pt
   https://drive.google.com/file/d/1h90FCeIDzLHTJdwylPNyyOLH2Vc27Hgs/view?usp=drive_link

   Place this file in the same folder as app.py.

5. **Launch the App**:
   python app.py

📊 **Model Training Results**

The model was trained for 50 epochs on a custom dataset.
Accuracy (mAP50): ~0.55+ (Example)
Classes: Scratch, Dent, Crack

🛠️ **Built With**

Python 🐍
Ultralytics YOLOv8 (Computer Vision)
Gradio (Web Interface)
Google Colab (Training Environment)
