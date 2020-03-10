import os
from PIL import Image

src = "./billmurray/"
size = 128, 128

def main(src): 
    i = 0
      
    for filename in os.listdir(src):
    # Image.open('old.jpeg')
    # box = (150, 200, 600, 600)
    # image = Image.open(src + filename).convert('RGB')
    # # cropped_image = image.crop(box)
    # new_image = image.resize((400, 400))
    # image.thumbnail((128,128), Image.ANTIALIAS)
    # print(image.size)
    # image.save("./bm_resize/"+filename)
        desired_size = 368
        
        im = Image.open(src + filename).convert('RGB')
        old_size = im.size  # old_size[0] is in (width, height) format
        
        ratio = float(desired_size)/max(old_size)
        new_size = tuple([int(x*ratio) for x in old_size])
        # use thumbnail() or resize() method to resize the input image
        
        # thumbnail is a in-place operation
        
        # im.thumbnail(new_size, Image.ANTIALIAS)
        
        im = im.resize(new_size, Image.ANTIALIAS)
        # create a new image and paste the resized on it
        
        new_im = Image.new("RGB", (desired_size, desired_size))
        new_im.paste(im, ((desired_size-new_size[0])//2, (desired_size-new_size[1])//2))
        new_im.save("./data_src/"+src+filename)
    
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main(src) 