# from transformers import InstructBlipProcessor, InstructBlipForConditionalGeneration
# import torch
# from PIL import Image
# import requests
# print("prompt1")
# model = InstructBlipForConditionalGeneration.from_pretrained("Salesforce/instructblip-vicuna-7b")
# processor = InstructBlipProcessor.from_pretrained("Salesforce/instructblip-vicuna-7b")

# device = "cpu" if torch.cuda.is_available() else "cpu"
# model.to(device)
# # url = "https://images.app.goo.gl/6wFawxpZJ1EYm34FA"
# image = Image.open(r"C:\Users\Project\Desktop\Docs\my_project\images\img2.png")
# prompt = "What do you understand by this image?"
# inputs = processor(images=image, text=prompt, return_tensors="pt").to(device)
# print("prompt2")
# outputs = model.generate(
#     **inputs,
#     do_sample=False,
#     num_beams=5,
#     max_length=256,
#     min_length=1,
#     top_p=0.9,
#     repetition_penalty=1.5,
#     length_penalty=1.0,
#     temperature=1,
# )
# generated_text = processor.batch_decode(outputs, skip_special_tokens=True)[0].strip()
# print(generated_text)