import json
import os

from kafka import KafkaProducer

from config import ConfigManager
from util import create_valid_file_name


def process_video(video_url: str, title: str):
    file_name = create_valid_file_name(title)
    download_path = ConfigManager.get_download_path()
    topic = ConfigManager.get_kafka_topic()
    bootstrap_servers = ConfigManager.get_kafka_brokers()
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
