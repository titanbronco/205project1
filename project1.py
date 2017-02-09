from PIL import Image

def medianOdd(myList):

# Store list length in the variable listLength

    listLength = len(myList)

# Sort the list

    sortedValues = sorted(myList)

# Location of middle value. Subtract one because of zero index

    middleIndex = ((listLength + 1)/2) - 1

# Return the object located at that index

    return sortedValues[middleIndex]
imglist =[]
for i in range (1,10):    
    imglist.append(Image.open(str(i)+".png"))
    
redPixelList = []
greenPixelList = []
bluePixelList= []
#list_of_pixels = []
pictureWidth, pictureHeight = imglist[0].size 
cleanimg = Image.new('RGB',(pictureWidth,pictureHeight))  


for x in range(0,pictureWidth):
    for y in range(0,pictureHeight):
        for myImage in imglist:
        
            myRed, myGreen, myBlue = myImage.getpixel((x,y))
        
            redPixelList.append(myRed)
            greenPixelList.append(myGreen)
            bluePixelList.append(myBlue)
            
            
        #redSort = sorted(redPixelList)
        #greenSort = sorted(greenPixelList)
        #blueSort = sorted(bluePixelList)
        #mediantup = (redSort[4], greenSort[4], blueSort[4])
        #list_of_pixels.append(mediantup)
        cleanimg.putpixel((x,y), (medianOdd(redPixelList), medianOdd(greenPixelList), medianOdd(bluePixelList)))
        redPixelList = []
        greenPixelList = []
        bluePixelList = [] 
        
     
print ("hello")
#cleanimg.putdata(list_of_pixels) 
cleanimg.show()
cleanimg.save("Result.png")