from PIL import Image, ImageFilter
#Read image
im = Image.open( 'image.jpg' )
#Display image

imData = list(im.getdata())
fContrast = .2

invertedData = [] 
for pixels in range(0,len(imData)):
    tempArr =[1,2,3]
    if imData[pixels][0] < 127:
        tempArr[0]= imData[pixels][0] - int(imData[pixels][0] * fContrast)
    else:
        tempArr[0]= imData[pixels][0] + int((255-imData[pixels][0]) * fContrast)
        
    if imData[pixels][1] < 127:
        tempArr[1]= imData[pixels][1] - int(imData[pixels][1] * fContrast)
    else:
        tempArr[1]= imData[pixels][1] + int((255-imData[pixels][1]) * fContrast)

    if imData[pixels][2] < 127:
        tempArr[2]= imData[pixels][2] - int(imData[pixels][2] * fContrast)
    else:
        tempArr[2]= imData[pixels][2] + int((255-imData[pixels][2]) * fContrast)

    invertedData.append(tuple(tempArr))
    
    
im.putdata(invertedData,1.0,0)
im.save( 'image_new.jpg', 'JPEG' )
