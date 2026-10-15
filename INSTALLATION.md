# 下载、运行与WorkBuddy使用说明

## 先选择适合自己的方式

这11个包包含技能说明和本地Python工具，不是手机小程序。只想了解用途，先读各自INTRODUCTION.md；想运行，读USER_GUIDE.md。每个技能各自独立下载。

## 下载文件

打开对应GitHub仓库，选择Code → Download ZIP，解压到自己的工作目录。进入包含SKILL.md的那层目录，保留scripts、references、examples等原有子目录。ZIP不包含Git提交历史；需要历史扫描时使用真正的Git仓库。

本地另备有每个技能的独立压缩包，包内容不包含个人运行环境或账号凭据。不要把一个脚本移出整个技能包后直接运行。

## 直接运行

本次示例以Windows和Python 3.12验证。可以从[Python官网](https://www.python.org/downloads/)安装适合自己系统的Python；确认终端能执行 python --version。进入技能根目录，用 python -m venv .venv 创建独立环境，再直接调用 .\.venv\Scripts\python.exe 安装依赖和运行命令。

直接调用环境中的Python不需要激活环境或修改PowerShell执行策略；依据[Python官方venv说明](https://docs.python.org/3/library/venv.html)。macOS/Linux通常使用 .venv/bin/python；本次未验证这些系统。Windows系统配音仅适用于Windows，其他系统可给渲染器提供已有录音。

Python环境和依赖须在使用者自己的电脑创建。不要把本项目工作机里的.venv或绝对路径复制给别人。核心示例是否需要第三方依赖，各指南已分别列出；本地模型或依赖的首次下载需要网络。

## 让WorkBuddy协助

腾讯WorkBuddy Enterprise的[官方技能文档](https://intl.cloud.tencent.com/zh/document/product/1316/84503)说明了本地技能包上传、检测、启用的流程。按你当前版本实际界面选择“技能→添加技能→上传技能”；文档适用的企业版与个人版入口可能不同。

本项目尚未在使用者当前WorkBuddy版本中实际导入、识别和运行这11个包。因此，支持SKILL.md格式与每项程序能成功执行应分别确认，不能标成“11项已在WorkBuddy安装成功”。安全检测有提示时按界面处理，不提供绕过办法。

若未导入技能，但当前WorkBuddy具备读取项目文件和运行终端的能力，可以选择解压后的技能目录，并提交各USER_GUIDE中的自然语言任务。若缺少这些能力，就先采用手动命令路线，或让WorkBuddy只解释指南。

确认运行时需区分：已下载→已导入并启用→已运行示例→输出符合预期。看到技能名不等于程序运行通过，看到结果文件也不等于真实业务验收通过。

## 常见问题

- 找不到Python：先确认系统安装与终端命令。不要误把浏览器内网页当作本地终端。
- 依赖安装了仍找不到：检查安装和运行是否用同一个.venv中的Python。
- 找不到输入文件：确认处于包含SKILL.md的目录，或改用带引号的正确路径。
- 输出目录已存在：换一个新的结果目录；不要删除自己还需要的旧结果。
- 报HOLD、UNKNOWN或需要人工核验：先按指南查看含义，这些可能是正常保护状态。
- 需要付费服务或API：基础示例优先离线。不能为了让演示通过而擅自切换收费调用或填写虚构凭据。
