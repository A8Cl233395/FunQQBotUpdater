print("需要访问 raw.githubusercontent.com 以检查更新，请确保网络环境正常")
confirm = input("是否继续？(y/N) ")
if confirm.lower() != 'y':
    print("已取消")
    exit(0)

import requests, yaml
try:
    latest_version_yaml = requests.get("https://raw.githubusercontent.com/A8Cl233395/FunQQBotUpdater/refs/heads/main/latest.yaml", timeout=10).text
except requests.Timeout:
    print("请求超时，请检查网络连接")
    exit(1)
updater_version = 2
latest_version_json = yaml.safe_load(latest_version_yaml)
print("当前更新器版本:", updater_version, "最新更新器版本:", latest_version_json["latest_updater_version"])
if latest_version_json["latest_updater_version"] > updater_version:
    print("检测到更新器有新版本，正在下载最新版本...")
    latest_updater_url = "https://raw.githubusercontent.com/A8Cl233395/FunQQBotUpdater/refs/heads/main/updater.py"
    try:
        latest_updater_code = requests.get(latest_updater_url).text
    except requests.Timeout:
        print("请求超时，请检查网络连接")
        exit(1)
    with open("updater.py", "w", encoding="utf-8") as f:
        f.write(latest_updater_code)
    print("更新完成，请重新运行本脚本")
    from subprocess import Popen
    Popen("python updater.py", shell=True)
else:
    print("更新器已是最新版本")

with open("settings.yaml", "r", encoding="utf-8") as f:
    local_settings = yaml.safe_load(f)
version = yaml.safe_load(local_settings)["VERSION"]

print("当前程序版本:", version, "最新程序版本:", latest_version_json["latest_version"])

if latest_version_json["latest_version"] > version:
    print("检测到程序有新版本，正在尝试获取全部更新...")
else:
    print("程序已是最新版本")
    exit(0)