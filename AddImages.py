"""
Put images in the NewImages folder and 
run this script to automatically create resized versions of the images
and change the permissions of the images to 704
"""


# import required modules
import os
from PIL import Image
# assign directory
directory = 'NewImages'
files = os.listdir(directory)
 
# loop through files
for file in files:
    # check if file is an image
    if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
        # rename file to replace spaces with '-'
        new_file = file.replace(' ', '-')
        ext = new_file.split('.')[-1]
        os.rename(f'{directory}/{file}', f'{directory}/{new_file}')
        
        # grab filename without extension
        filename = new_file.split('.')[0]

        # open image
        img = Image.open(f'{directory}/{new_file}')

        # Put original image in the images folder
        # and change permissions of the images to 704
        img.save(f'images/{new_file}')
        os.chmod(f'images/{new_file}', 0o704)

        # create copies of the image with different widths and maintain aspect ratio,
        # rename copy to f'{new_file}-p-{new_size}.{ext}'
        # and put them in the images folder
        widths = [500, 800, 1080, 1600, 2000, 2600]
        for width in widths:
            if img.width > width:
                new_img = img.copy()
                wpercent = (width / float(img.size[0]))
                hsize = int((float(img.size[1]) * float(wpercent)))
                new_img = new_img.resize((width, hsize), Image.Resampling.LANCZOS)
                new_img.save(f'images/{filename}-p-{width}.{ext}')
                # change permissions of the images to 704
                os.chmod(f'images/{filename}-p-{width}.{ext}', 0o704)

        # close and delete image
        img.close()
        os.remove(f'{directory}/{new_file}')