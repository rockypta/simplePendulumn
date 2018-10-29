from PIL import Image, ImageFilter
#Read image
im = Image.open( 'image.jpg' )
#Display image

imData = list(im.getdata())
fBrightNess = .0

invertedData = [] 
for pixels in range(0,len(imData)):
    tempArr =[1,2,3]
    tempArr[0]=imData[pixels][0] + int((255-imData[pixels][0])*fBrightNess)
    tempArr[1]=imData[pixels][1] + int((255-imData[pixels][1])*fBrightNess)
    tempArr[2]=imData[pixels][2] + int((255-imData[pixels][2])*fBrightNess)
    invertedData.append(tuple(tempArr))
    
    
im.putdata(invertedData,1.0,0)
im.save( 'image_new.jpg', 'JPEG' )
