from PIL import Image, ImageFilter
#Read image
im = Image.open( 'image.jpg' )
#Display image

imData = list(im.getdata())

invertedData = [] 
for pixels in range(0,len(imData)):
    tempArr =[1,2,3]
    for iter in range(pixels - 2, pixels +2):   
        tempArr[0]+=imData[iter][0]
        tempArr[1]+=imData[iter][2]
        tempArr[2]+=imData[iter][2]
    invertedData.append(tuple(tempArr))
    
    
im.putdata(invertedData,1.0,0)
im.save( 'image_new.jpg', 'JPEG' )
