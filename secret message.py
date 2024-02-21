from PIL import Image

# Function to convert string to list of numbers
def string_to_numbers(s):
    return [ord(c) for c in s]

# Function to convert list of numbers to string
def numbers_to_string(nums):
    return ''.join(chr(num) for num in nums)

# Function to encrypt message into a .bmp file
def encrypt_message(message, image_path):
    # Open the image
    img = Image.open("panda.bmp")
    width, height = img.size

    # Convert message to list of numbers
    nums = string_to_numbers(message)

    # Modify image to store encrypted message
    index = 0
    for y in range(height):
        for x in range(width):
            if index < len(nums):
                pixel = list(img.getpixel((x, y)))
                pixel[0] = nums[index]  # Change red value
                img.putpixel((x, y), tuple(pixel))
                index += 1

    # Save modified image
    img.save("encrypted_image.bmp")

# Function to decrypt message from a .bmp file
def decrypt_message(image_path):
    # Open the encrypted image
    img = Image.open(image_path)
    width, height = img.size

    # Extract encrypted message from image
    encrypted_nums = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            encrypted_nums.append(pixel[0])  # Get red value

    # Convert list of numbers to string
    decrypted_message = numbers_to_string(encrypted_nums)
    return decrypted_message

# Example usage:
message = "This is a secret message."
image_path = "original_image.bmp"

# Encrypt message into image
encrypt_message(message, image_path)

# Decrypt message from encrypted image
decrypted_message = decrypt_message("encrypted_image.bmp")
print("Decrypted Message:", decrypted_message)