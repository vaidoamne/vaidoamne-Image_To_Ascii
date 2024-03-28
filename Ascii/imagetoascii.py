
import cv2
import os
#image conversion for gray scale to ascii based on brightness level
def printAscii(pixelintensity):
    char = ""
    if pixelintensity in range(0,75):
        char = "@"
    if pixelintensity in range(75,125):
        char = '#'
    if pixelintensity in range(125,175):
        char = "/"
    if pixelintensity in range(175,225):
        char = '"'
    if pixelintensity in range(225,255):
        char = "-"

    return char
def main():
    print("Pick one image to convert:")
    print("whitecat")
    print("flowers")
    print("guy")
    os.remove("result.txt")
    result = open("result.txt", "x")
    script_dir = os.path.dirname(__file__)
    rel_path = input()+".jpg"
    imageName = os.path.join(script_dir, rel_path)
    image = cv2.imread(imageName,cv2.IMREAD_GRAYSCALE)
    imageHeight = image.shape[0]
    imageWidth = image.shape[1]
    for i in range(imageWidth):
       result.write('\n')
       for j in range(imageHeight):
            pixelintensity = image[i,j]
            pixelprint = printAscii(pixelintensity)
            result.write(pixelprint)
    print("Done")
    result.close()
if __name__ == '__main__':
    main()