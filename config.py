import json
import os


class Config:
    def __init__(self, config_path='config.json'):
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"配置文件 {self.config_path} 不存在")
        
        with open(self.config_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_user(self):
        return self.config.get('user', {})

    def get_products(self):
        return self.config.get('products', [])

    def get_settings(self):
        return self.config.get('settings', {})

    def get_phone(self):
        return self.config.get('user', {}).get('phone', '')

    def get_password(self):
        return self.config.get('user', {}).get('password', '')
