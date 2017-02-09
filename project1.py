from PIL import Image

#https://github.com/titanbronco/205project1

def medianOdd(myList):
# Store list length in the variable listLength
    listLength = len(myList)
# Sort the list
    sortedValues = sorted(myList)
# Location of middle value. Subtract one because of zero index
    middleIndex = ((listLength + 1)/2) - 1
# Return the object located at that index
    return sortedValues[middleIndex]
    
#open the images and store them in an image list using a loop
imglist =[]
for i in range (1,10):    
    imglist.append(Image.open(str(i)+".png"))
    
redPixelList = []#create empty lists to be populated with RGB values from the image pixels
greenPixelList = []
bluePixelList= []
pictureWidth, pictureHeight = imglist[0].size #set the size
cleanimg = Image.new('RGB',(pictureWidth,pictureHeight))  #create the new empty image


for x in range(0,pictureWidth):
    for y in range(0,pictureHeight):
        for myImage in imglist:
        
            myRed, myGreen, myBlue = myImage.getpixel((x,y)) #get the pixels from the image
        
            redPixelList.append(myRed)#put the pixels in lists to be sorted through
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
            
            
        #populate new image with median RGB values
        cleanimg.putpixel((x,y), (medianOdd(redPixelList), medianOdd(greenPixelList), medianOdd(bluePixelList)))
        redPixelList = []
        greenPixelList = []
        bluePixelList = [] 
        
     
cleanimg.show()
cleanimg.save("Result.png")