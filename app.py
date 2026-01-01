
import gradio as gr
from ultralytics import YOLO

# Note: Users will need to update this path to their own model location
model = YOLO('car_damage_best.pt') 

def inspect(img):
    results = model(img)[0]
    return results.plot(), f"{len(results.boxes)} Damages Found"

demo = gr.Interface(
    fn=inspect, 
    inputs="image", 
    outputs=["image", "text"],
    title="🚗 Smart Car Damage Inspector"
)

if __name__ == "__main__":
    demo.launch()
