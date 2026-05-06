# youtubeCommentsScraper
It is a short tool that helps you scrape the comments section on YouTube videos, using yt-dlp  


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


Install Requirements
Bashpip install -U yt-dlp pandas

Scrape Comments
Bashyt-dlp --write-comments --no-download "https://www.youtube.com/watch?v=VIDEO_ID"

Note: This creates a .info.json file with all comments.

