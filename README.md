# README.md

# Bing Search Bot

该项目是一个自动化工具，使用Chrome浏览器在Bing搜索引擎上搜索指定内容以获取Microsoft Rewards每日奖励

## 功能

- 启动Chrome浏览器
- 在Bing上执行搜索

## 使用方法

1. （安装Anaconda3）

2. 使用查看chrome浏览器版本，并下载与chrome浏览器兼容的chrome driver（大版本匹配即可）。配置环境变量PATH到chrome driver路径

3. 在项目config文件夹的user_config.json中设置Microsoft账号密码

   ```json
   {
       "username": "username@email.com",
       "password": "password"
   }
   ```

4. 配置Python环境：

   ```
   conda env create -f environment.yml
   ```

5. 启动虚拟环境：

   ```bash
   conda activate ms_rewards
   ```

   

6. 运行主程序（需要在bing-search-bot路径下执行此命令）：

   ```
   python src/main.py
   ```
