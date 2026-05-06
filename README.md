# youtubeCommentsScraper
Tool to scrape all comments (including replies) from any public YouTube video.


## Setup Instructions

### 1. Install Python
Download and install Python from: [https://www.python.org/](https://www.python.org/)

### 2. Create Project & Virtual Environment

```bash
# Navigate to project folder
cd path/to/youtube-comment-scraper

# Create virtual environment
python -m venv myenv

# Activate virtual environment
myenv\Scripts\activate     # For Windows
# source myenv/bin/activate # For macOS/Linux


#Install Requirements

pip install -U yt-dlp pandas

#Scrape Comments

yt-dlp --write-comments --no-download "https://www.youtube.com/watch?v=VIDEO_ID"

#Note: This creates a .info.json file with all comments.

#To convert from json to csv use the script (convert_to_csv.py) 
