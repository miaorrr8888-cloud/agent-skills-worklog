---
name: shortvideo-pipeline
description: 生成短视频脚本、分镜、字幕及发布准备材料，支持离线 mock 演示；不渲染或自动发布视频。
license: MIT
---

# 短视频生产材料

在该包目录运行 `python -m shortvideo_pipeline.cli --help` 查看命令，`python -m shortvideo_pipeline.cli demo` 生成离线 mock 示例，`python -m unittest discover -s tests -v` 运行测试。

先明确选题、观众、平台、目标时长与事实素材。single 与 batch 接受简报并产出脚本、分镜、字幕和准备材料。对真实模型的调用需先配置所选 provider；凭据只从本地环境或 .env 读取，禁止提交真实 .env。

mock 结果仅用于结构演示，不能当成真实模型创意。成片渲染、版权审查、真实创意质量、平台验收与自动发布不包含在本包内。对外使用前检查事实、字幕时序与素材许可。
