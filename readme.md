# Using the script to deploy tiles

1. Clone the repo https://github.com/albertkun/ucla_maapp_tiles_deploy/
2. Put the zipfile of the tiles into the `tiles_to_add` folder (if it doesn't exist, create it)
3. Commit the file using these commands:
``` bash
git add .
git commit -am "commit new tiles"
git push
```
4. Tiles will automatically extract on server

Note: when script is done, you should run git pull to see that the zip file you added moved from tiles_to_add to existing_tiles folder