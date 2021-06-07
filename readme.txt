Wiki-searcher
index.py is the entry point of the Flask application.


Setup 'hosts' file for local testing:
Modify C:\Windows\System32\drivers\etc\hosts file.
Include additional urls for further search testing.
Include the following lines as a minimum:
127.0.0.1		wiki-search.com
127.0.0.1		dogs.wiki-search.com
127.0.0.1		ordinary.wiki-search.com
127.0.0.1   sleepy.wiki-search.com


Install required Python packages:
This will install Flask, its dependents and Requests.
Run the following command:
python -m pip install -r requirements.txt


Running:
Run the following command:
python index.py


Development Notes:
Wikipedia's API disabled searching by title. Instead, I used their index.php.
https://en.wikipedia.org/w/index.php?title=
I noticed that the url for pages that redirected returned as the un-redirected url.
To bypass this, I added the flag redirect=no to the query, then looked on the resulting page for the correct link.
I created functions to detect the type of page: single_page, category_page and redirect_page.
However, by removing the footer and using regex, correct links could be found without needing special regex for each type of page.
The ANCHOR_REGEX_PATTERN was refined multiple times to exclude links contained in the description after the correct link.
(See https://en.wikipedia.org/wiki/Sleepy, Nikola "Sleepy" Andrews (born 1998), American Twitch streamer and former professional Overwatch player.
 This included undesired links for Twitch and Overwatch.)
