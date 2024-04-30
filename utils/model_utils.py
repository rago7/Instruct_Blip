# utils/model_utils.py
from transformers import InstructBlipProcessor, InstructBlipForConditionalGeneration
from PIL import Image

model = InstructBlipForConditionalGeneration.from_pretrained("Salesforce/instructblip-vicuna-7b")
processor = InstructBlipProcessor.from_pretrained("Salesforce/instructblip-vicuna-7b")


def process_image_with_prompt(image: Image, action: str) -> str:
    if action == "find_text":
        prompt = "Describe the text present in the image."
    elif action == "navigate":
        prompt = "What is the main navigation element in this image?"
    else:
        prompt = "What is unusual about this image?"
    prompt = "what is this image?"
    inputs = processor(images=image, text=prompt, return_tensors="pt")
    outputs = model.generate(**inputs)
    description = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip()
    return description
    return "temporary return -- hehe --"
