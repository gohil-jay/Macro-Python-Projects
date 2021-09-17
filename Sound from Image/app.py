from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string

def image_to_sound(image_path):
    try:
        loaded_image = Image.open(image_path)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        
        print(cleaned_text)
        
        sound = gTTS(cleaned_text, lang="en")
        sound.save("image_to_sound.mp3")
        return True
    
    except Exception as bug:
        print("The bug thrown : ", bug)
        return False

if __name__ == "__main__":
    image_to_sound("text_image.jpg")
    input()
