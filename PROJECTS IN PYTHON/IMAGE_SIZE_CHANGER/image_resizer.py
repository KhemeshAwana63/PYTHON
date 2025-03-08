from PIL import Image
import os
def compress_image(input_path , output_path , max_size_kb = 1000):
    img = Image.open(input_path)

    # resize to (400 by 400 pixel)-> github standard
    img = img.resize((400, 400), Image.Resampling.LANCZOS)

    #run a loop to reduce quality untill it is less than 1 mb
    quality = 90
    while True:
        img.save(output_path,"JPEG", quality = quality)
        if os.path.getsize(output_path) <= max_size_kb*1024 or quality <= 10:
            break
        quality -= 5  #reducing the quality untill the condition is met

    print("the process of resizing the image is complete")


compress_image(r"C:\Users\HP\Pictures\Picsart_24-12-22_08-30-24-016.jpg",
               r"C:\Users\HP\Pictures\compressed_image.jpg")
