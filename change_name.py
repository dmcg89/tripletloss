import os
from PIL import Image
file = "./billnye/"

def main(src): 
    i = 0
      
    for filename in os.listdir(file): 
        print(filename)
        dst ="img" + str(i) + ".jpg"
        src =file+ filename 
        dst ="./rename/"+ dst
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
        i += 1

# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main(file) 