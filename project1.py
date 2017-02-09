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
    
img1 = Image.open('1.png')
img2 = Image.open('2.png')
img3 = Image.open('3.png')
img4 = Image.open('4.png')
img5 = Image.open('5.png')
img6 = Image.open('6.png')
img7 = Image.open('7.png')
img8 = Image.open('8.png')
img9 = Image.open('9.png')
imglist = [img1, img2, img3, img4, img5, img6, img7, img8, img9]
redPixelList = []
greenPixelList = []
bluePixelList= []
#list_of_pixels = []
pictureWidth, pictureHeight = img1.size 
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