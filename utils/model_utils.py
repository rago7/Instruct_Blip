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
    prompt = "Explain me what is in this image?"
    inputs = processor(images=image, text=prompt, return_tensors="pt")
    # outputs = model.generate(**inputs)
    outputs = model.generate(
    **inputs,
    do_sample=False,
    num_beams=5,
    max_length=256,
    min_length=1,
    top_p=0.9,
    repetition_penalty=1.5,
    length_penalty=1.0,
    temperature=1,
    )
    description = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip()
    print(prompt, description)
    return description
    return "temporary return -- hehe --"
