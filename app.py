from flask import Flask, jsonify
import configparser
import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import argparse

app = Flask(__name__)

# 存储最新的配置数据
config_data = []

class ConfigFileHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('deepseek_config.ini'):
            # 当配置文件被修改时重新加载
            global config_data
            config_data = load_config()
            print("配置文件已更新")

def load_config():
    config = configparser.ConfigParser()
    config.read('deepseek_config.ini', encoding='utf-8')
    categories = []
    
    # 处理导航链接
    if '导航链接' in config:
        nav_links = []
        for name, url in config['导航链接'].items():
            nav_links.append({
                'name': name,
                'url': url
            })
        categories.append({
            'name': '导航链接',
            'links': nav_links
        })
    
    # 处理其他类别
    for section in config.sections():
        if section == '导航链接':
            continue
            
        # 处理普通配置项
        items = []
        for name, template in config[section].items():
            items.append({
                'name': name,
                'template': template
            })
            
        categories.append({
            'name': section,
            'items': items
        })
    
    return categories

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/categories')
def get_categories():
    # 返回最新的配置数据
    global config_data
    return jsonify(config_data)

def start_file_watcher():
    # 初始化配置数据
    global config_data
    config_data = load_config()
    
    # 设置文件监听器
    event_handler = ConfigFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    print("开始监听配置文件变化")
    
    return observer

if __name__ == '__main__':
    # 创建参数解析器
    parser = argparse.ArgumentParser(description='启动DeepSeek提示词聚合工具')
    parser.add_argument('--port', type=int, default=8080, help='指定服务端口号')
    args = parser.parse_args()

    # 启动文件监听器
    observer = start_file_watcher()
    
    try:
        app.run(debug=True, host='0.0.0.0', port=args.port)
    finally:
        # 确保在程序退出时停止监听器
        observer.stop()
        observer.join() 