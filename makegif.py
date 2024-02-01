import glob
from PIL import Image
import cv2

#%%
def make_avi(input_pattern: str, output_file: str, fps: float = 30):
    image_paths = sorted(glob.glob(input_pattern))

    frame = cv2.imread(image_paths[0])
    height, width, layers = frame.shape
    
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    for image in image_paths:
        video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()


parent_folder = "C:/Users/Mels/Code/pytimelapse/screenshots"
fps = 95
child_folders = [f for f in os.listdir(parent_folder)] # get only folders, not files
for folder in child_folders:
    subfolder = os.path.join(parent_folder, folder)  # concatenate folders to get full path
    image_path = f"{subfolder}/*.png"  # match images like this
    output_file = f"{folder}.avi"
    make_avi(image_path, output_file, fps)


#%%

folder = 'C:/Users/Mels/Code/pytimelapse/screenshots/2024.01.28'
output_filepath = f'./output.gif'
image_paths = sorted(glob.glob(f"{folder}/*.png"))
images = [Image.open(image_path) for image_path in image_paths]

gif = images[0]
gif.info['duration'] = 8.5 #ms per frame
gif.info['loop'] = 0 #how many times to loop (0=infinite)
gif.save(fp=output_filepath, format='gif', save_all=True, append_images=images[1:])
# %%
