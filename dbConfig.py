import toml
import os

def read_config():
    config = {}
    
    if os.path.exists('config.toml'):
        config = toml.load('config.toml')['database']
    else:
        config = {
            'host': os.getenv('DB_HOST', 'kubela.id'),
            'port': int(os.getenv('DB_PORT', '3306')),
            'user': os.getenv('DB_USER', 'davis2024irwan'),
            'password': os.getenv('DB_PASSWORD', 'wh451n9m@ch1n3'),
            'database': os.getenv('DB_DATABASE', 'aw')
        }
    
    return config
