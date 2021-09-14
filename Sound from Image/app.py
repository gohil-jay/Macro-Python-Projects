from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string

def image_to_sound(path_to_image):
        
    loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        
        print(cleaned_text)
        
        sound = gTTS(cleaned_text, lang="en")
        sound.save("test_sound.mp3")

image_to_sound("test_image.jpeg")
