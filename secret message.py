import tkinter as tk
from tkinter import filedialog
from PIL import Image


# Function to convert string to list of numbers
def string_to_numbers(s):
    return [ord(c) for c in s]


# Function to convert list of numbers to string
def numbers_to_string(nums):
    return ''.join(chr(num) for num in nums)


# Function to encrypt message into a .bmp file
def encrypt_message():
    message = entry_message.get() + "7"  # Add 7 to the end of the message
    image_path = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])

    # Open the image
    img = Image.open(image_path)
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
    label_status.config(text="Message encrypted successfully.")


def get_message_from_image():
    image_path = filedialog.askopenfilename(filetypes=[("BMP files", "*.bmp")])

    # Open the encrypted image
    img = Image.open(image_path)
    width, height = img.size

    # Extract encrypted message from image
    encrypted_nums = []
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            val = pixel[0]
            if val == 7:
                return encrypted_nums
            else:
                encrypted_nums.append(val)
            # encrypted_nums.append(pixel[0])  # Get red value

# Function to decrypt message from a .bmp file
def decrypt_message():
    encrypted_nums = get_message_from_image()

    # Convert list of numbers to string
    decrypted_message = numbers_to_string(encrypted_nums)

    # Remove everything after the last occurrence of '7'
    decrypted_message = decrypted_message[:decrypted_message.rfind('7')]

    label_decrypted.config(text="Decrypted Message: " + decrypted_message)


# Create GUI
root = tk.Tk()
root.title("Message Encryption and Decryption")

# Message Entry
label_message = tk.Label(root, text="Enter Message:")
label_message.pack()
entry_message = tk.Entry(root, width=50)
entry_message.pack()

# Encryption Button
btn_encrypt = tk.Button(root, text="Encrypt Message", command=encrypt_message)
btn_encrypt.pack()

# Decryption Button
btn_decrypt = tk.Button(root, text="Decrypt Message", command=decrypt_message)
btn_decrypt.pack()

# Status Label
label_status = tk.Label(root, text="")
label_status.pack()

# Decrypted Message Label
label_decrypted = tk.Label(root, text="")
label_decrypted.pack()

root.mainloop()
