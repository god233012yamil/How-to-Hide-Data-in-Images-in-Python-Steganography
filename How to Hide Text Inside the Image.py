from PIL import Image

def text_to_bin(text):
    """Convert text to binary."""
    binary = ''.join(format(ord(i), '08b') for i in text)
    return binary

def hide_text(image_path, text):
    """Hide text inside an image."""
    image = Image.open(image_path)
    binary = text_to_bin(text) + '1111111111111110'  # Append a delimiter to denote the end of text

    if image.mode in ('RGBA'):
        image = image.convert('RGBA')
        datas = image.getdata()

        new_data = []
        digit = 0
        for item in datas:
            if (digit < len(binary)):
                newpix = list(item)
                newpix[0] = newpix[0] & ~1 | int(binary[digit])  # Change the least significant bit of each pixel
                new_data.append(tuple(newpix))
                digit += 1
            else:
                new_data.append(item)

        image.putdata(new_data)
        image.save(image_path, "PNG")
        
        return "Completed!"

print(hide_text('image.png', 'Hello, World!'))
