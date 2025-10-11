# QQBotUpdater

QQBotUpdater 是一个用于检查和更新 QQBot 的更新器脚本。

## 功能

- 检查更新器自身的版本并自动更新。
- 检查 QQBot 的版本并获取最新更新。
- 支持从远程仓库下载最新的更新器和程序版本。

## 文件结构

- `updater.py`：更新器主脚本。
- `latest.yaml`：记录最新版本信息的文件。
- `2.yaml`：示例更新日志文件。
- `README.md`：项目说明文件。

## 使用方法

1. 确保已安装以下依赖：
   - `requests`
   - `pyyaml`

   可以通过以下命令安装依赖：
   ```bash
   pip install requests pyyaml