from PIL import Image, ImageFilter
#Read image
im = Image.open( 'image.jpg' )
#Display image

imData = list(im.getdata())

invertedData = [] 
for pixels in range(0,len(imData)):
    tempArr =[1,2,3]
    tempArr[0]=255-imData[pixels][0]
    tempArr[1]=255-imData[pixels][2]
    tempArr[2]=255-imData[pixels][2]
    invertedData.append(tuple(tempArr))
    
    
im.putdata(invertedData,1.0,0)
im.save( 'image_new.jpg', 'JPEG' )
