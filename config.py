import os
from typing import List


class ConfigManager:

    @classmethod
    def get_reddit_username(cls) -> str:
        return os.environ.get("REDDIT_USERNAME", "")

    @classmethod
    def get_reddit_password(cls):
        return os.environ.get("REDDIT_PASSWORD", "")

    @classmethod
    def get_reddit_client_secret(cls):
        return os.environ.get("REDDIT_CLIENT_SECRET", "")

    @classmethod
    def get_reddit_client_id(cls):
        return os.environ.get("REDDIT_CLIENT_ID", "")

    @classmethod
    def get_reddit_subreddit(cls):
        return os.environ.get("REDDIT_SUBREDDIT", "")

    @classmethod
    def get_reddit_allowed_users(cls) -> List[str]:
        return os.environ.get("REDDIT_ALLOWED_USERS", "").split(",")

    @classmethod
    def get_download_path(cls) -> str:
        return os.environ.get("DOWNLOAD_PATH", "")

    @classmethod
    def get_kafka_topic(cls) -> str:
        return os.environ.get("KAFKA_TOPIC", "reddit-jobs")

    @classmethod
    def get_kafka_bootstrap_servers(cls) -> List[str]:
        return os.environ.get("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092").split(",")
