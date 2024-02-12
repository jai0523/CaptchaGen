#pip install pillow
from PIL import Image, ImageDraw, ImageFont
import random
import string
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageTk

def generate_captcha(text, font_path='arial.ttf', size=(200, 100), color=(0, 0, 0), background=(255, 255, 255)):
    """
    Generate a CAPTCHA image
    :param text: Text for the CAPTCHA
    :param font_path: Path to the font file
    :param size: Size of the image (width, height)
    :param color: Color of the text (R, G, B)
    :param background: Background color of the image (R, G, B)
    :return: CAPTCHA image
    """
    image = Image.new('RGB', size, background)
    font = ImageFont.truetype(font_path, 40)
    draw = ImageDraw.Draw(image)
    draw.text((10, 30), text, fill=color, font=font)
 
    # Optional: Add noise and distort for a more challenging CAPTCHA
    # You can implement your own noise and distortion here
 
    return image

def show_captcha():
    global captcha_image_pil  # Keep track of the PIL Image
    # Get selected font style
    selected_font = font_combobox.get()

    # Check if a font style has been selected
    if selected_font:
        # Generate a random CAPTCHA text
        captcha_text = random_string()
        
        # Generate a random color for the text
        text_color = random_color()

        # Generate CAPTCHA image with selected font style and random color
        font_path = font_paths[selected_font]
        captcha_image_pil = generate_captcha(captcha_text, font_path, color=text_color)
        global img
        img = ImageTk.PhotoImage(captcha_image_pil)
        label.config(image=img)
        label.image = img
        captcha_label.config(text=f"Captcha Generated: {captcha_text}")

    else:
        # Display an error message if no font style is selected
        captcha_label.config(text="Please select a font style")

def save_captcha():
    """
    Save the captcha image
    """
    global captcha_image_pil
    if captcha_image_pil:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            captcha_image_pil.save(save_path)

def random_string(length=6):
    """
    Generate a random string of uppercase letters and digits
    :param length: Length of the string
    :return: Random string
    """
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def random_color():
    """
    Generate a random color
    :return: Tuple (R, G, B)
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Font styles and their paths
font_paths = {
    "Arial": "/Users/jay/Downloads/Fonts_Styles/Arial.ttf",
    "Arial_Italic": "/Users/jay/Downloads/Fonts_Styles/Arial_Italic.ttf",
    "Ariana_Violeta": "/Users/jay/Downloads/Fonts_Styles/ArianaVioleta-dz2K.ttf",
    "Caviar_Dreams_Bold": "/Users/jay/Downloads/Fonts_Styles/Caviar_Dreams_Bold.ttf",
    "CaviarDreams_BoldItalic": "/Users/jay/Downloads/Fonts_Styles/CaviarDreams_BoldItalic.ttf",
    "CaviarDreams": "/Users/jay/Downloads/Fonts_Styles/CaviarDreams.ttf",
    "Freedom-10eM": "/Users/jay/Downloads/Fonts_Styles/Freedom-10eM.ttf",
    "HappySwirly-KVB7l": "/Users/jay/Downloads/Fonts_Styles/HappySwirly-KVB7l.ttf",
    "MariaLite-oR6d": "/Users/jay/Downloads/Fonts_Styles/MariaLite-oR6d.ttf",
    "ostrich-regular": "/Users/jay/Downloads/Fonts_Styles/ostrich-regular.ttf",
    "Oswald-HeavyItalic": "/Users/jay/Downloads/Fonts_Styles/Oswald-HeavyItalic.ttf",
    "Oswald-Stencil": "/Users/jay/Downloads/Fonts_Styles/Oswald-Stencil.ttf",
    "Pacifico": "/Users/jay/Downloads/Fonts_Styles/Pacifico.ttf",
    "Roboto-Regular": "/Users/jay/Downloads/Fonts_Styles/Roboto-Regular.ttf"
  
}

# Create the main window
root = tk.Tk()
root.title("CAPTCHA Generator")

# Create a frame for the CAPTCHA image
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

label = ttk.Label(frame)
label.pack()

# Create a label to display the generated CAPTCHA text
captcha_label = ttk.Label(root, text="")
captcha_label.pack()

# Font selection
font_label = ttk.Label(root, text="Select Font:")
font_label.pack()

font_combobox = ttk.Combobox(root, values=list(font_paths.keys()))
font_combobox.pack()

# Create a button to generate a new CAPTCHA
generate_button = ttk.Button(root, text="Get CAPTCHA", command=show_captcha)
generate_button.pack(pady=10)

# Create a button to save the CAPTCHA
save_button = ttk.Button(root, text="Save CAPTCHA", command=save_captcha)
save_button.pack(pady=10)

# Show the initial CAPTCHA
show_captcha()

# Run the application
root.mainloop()

