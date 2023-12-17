# About foo-Wallpaper-Feh-Gif
This is just a loop script that sets a gif as a wallpaper. Supports transparency.

![desktopGif](https://user-images.githubusercontent.com/36126914/154766367-2c3d9c80-3cdc-4790-b15c-7eba5eee9fd2.gif)
<img src="https://github.com/thomas10-10/foo-Wallpaper-Feh-Gif/raw/master/desktop-animation2.gif"  />
<img src="https://github.com/thomas10-10/foo-Wallpaper-Feh-Gif/raw/master/desktop-animation4.gif"  />

# More gif here
- https://imgur.com/a/F6w9Vr4
- https://imgur.com/a/XxraHzY
- https://imgur.com/a/I8yKrl5

# Requirements:
- feh or xload or [xwallpaper](https://github.com/stoeckmann/xwallpaper)
- md5sum
- imagemagick
- for auto speed calculation, bc package is needed

# To run it
Download back4.sh and a gif.
For ubuntu/xfce set prog=$select4 in back4.sh , You can set stretched style in desktop panel.

```
curl -L https://raw.githubusercontent.com/thomas10-10/foo-Wallpaper-Feh-Gif/master/install.sh | bash
back4.sh 0.010 gif/pixel.gif &
#back4 speed pathToGif &
```
# auto speed calculation
set 'auto' speed option for automatically calculate speed (30 frames per second)

```
back4.sh auto gif/pixel.gif &
```

# select between feh,xwallpaper,xload,ubuntu-xfce
edit back4.sh, set prog=$select2 for xwallpaper, or select4 for ubuntu-xfce

# autostart with i3, in i3 config :

```
exec_always --no-startup-id killall back4.sh 
exec_always --no-startup-id $HOME/back4.sh 0.03 Downloads/beautycity.gif
```

# To stop it
```
killall back4.sh
```

# Alternatively

You can add the speed as a suffix to your desired gif.

```
ls gif/pixel.gif-0.010
back4.sh gif/pixel.gif-0.010 &
```


# To clean cache
 ```
rm -rf /tmp/back4
```

# If you have big gif , you must change config in ImageMagick policy example:
```
sudo sed -i s'@<policy domain="resource" name="memory" value=".*"/>@<policy domain="resource" name="memory" value="2GiB"/>@'g /etc/ImageMagick-6/policy.xml
```

# If you want to use python version
# Requierments:
- python 3.X
- feh or xload or [xwallpaper](https://github.com/stoeckmann/xwallpaper)

# To Run it:
First you need to add executable flag to back4.py
```
sudo chmod +x back4.py
``` 
After that you can run it. For now you have to call it localy:
```
./back4.py auto gif/train.gif &
```

# If you like it support the originator

<a href="https://ko-fi.com/thomas1010">
<img src="https://uploads-ssl.webflow.com/5c14e387dab576fe667689cf/61e11d430afb112ea33c3aa5_Button-1-p-500.png" alt="drawing" width="200"/>
 </a>

