# Twitter follow list visualizer
A small Python script that creates HTML visualizations for JSON Twitter follow list exports made using [unflwrs](https://unflwrs.syfaro.com/) by [Syfaro](https://github.com/Syfaro). The script supports custom follow lists.

To use this visualizer, it is important that the *"download profile pictures"* and *"export json instead of csv"* boxes are checked in the [unflwrs](https://unflwrs.syfaro.com/) tool:

![2022-12-11 18_46_24-unflwrs](https://user-images.githubusercontent.com/78315156/206920292-36ccc4e9-90ae-4fcf-abb1-4de2bb7ee300.png)

### twitter-follow-json-visualizer.py
With this script, the user selects the directory in which the [unflwrs](https://unflwrs.syfaro.com/) JSON files are stored. For the program to run, at least the `following.json`, `followers.json` files and the `profile_pictures` directory need to be present in that directory. The resulting HTML pages will look like this:

![2022-12-11 18_50_54-followers - Twitter](https://user-images.githubusercontent.com/78315156/206920294-9d7fdeb9-a6b0-4e46-9788-1f5c0c2b1496.png)

All URLs that are available on the profile, whether in the description or in the URL section, are all shown. Thus, it's guaranteed that all available URLs are shown. The creation date of the twitter account and the location, if available, is also shown.

**Update 16-12-2022:** Pinned tweets and the URLs in them are listed as well. Some people put links to their linktree or other socials in their pinned tweet ONLY. Even worse, some people only share the HANDLES of their other socials, without any links. Now you can still get into contact with these people.

### twitter-follow-json-directory-merger.py
With this script, two [unflwrs](https://unflwrs.syfaro.com/) archives can be merged. The user is asked to select three directories:
 1. the first input directory
 2. the second input directory (in case of collisions files from this directory will be kept)
 3. the output directory

### Requirements
To use this script, you need to:
-   have  **Python**  installed (tested on version 3.10.2)
-   have the  **easygui**  module installed (tested on version 0.98.2; run `pip install easygui==0.98.2` after installing Python)

### Future plans
I initially wrote this quite quickly for personal use, hence the sloppy code. If I have the time for it I may improve the code in the future.
