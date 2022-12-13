from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import requests

processor_printed = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
model_printed = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed')

processor_handwritten = TrOCRProcessor.from_pretrained('microsoft/trocr-base-handwritten')
model_handwritten = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-handwritten')

def get_printed_text(image_file):
    image = Image.open(image_file).convert("RGB")
    pixel_values = processor_printed(images=image, return_tensors="pt").pixel_values

    generated_ids = model_printed.generate(pixel_values)
    generated_text = processor_printed.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

def get_handwritten_text(image_file):
    image = Image.open(image_file).convert("RGB")
    pixel_values = processor_handwritten(images=image, return_tensors="pt").pixel_values

    generated_ids = model_handwritten.generate(pixel_values)
    generated_text = processor_handwritten.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text