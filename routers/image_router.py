# routers/image_router.py
from fastapi import APIRouter, File, UploadFile
from utils.model_utils import process_image_with_prompt
import torch
from PIL import Image
import io

router = APIRouter()

@router.post("/analyze-image/{action}")
async def analyze_image(action: str, file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    description = process_image_with_prompt(image, action)
    return {"description": description}


# Load model and processor
# processor = InstructBlipProcessor.from_pretrained("Salesforce/instructblip-vicuna-7b")
# model = InstructBlipForConditionalGeneration.from_pretrained(
#     "Salesforce/instructblip-vicuna-7b",
#     load_in_4bit=True,
#     torch_dtype=torch.float16
# )

# @router.post("/analyze-image/")
# async def analyze_image(file: UploadFile = File(...)):
#     # Convert uploaded file to image
#     # image_bytes = await file.read()
#     # image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

#     # # Prepare prompt and process the image
#     # prompt = "What is unusual about this image?"
#     # inputs = processor(images=image, text=prompt, return_tensors="pt")
    
#     # # If using CUDA, uncomment the next line
#     # # inputs = inputs.to(device="cuda", dtype=torch.float16)

#     # outputs = model.generate(
#     #     **inputs,
#     #     num_beams=5,
#     #     max_new_tokens=256,
#     #     min_length=1,
#     #     top_p=0.9,
#     #     repetition_penalty=1.5,
#     #     length_penalty=1.0,
#     #     temperature=1,
#     # )

#     # generated_text = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip()
#     # return {"description": generated_text}
#     return {"description": "generated_text"}
