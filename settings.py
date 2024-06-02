import logging

BASE_FOLDER = './file'
SECURITY_USER = ('forij', 'cpt', 'yushang')
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s',
                    handlers=[
                        logging.FileHandler('app.log'),  # 将日志保存到文件
                    ])