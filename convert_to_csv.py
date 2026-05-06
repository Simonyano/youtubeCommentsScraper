import json
import pandas as pd

with open('[filename].info.json', encoding='utf-8') as f:
    data = json.load(f)

comments = []

def extract_comments(comment_list, parent_id=None):
    for c in comment_list:
        comments.append({
            'comment_id': c.get('id'),
            'parent_id': parent_id,
            'author': c.get('author'),
            'text': c.get('text'),
            'like_count': c.get('like_count'),
            'publish_time': c.get('timestamp'),
            'is_reply': parent_id is not None
        })
        if c.get('replies'):
            extract_comments(c['replies'], c.get('id'))

extract_comments(data.get('comments', []))

df = pd.DataFrame(comments)
df.to_csv('youtube_comments.csv', index=False, encoding='utf-8')
print(f"Saved {len(df)} comments to CSV")
