**For Linux
	- Go to the .ssh folder.
	- Enter the command "ssh-keygen -o -t rsa -C "email@id"
	- This is generate 2 keys public and pivrate.
	- cat the contents of the pub key and save them in Github.
	- Once pub key added to github, in the terminal exec "ssh -T git@github.com" , if the key added succesfully you will see your user name.
