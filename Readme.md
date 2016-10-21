## Synopsis

So, you've come across a Giphy media file, on the web or perhaps in your Slack channel, and you'd like to know where it came from.

Giphy tags its pages with meta keywords (yes, apparently people still use meta keywords), but doesn't inject the same data into its media files.

This silly little tool accepts a media file URL (e.g. http://media.giphy.com/media/10zxDv7Hv5RF9C/giphy.gif) and extracts the meta keywords from the related webpage (e.g. giphy.com/gifs/10zxDv7Hv5RF9C )

## Installation

The frontend is some pretty simple AngularJS.  The backend is set up to run on Google App Engine, but doesn't use any GAE-specific frameworks, so you can easily port the Python to another platform.

## Sample

http://giphytags.appspot.com

## Contributors

https://github.com/peckjon

## License

WTFPL v2: https://en.wikipedia.org/wiki/WTFPL