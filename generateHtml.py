import os,sys
import glob



def IsUnique(ImageName, listOfImages):
	ImageName_ = ImageName.split('.')[0]
	unique = True
	for image in listOfImages:
		OnlyName = image.split('.')[0]
		if(OnlyName == ImageName_):
			if(unique):
				unique = False
			else:
				return False
	return True


def RemoveRepeatedFiles(listOfImages):
	for image in listOfImages:
		#print(image," : ",IsUnique(image,listOfImages))
		if(not IsUnique(image,listOfImages)):
			#print('\t',image,' is not unique')
			listOfImages.remove(image)
	return listOfImages



def GetListOfImages():
	ImageFiles = glob.glob("*.png") + glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.gif")
	#print(ImageFiles)
	return RemoveRepeatedFiles(ImageFiles)


def GetListofDirectories():
        items = os.listdir('.')
        directores = []
        for item in items:
                if os.path.isdir(item):
                        print(item)
                        if(item[0] != '.'):
                                directores.append(item)
        return directores

#listOfImages = GetListOfImages()
listOfImages = sorted(GetListOfImages(), key=str.lower)
listOfDirectories = sorted(GetListofDirectories(), key=str.lower)
#print(listOfImages)
#sys.exit(0)

skeleton = open('res/skeleton.html','r')

outFile = open('index.html','w')
count = 0

for inline in skeleton:
	if('<body>' in inline):
		outFile.write(inline)
		toWrite = '<h1>%s</h1>'%(os.getcwd())
		outFile.write(toWrite)
        if('[parent]' in inline):
                for dir_ in listOfDirectories:
                        toWrite = '<a href="./%s/">[%s]</a>'%(dir_,dir_)
                        outFile.write(toWrite)
	if(not('piccont' in inline)):
		outFile.write(inline)
	else:
		outFile.write(inline)
		for image in listOfImages:
			toWrite = "<div class='pic'><h3><a href='%s'>%s</a></h3><img src='%s' style='border: none; width: 40ex; '><p>Also as [none]</p></div> </div>"%(image,image,image)
			outFile.write(toWrite)
			count += 1

outFile.close()
print('%d image added'%(count))
print('Done!')
