import json
import os
import urllib.parse

from kafka import KafkaProducer

from config import ConfigManager


def process_video(video_url: str):
    url_parts = urllib.parse.urlparse(video_url)
    path_parts = url_parts[2].rpartition('/')
    file_name = path_parts[2]
    download_path = ConfigManager.get_download_path()
    topic = ConfigManager.get_kafka_topic()
    bootstrap_servers = ConfigManager.get_kafka_bootstrap_servers()
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    message = {
        'job_type': 'reddit-download-video-job',
        'job':
            {
                'VideoURL': video_url,
                'OutputFileName': os.path.join(download_path, file_name)
            }
    }
    json_message = json.dumps(message).encode('utf-8')  # Encode as bytes
    producer.send(topic, json_message)
    producer.close()
