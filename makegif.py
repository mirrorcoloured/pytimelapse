import glob
from PIL import Image

folder = 'C:/Users/Mels/Code/pytimelapse/screenshots/2023.11.01'
output_filepath = f'./output.gif'
image_paths = sorted(glob.glob(f"{folder}/*.png"))
images = [Image.open(image_path) for image_path in image_paths]

gif = images[0]
gif.info['duration'] = 10 #ms per frame
gif.info['loop'] = 0 #how many times to loop (0=infinite)
gif.save(fp=output_filepath, format='gif', save_all=True, append_images=images[1:])