import logging
import sys

import praw

from config import ConfigManager
from processor import process_video


def main():
    bot_name = "vd-bot"
    bot_author = "vaio"
    app_version = "0.0.1"
    user_agent = f"{bot_name} {app_version} by {bot_author}"

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[logging.StreamHandler(sys.stdout)],  # Log to stdout
                        force=True)

    client_id = ConfigManager.get_reddit_client_id()
    client_secret = ConfigManager.get_reddit_client_secret()
    username = ConfigManager.get_reddit_username()
    password = ConfigManager.get_reddit_password()

    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret,
                         user_agent=user_agent, username=username, password=password)

    allowed_users = ConfigManager.get_reddit_allowed_users()
    subreddit = ConfigManager.get_reddit_subreddit()
    sub = reddit.subreddit(subreddit)
    logging.info(f"Starting to poll new submissions from {subreddit}")
    for submission in sub.stream.submissions(skip_existing=True):
        if submission.author.name not in allowed_users:
            logging.debug(f"Discarding submission... Author not allowed. Author: {submission.author.name}")
            continue
        process_submission(submission)


def process_submission(submission):
    title = submission.title
    if hasattr(submission, 'crosspost_parent_list') and submission.crosspost_parent_list[0]['is_video']:
        secure_media = submission.crosspost_parent_list[0]['secure_media']
    elif submission.is_video:
        secure_media = submission.secure_media
    else:
        logging.debug(f"Discarding submission... Not a video")
        return
    logging.info(f"Processing submission...")
    process_video(secure_media['reddit_video']['fallback_url'], title)


if __name__ == "__main__":
    main()
