class Logger:
    def __init__(self, name):
        self.name = name

    def log_info(self, message):
        print(f"\033[92m[INFO] {self.name}: {message}\033[0m")  # 绿色

    def log_error(self, message):
        print(f"\033[91m[ERROR] {self.name}: {message}\033[0m")  # 红色

    def log_warning(self, message):
        print(f"\033[93m[WARNING] {self.name}: {message}\033[0m")  # 黄色

    def log_debug(self, message):
        print(f"\033[94m[DEBUG] {self.name}: {message}\033[0m")  # 蓝色