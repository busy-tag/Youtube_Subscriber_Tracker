from PIL import Image, ImageDraw, ImageFont

def draw_subscription_info(channel_name, subscriber_count, background_image_path, output_path):
    # Load background image
    background_img = Image.open(background_image_path)
    
    # Resize background image to match desired output dimensions (240x280)
    background_img = background_img.resize((240, 280))

    # Initialize a blank image with the same size as the background image
    img = Image.new('RGB', background_img.size)

    # Paste the resized background image onto the blank image
    img.paste(background_img, (0, 0))

    # Initialize ImageDraw object
    draw = ImageDraw.Draw(img)

    # Load a custom font
    font_path = "MontserratBlack-3zOvZ.ttf"  # Replace with the path to your font file
    font_size = 22
    font = ImageFont.truetype(font_path, font_size)

    # Define text
    text = f"{channel_name}\n\nSubs: {subscriber_count}"

    # Calculate text position
    text_x = 20
    text_y = 100

    # Draw text on image
    draw.text((text_x, text_y), text, fill=(0, 0, 0), font=font)

    # Save the image to the specified output path
    img.save(output_path)