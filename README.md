# Auto-Instagram-Confessions
Create a confessions account on Instagram and post confessions received from google forms anonymously and automatically.


## Previous Default approach for Instagram confession page
1. Receive anonymous confessions via google form.
2. copy and paste them to a photo editing software and make a instagram postable photo.
3. save that photo and post it to instagram account with a proper counting.

> This is very lengthy approach. Admin has to do a lot of work for posting each confession.

## An improvised Solution:
Here I purpose a program that reads the confessions from google sheet (responses of google forms) and writes them to a specific photo template and posts these photos to instagram with a proper automatic counting. If length of the confession if larger than a single template, it creates multiple templates for that confessions and posts an album post with all photos.

## Implementation:
I used the following python libraries for the implementation:
1. `pandas` python library to read confessions from google sheet.
2. `PIL` python library to modify the template by writing the confession text.
3. `instagrapi` python library to post the confessions on Instagram.

## Deployment:
You can deploy it locally:
1. Create a google form like this:

<img src="./extras/gform.png" alt="gform" width="500"/>

2. clone this repository using `https://github.com/manoj2601/Auto-Instagram-Confessions.git` or download it in zip format and extract it.
3. edit config.py with your login credentials and google sheet link (where the google form responses are being stored).
4. Run `python main.py` whenever you want to post confessions on your instagram handle.
  
  Now if you check your instagram handle, all newly confessions are posted like the following: 

## Final instagram posts:
**Single Post short confessions:**  

<img src="./posts/1.jpg" alt="photo post" width="300"/>
  
**Album post for long confessions:**  

<img src="./posts/2-1.jpg" alt="album-post-1" width="300"/>        <img src="./posts/2-2.jpg" alt="album-post-2" width="300"/>

## Contributing:
All contributions and suggestions are welcome!
* Raise an issue for suggesions.
* To contribute :
	1. Fork it.
	2. Create your feature branch: `git checkout -b my-new-feature`.
	3. Commit your changes: `git commit -am "Add  some feature"`
	4. Submit a pull request.

Give it a star, if you like the concept.