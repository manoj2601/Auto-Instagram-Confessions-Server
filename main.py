import pandas as pd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from instagrapi.types import Usertag, Location
from instagrapi import Client
import textwrap
from config import username, password, sheet_url


#read confessions from google sheets
url_1 = sheet_url.replace('/edit', '/export?format=csv&')
p = pd.read_csv(url_1, usecols= ['Write your confession here:'])
confessions = [i[0] for i in p.values]
#check for new confessions
posted = int(open('total.txt', 'r').read())
if(posted == len(confessions)):
	print("No new confessions!")
	exit(1)

#instagram login
bot = Client()
bot.login(username, password)

# font, size and colour
fontSize = 30
myFont = ImageFont.truetype('OpenSans-SemiBold.ttf', fontSize)
bodyColor = (255, 0, 0)
headingColor = (0, 0, 255)

instaHandleCorner = (250, 1030)

#posting new confessions
for i in range(posted+1, len(confessions)+1):
	
	#wrapping
	text = confessions[i-1]
	paragraphs = text.splitlines()
	Lines = [textwrap.wrap(j, 50) for j in paragraphs]
	lines = []
	for l in Lines:
		if(len(l) == 0):
			lines.append('')
		else:	lines.extend(l)
	while(lines[len(lines)-1] == ''):
		lines = lines[:-1]
	lines.insert(0, 'Confession #'+str(i))

	#template open
	img = Image.open('template.jpg')
	I1 = ImageDraw.Draw(img)
	I1.text(instaHandleCorner, username, font=myFont, fill=(0, 0, 0))
	w,h = img.size


	#single photo post
	if(len(lines) <= 20):
		currHeight = 100+20*(20-len(lines))
		for line in lines:
			if(line == ''):
				currHeight += 30
				continue
			width,height = myFont.getsize(line)
			if(line[0:10] == 'Confession'):
				I1.text((200, currHeight+height), line, font=myFont, fill=headingColor)
			else:	I1.text((200, currHeight+height), line, font=myFont, fill=bodyColor)
			currHeight += height
		filename="posts/"+str(i)+".jpg" 
		img.save(filename)
		bot.photo_upload(path=filename, 
			caption="Confession: #"+str(i)
			# ,usertags=[Usertag(user=bot.user_info_by_username(username), x=1, y=1)]
			)


	#multiple_pages album post
	elif(len(lines) > 20):
		swipePhoto = Image.open('swipe.png').convert("RGBA")

		totalPages = 1+(len(lines)-1)/20
		subCount = 1
		photos = []
		while(len(lines) > 20):
			currHeight = 100
			for j in range(0, 20):
				line = lines[j]
				if(line == ''):
					currHeight += 30
					continue
				width,height = myFont.getsize(line)
				if(line[0:10] == 'Confession'):
					I1.text((200, currHeight+height), line, font=myFont, fill=headingColor)
				else:	I1.text((200, currHeight+height), line, font=myFont, fill=bodyColor)
				currHeight += height
			filename="posts/"+str(i)+"-"+str(subCount)+".jpg" 
			photos.append(filename)
			img.paste(swipePhoto, (900, 900), swipePhoto)
			img.save(filename)
			img = Image.open('template.jpg')
			I1 = ImageDraw.Draw(img)
			I1.text(instaHandleCorner, username, font=myFont, fill=(0, 0, 0))
			subCount+=1
			lines = lines[20:]

		#last page
		currHeight = 100+20*(20-len(lines))
		for line in lines:
			if(line == ''):
				currHeight += 30
				continue
			width,height = myFont.getsize(line)
			I1.text((200, currHeight+height), line, font=myFont, fill=bodyColor)
			currHeight += height
		filename="posts/"+str(i)+"-"+str(subCount)+".jpg" 
		photos.append(filename)
		img.save(filename)
		
		#upload album post
		bot.album_upload(paths=photos, 
			caption="Confession: #"+str(i)
			# ,usertags=[Usertag(user=bot.user_info_by_username(username), x=1, y=1)]
			)

open('total.txt', 'w').write(str(len(confessions)))