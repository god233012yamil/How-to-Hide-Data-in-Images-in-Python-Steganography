from PIL import Image

def bin_to_text(binary):
    """Convert binary to text."""
    message = ''.join(chr(int(binary[i:8+i],2)) for i in range(0,len(binary),8))
    return message

def extract_text(image_path):
    """Extract hidden text from an image."""
    image = Image.open(image_path)
    if image.mode in ('RGBA'):
        image = image.convert('RGBA')
        datas = image.getdata()

        binary = ''

        for item in datas:
            digit = bin(item[0])[-1]  # Extract the least significant bit of each pixel
            binary += digit
            if (binary[-16:] == '1111111111111110'):  # Check for the delimiter
                break

        binary = binary[:-16]  # Remove the delimiter

        return bin_to_text(binary)

print(extract_text('image.png'))

