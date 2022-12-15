from easygui import diropenbox
from os import getcwd, listdir
from os.path import join, splitext, isfile
from json import load

def get_html_head(profile_key):
    """generates head section of the HTML content
    takes profile_key and uses it as the title for the HTML page"""
    content = "<!DOCTYPE html>\n<html lang=\"en\">\n\t<head>\n\t\t<meta charset=\"utf-8\">\n\t\t<title>"
    content += profile_key + " - Twitter"
    content += "</title>\n\t\t<link rel=\"icon\" type=\"image/png\" sizes=\"16x16\" href=\""
    content += """data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAACXBIWXMAAAABAAAAAQE4IvRAAAAAJHpUWHRDcmVhdG9yAAB4nHNMyU9KVXBMK0ktUnBNS0tNLikGAEF6Bs7nzXNmAAACn0lEQVRYhe3WT2gcZRjH8c+0xgY1s21FxZgRRDEQoeJB8aJ4sVAP9qAiXjpbT+qhvdiLCqJUai3ooXgQhO5oDy0UL3rV0qoIgjaHlIIHESaplIKpk1pq0nY8zG67TvbPbNyczA+G2X3ed57fl/ff87Km/7uCYSaLkuxuPIVNmMPJNA7ny/0mDs2b3blpOUCUZJvxVxqHfw9oXMOH2IGb2pou4SO8ky/lS8FIMIVX8W4ah+dhXSnXbiRRI1s/oPkJvFwyh1vwJr4LRoIZnMZCy7wTwFa8KHAkSrLRigz78XCfPo/hIXyGo1GSvTTeWAg6AdzVfD+Pk1GS3d8ra3PKdlYEXcKz+AbTZ+tjeSeA822/H8V0lGRvREl2a5ekj+PmigAjuIyn0zg80wqWAb4u/b8N7+HXKMn2Rkk2eW/jYnv7xormLb2QxuHP7YHyLrhHsVBqPZL8gu9xBnfi9QEAHknjcLo9UF61NcQ4ig1dkjzYfFaiP8qBMsCXisVyFvet0KSbFuV+LwfLa+BbTK6COcyk9XCpH8BBXF0FczjeKfgvgDQOf8JbqwTwRV8AWAyC9xWHy7khmp++luc/VAI4t2OMYgd8itkhARyYq9fyTg3lXdDSBkURGYZOyfPD3RqXjQDkuY/x1RDMr+CVtF7rurA7AszWw6t4TlHpLv8HgD1pHP7Yq0PfG1GUZLfjGRxwo1pW0cFreb5rrt7rVO8yAi1NNBbW4UnF1qxqnuMD8t39zGmOwHjjz2B9EIwr5mwjHsATintBzztBSfN4LY3DI1U/uD4FUZJtwT5sM/hldRGH8HYahwOdH8uMoiSbUlTE7Yqq1w3mCk7hGD5P43BZoVkRwHV9kotGF+7AFCYw1my5gN8wk8bhxS5fr2lNlfUPUFKyhPy+ImEAAAAASUVORK5CYII="""
    content += "\" />\n\t\t<style>"
    content += """
            @import url('https://fonts.googleapis.com/css?family=Lato:400,900');

			::-webkit-scrollbar {
				overflow: overlay;
				width: 16px;
				position: relative;
				right: 10px;
			}

			::-webkit-scrollbar-track {
				display: none;
			}

			::-webkit-scrollbar-button {
				height: 0;
			}

			::-webkit-scrollbar-thumb {
				background: rgba(23,23,23,0);
				border: 4px solid transparent;
				border-radius: 24px;
				min-height: 60px;
				box-shadow: 0px 0px 0px 4px rgba(23,23,23,0.5) inset;
			}

			#sidebar::-webkit-scrollbar-thumb {
				background: rgba(232,232,232,0);
				box-shadow: 0px 0px 0px 4px rgba(232,232,232,0.5) inset;
			}

			html {
				font-family: 'Lato', sans-serif;
			}

			body {
				padding: 0;
				margin: 0;
			}

			#slack-archive-viewer {
				padding: 0;
				margin: 0;
				height: 100vh;
				overflow: hidden;
			}

			.index-container {
				width: calc(100vw - 385px);
				height: 100vh;
				text-align: left;
				display: inline-block;
				margin-right: -2px;
				padding-right: 2px;
			}

			.index-contents {
				display: flex;
				align-items: center;
				justify-content: center;
			}
			
			#sidebar {
				/*display: inline-block;
				width: 380px;
				color: white;
				text-align: left;
				background-color: #1da1f2;
				z-index: 10;
				overflow-y: overlay;
				overflow-x: hidden;
				white-space: nowrap;
				height: 100vh;
				user-select: none;
				margin-bottom: -3px;
				padding-bottom: 3px;*/
                clear: left;
				margin: auto;
				width: 598px;
				transition: 0.15s;
				border-left: 1px solid #eff3f4;
				border-right: 1px solid #eff3f4;
				border-top: 1px solid #eff3f4;
			}

			#sidebar a {
				font-size: 100%;
			}

			#sidebar h3 {
				margin: 20px 20px 10px 20px;
				color: white;
				font-weight: 900;
			}

			.content {
				width: 100vw;
				height: 100vh;
				text-align: left;
				float: none;
				overflow-y: overlay;
				overflow-x: hidden;
			}

			.message-container {
				clear: left;
				margin: auto;
				width: 578px;
				padding: 10px 10px 10px 10px;
				transition: 0.15s;
				border-left: 1px solid #eff3f4;
				border-right: 1px solid #eff3f4;
				border-top: 1px solid #eff3f4;
			}

			.message-container .preview {
				max-width: 360px;
				max-height: 360px;
				border-radius: 5px;
				position: relative;
				margin: 2px 0 5px 0;
				top: 8px;
			}

			.message-container .yt-embed {
				position: relative;
				margin: 2px 0 5px 0;
				top: 8px;
				padding: 0;
			}

			.message-container .yt-embed iframe {
				width: 400px;
				height: 225px;
				border-radius: 5px;
				margin: 0;
				padding: 0;
			}

			.message-container .message-list {
				margin: 0;
				padding-left: 25px;
			}

			.message-container .message-list-outer {
				margin: 2px 0 2px 0;
				padding-left: 25px;
			}

			.message-container .message-list .bullet::marker {
				font-size: 1.2em;
			}

			.message-container .message-file {
				border-radius: 5px;
				border-style: solid;
				border-color: rgba(212, 212, 212, 1);
				border-width: 1px;
				background-color: white;
				overflow: hidden;
				width: 426px;
				height: 62px;
				position: relative;
				margin: 2px 0 5px 0;
				top: 8px;
				display:inline-block;
				white-space: nowrap;
			}

			.message-container .message-file-info {
				color: #1D1C1D;
				font-size: 95%;
				float: left;
				margin: 12.5px 0 0 12.5px;
				width: 291px;
				text-overflow: ellipsis;
				white-space: nowrap;
				overflow: hidden;
			}

			.message-container .message-file-name {
				color: #1D1C1D;
				font-weight: 600;
				margin: 0;
				width: 280px;
				height: 22px;
				text-overflow: ellipsis;
				white-space: nowrap;
				overflow: hidden;
			}

			.message-container .message-file-type {
				color: #616061;
				margin: 0;
				width: 280px;
				height: 22px;
				text-overflow: ellipsis;
				white-space: nowrap;
				overflow: hidden;
			}

			.message-container .message-reactions {
				margin: 5px 0 5px 0;
			}

			.message-container .message-reactions .reaction {
				border-radius: 10px;
				border-style: solid;
				border-color: #1D9BD1;
				font-size: 90%;
				border-width: 1px;
				background-color: #E2EFF4;
				overflow: hidden;
				color: #2664A3;
				float: left;
				padding: 4px 6px 4px 4px;
				margin-right: 4px;
				top: 8px;
				white-space: nowrap;
			}

			.message-container .message-reactions .reaction b {
				font-size: 80%;
				position: relative;
				top: -0.05em;
			}

			.message-container .user-icon {
				background-color: rgb(248, 244, 240);
				width: 48px;
				height: 48px;
				border-radius: 24px;
				display: inline-block;
				vertical-align: top;
				margin-right: 0.65em;
				float: left;
			}

			.message-container .username {
				display: inline-block;
				font-weight: 600;
				line-height: 1;
				color: #1D1C1D;
			}

			.message-container .user-email {
				font-weight: normal;
				font-style: italic;
			}

			.message-container .message {
				display: inline-block;
				vertical-align: top;
				line-height: 1;
				width: calc(100% - 3em);
				bottom: 0;
			}

			.message-container .msg p {
				margin-top: 0.2em;
				margin-bottom: -0.2em;
				color: #1D1C1D;
				white-space: pre-wrap;
				font-size: 95%;
			}

			.message-container .msg p.meta-msg {
				color: #616061;
			}

			.message-container .msg pre {
				background-color: #EFEFEF;
				white-space: pre-wrap;
				overflow: auto;
				padding: 0 1em;
				margin: 0.5em 0 0 0;
				border-style: solid;
				border-color: #D4D4D4;
				border-width: 1px;
				border-radius: 3px;
			}

			h1 {
				width: 100%;
				color: #1D1C1D;
				position: relative;
				font-size: 250%;
				text-align: center;
				margin: 50px 0 0 0;
			}

			h2 {
				margin: 0 0 10px 0;
				width: 100%;
				color: #616061;
				position: relative;
				font-size: 123%;
				text-align: center;
				font-weight: 500;
			}

			.message-container .message .msg {
				line-height: 1.5;
                margin-top: 6px;
			}

			.message-container .message-attachment {
				padding-left: 5px;
				border-left: 2px gray solid;
			}

			.message-container .message-attachment .service-name {
				color: #999999;
			}

			.message-container .icon {
				max-width: 10px;
			}

			blockquote {
				border-left: 4px solid #DDDDDD;
				margin: 10px 0px 0px 0px;
				padding: 0 10px 5px 10px;
				color: #1D1C1D;
			}

			.message-container .message-thread {
				border-left: 10px solid #1da1f2;
				border-radius: 5px;
				margin: 0;
			}

			.message-container .message-thread:hover {
				border-left: 10px solid #e8f5fe;
			}

			.message-container .message-thread-container {
				border-radius: 5px;
				border-style: solid;
				border-color: rgba(0,0,0,0.03);
				border-width: 1px;
				background-color: white;
				position: relative;
				margin: 2px 0 10px 0;
				top: 8px;
				transition: 0.15s;
			}

			.message-thread .message-container {
				clear: left;
				min-height: 36px;
				max-width: calc(100% - 20px);
				padding: 10px 10px 10px 10px;
			}

			.message-thread .message-container:first-child {
				margin-top: 0;
			}

			.message-thread .message-container:last-child {
				margin-bottom: 0;
			}

			.message-container .message-thread-container:hover {
				border-color: rgba(212, 212, 212, 1);
			}

			.channel_join .msg, .channel_topic .msg, .bot_add .msg, .app_conversation_join .msg {
				font-style: italic;
			}

			.attachment-footer {
				font-size: small;
			}

			.list {
				margin: 0;
				padding: 0;
				list-style-type: none;
                display: inline-block;
                width: 100%;
			}

            li {
                list-style-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAACXBIWXMAAAABAAAAAQE4IvRAAAAAJHpUWHRDcmVhdG9yAAB4nHNMyU9KVXBMK0ktUnBNS0tNLikGAEF6Bs7nzXNmAAAA5UlEQVQ4jdXTrU4DQRSG4adkCaiRJPwsFQSPwSEx4MoN7K2xgmCaVHIH3AGSIFYUvQraBDAzhYTd7oQqPvVlzpk352dmJFNl3d5hryc8L3JBuMBxT+y5KOt2isOehNemCpPoTzGKfhdTXKbEAmc4wbID1KxMFRZQ1u0O7iPkAecJBPOmCgfr+voBmeEqQiZ4ga2hy+sgTRXeUzwLNATJAuVA+J7RJpAxPofe0XUXpKxb2MZHU4UlA601VZjhpqOSIyxwmw4GX3aEDSp7/f8PtJpRXHWufuUm0D7eNq3oUfx4f9BTMl+fLkm4STi2fQAAAABJRU5ErkJggg==');
            }

            .li-location {
                list-style-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABIAAAASCAYAAABWzo5XAAAACXBIWXMAAAABAAAAAQE4IvRAAAAAJHpUWHRDcmVhdG9yAAB4nHNMyU9KVXBMK0ktUnBNS0tNLikGAEF6Bs7nzXNmAAAA4UlEQVQ4jZ2TIQ7CQBBFHyRgwIIAaklPwBnwJFgUqgIH18E14RZYVGVZC4ieAByYWTJd2O3CS0bszJ+3TZu28DMDlsBUzgY4AKfATo0+kANPT+WSCdIBjgGJraNkvewiJLa2PkkbuDlhA6yljDO7yc4HqRN8ABM1T6SnM6l+CsvAERvgqs4X6WncnfeN+rY7MFLzsfR0JvkmAiicYAmspEpnVvgkABnNX8tWFhL1gCpCUkk2yCZCtGmSAHSBc0BylkwU84BoHiuxfPtx818lAEPqL76S3l8slGjxr8SylwryAmvagHZe48R1AAAAAElFTkSuQmCC');
            }

            .message-url-container {
                margin: 0;
                padding: 8px 0 0 26px;
            }

            .message-location-container {
                margin: 0;
                padding: 8px 0 0 26px;
            }

            #li-url {
                position: relative;
                top: -4px;
                transition: 0.15s;
                color: #1da1f2;
				text-decoration: none;
            }

			#li-url:visited {
                color: #1da1f2;
				text-decoration: none;
			}

			#li-url:hover {
				color: #1da1f2;
				text-decoration: underline;
			}

			.channel {
				transition: 0.15s;
                display: inline-flex;
                text-align: center;
                height: 48px;
			}

            .name {
				font-weight: 600;
                position: relative;
                top: -0.2em;
			}

            .handle {
				color: #657786;
                position: relative;
                top: -0.2em;
			}

            .user-info {
				height: 48px;
			}

            .message-header {
				height: 48px;
			}

            .time {
				display: inline-block;
				color: #6F6E6F;
				word-spacing: 5px;
				font-size: 75%;
				font-weight: 500;
				position: relative;
				top: -0.5em;
				transition: 0.15s;
			}

			.channel a:link {
				width: 100%;
				color: #657786;
				transition: 0.15s;
                font-weight: 600;
                margin: 14px 0 0 0;
                padding: 0 15px 0 15px;
			}

            .channel a:hover {
                color: #1da1f2;
				text-decoration: none;
			}

			.channel.active {
				transition: 0.15s;
			}

			.channel.active a {
				color: #1da1f2;
                border-bottom: 2px solid #1da1f2;
			}

			.channel.active:hover {
				background-color: #e8f5fe;
			}

			.channel:hover {
				text-decoration: none;
				background: #e8f5fe;
                color: #1da1f2;
			}

			.context-menu {
				border-radius: 5px;
				border-style: solid;
				border-color: #DCDCDC;
				border-width: 1px;
				background-color: #F8F8F8;
				position: absolute;
				box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
				color: #1D1C1D;
				transition: 0.15s;
			}

			.context-menu ul {
				list-style: none;
				margin: 0;
				padding: 5px 0 5px 0;
			}

			.context-menu ul li {
				font-size: 100%;
				text-decoration: none;
				color: #1D1C1D;
				background-color: #F8F8F8;
				margin: 0;
				padding: 5px 25px 5px 25px;
				transition: 0.15s;
			}

			.context-menu ul li a {
				width: 100%;
				font-size: 100%;
				text-decoration: none;
				color: #1D1C1D;
				background-color: #F8F8F8;
				margin: 0;
				padding: 5px 25px 5px 25px;
				transition: 0.15s;
			}

			.context-menu ul li:hover {
				color: white;
				background-color: #1264A3;
			}

			.highlight {
				background-color: #FAE9B4;
				border-radius: 5px;
			}

			a {
				transition: 0.15s;
			}

			a:link {
				text-decoration: none;
			}

			a:visited {
				color: #657786;
				text-decoration: none;
			}

			a:hover {
				color: #1da1f2;
				text-decoration: underline;
			}

            a:active {
				color: #1da1f2;
				text-decoration: none;
			}

			.close {
				display: none;
			}"""
    content += "\n\t\t</style>\n\t</head>\n"
    return content

def get_html_body(navbar_content, profiles_content):
    """generates body section of the HTML content"""
    content = "\t<body>\n"
    content += "\t\t<div id=\"slack-archive-viewer\">\n"
    content += "\t\t\t<div class=\""
    content += "content"
    content += "\">\n"
    content += "\t\t\t\t<div id=\"sidebar\">\n\t\t\t\t\t<div class=\"list\" id=\"channel-list\">\n"
    content += navbar_content
    content += "\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n"
    content += profiles_content
    content += "\n\t\t\t</div>\n\t\t</div>\n"
    content += "\t</body>\n</html>"
    return content

def get_html_navbar(current_key, profile_keys):
    """generates HTML navbar"""
    content = ""
    for k in profile_keys:
        content += "\t\t\t\t\t<div class=\"channel"
        content += " active" if k[0] == current_key else ""
        content += "\">\n\t\t\t\t\t\t<a href=\""
        content += k[0]
        content += ".html\">"
        content += k[0] + " (" + k[1] + ")"
        content += "</a>\n\t\t\t\t\t</div>\n"
    return content

def get_html_urls(urls):
    """generates HTML for a list of URLs"""
    content = "\t\t\t\t\t<ul class=\"message-url-container\">\n"
    for url in urls:
        content += "\t\t\t\t\t\t<li><a id=\"li-url\" href=\""
        content += url[1]
        content += "\">"
        content += url[0]
        content += "</a></li>\n"
    content += "\t\t\t\t\t</ul>\n"
    return content

def get_html_profile(handle, name, timestamp, description, location, urls):
    """generates HTML for an individual user profile"""
    content = "\t\t\t\t<div class=\"message-container\">\n\t\t\t\t\t<div class=\"message-header\">\n\t\t\t\t\t\t<img src=\"profile_picture/"
    content += handle
    content += ".jpg\" class=\"user-icon\" />\n\t\t\t\t\t\t<div class=\"user-info\">\n"
    content += "\t\t\t\t\t\t\t<div class=\"name\">" + name + "</div>\n"
    content += "\t\t\t\t\t\t\t<div class=\"handle\">@" + handle + "</div>\n"
    content += "\t\t\t\t\t\t<div class=\"time\">" + timestamp + "</div>\n"
    content += "\t\t\t\t\t\t</div>\n\t\t\t\t\t</div>\n\t\t\t\t\t<div class=\"message\">\n"
    content += "\t\t\t\t\t<div class=\"msg\">\n\t\t\t\t\t\t<p>"
    content += description
    content += "</p>\n\t\t\t\t\t</div>\n"
    if location:
        content += "\t\t\t\t\t<ul class=\"message-location-container\">\n\t\t\t\t\t\t<li class=\"li-location\">"
        content += location
        content += "</li>\n\t\t\t\t\t</ul>\n"
    content += get_html_urls(urls)
    content += "\t\t\t\t</div>\n\t\t\t</div>\n"
    return content

def get_html_content(profiles):
    """generates HTML for all user profiles"""
    content = ""
    for p in profiles:
        handle = p[0].get("username", "")
        name = p[0].get("name", "")
        timestamp = p[0].get("created_at", "")
        description = p[0].get("description", "")
        location = p[0].get("location", "")
        urls = list(map(lambda e: (e.get("display_url", ""), e.get("expanded_url", "")), p[0].get("entities", {}).get("url", {}).get("urls", []))) + list(map(lambda e: (e.get("display_url", ""), e.get("expanded_url", "")), p[0].get("entities", {}).get("description", {}).get("urls", [])))
        content += get_html_profile(handle, name, timestamp, description, location, urls)
    return content

def write_htmls(profile_data, root_dir):
    """writes HTML files in root_dir for all entries in profile_data"""
    for profile_key in profile_data.keys():
        output_file = open(join(root_dir, profile_key+".html"), "w", encoding="utf-8")
        header = get_html_head(profile_key)
        navbar = get_html_navbar(profile_key, list(map(lambda x: (x,str(len(profile_data.get(x)))), profile_data.keys())))
        profiles = get_html_content(profile_data.get(profile_key))
        body = get_html_body(navbar, profiles)
        output_file.write(header)
        output_file.write(body)
        output_file.close()

def import_json(filepath):
    """read JSON file (assuming UTF-8 encoding)"""
    json_file = open(filepath, "r", encoding="utf-8")
    data = load(json_file)
    json_file.close()
    return data

def generate_mutuals(profile_data):
    """returns list of profiles that are both in the "following" and in the "followers" list"""
    return [handle for handle in profile_data.get("following", []) if handle[0].get("username", "") in list(map(lambda x: x[0].get("username", ""), profile_data.get("followers", [])))]

def main():
    root_dir = diropenbox(msg="Select input directory", title="Select input directory", default=getcwd())

    # check if the essential files are present in the selected directory
    for f in ["following.json", "followers.json", "profile_picture"]:
        if f in listdir(root_dir):
            print(f + " found")
        else:
            print("ERROR: " + f + " not found")
            exit()
    
    # get all JSON files in the selected directory
    files = list(map(lambda x: splitext(x)[0], filter(lambda x: splitext(x)[1] == ".json" and isfile(join(root_dir, x)), listdir(root_dir))))

    # read these JSON files and put them into a single dictionary
    profile_data = {}
    for f in files:
        filename_segments = f.split("-")
        # this ensures that "followers.json" will be called "followers", but "list-000000000-listname.json" will be called "listname"
        if len(filename_segments) > 1 and filename_segments[0] == "list":
            filename = "-".join(filename_segments[2:])
        else:
            filename = f
        profile_data.update({filename: import_json(join(root_dir, f+".json"))})
    profile_data.update({"mutuals": generate_mutuals(profile_data)})

    # write HTML files generated from JSON data
    write_htmls(profile_data, root_dir)

main()

