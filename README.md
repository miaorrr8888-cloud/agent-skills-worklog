# Agent Skills & Work Log

这是我近几个月学习、尝试和制作 AI 工具的阶段性记录。

我把能找到实际文件的成果整理成 11 个技能包，公开源码、使用方法、测试和已知限制。开发和整理使用了 AI 辅助；这里记录能检查的成果，不把想法、模拟结果或未验证的业务效果写成已完成。

维护者：[miaorrr8888-cloud](https://github.com/miaorrr8888-cloud) · [MIT 许可](LICENSE) · [工作记录](WORK_LOG.md) · [来源说明](PROVENANCE.md)

## 技能清单

| 技能 | 能做什么 | 形式 |
|---|---|---|
| [shortvideo_pipeline](shortvideo_pipeline) | 准备口播稿、分镜、字幕等短视频生产材料 | Python 包与技能入口 |
| [reddit-lead-harvest](reddit-lead-harvest) | 整理 Reddit 原帖中的需求证据 | 操作说明 |
| [freelance-marketplace-buyer-pipeline](freelance-marketplace-buyer-pipeline) | 区分外包采购、招聘岗位和冷开发线索 | 操作说明 |
| [github-secret-gated-baseline](github-secret-gated-baseline) | 上传前检查凭证模式、文件范围和 Git 基线 | Python 辅助工具 |
| [evidence-gated-lead-pipeline](evidence-gated-lead-pipeline) | 校验 URL 结构、文案规则和线索状态 | Python 参考实现 |
| [product-video-reverse-search](product-video-reverse-search) | 对已有商品视频候选做启发式排序 | Python 辅助工具 |
| [product-real-asset-library](product-real-asset-library) | 检查媒体信息、追溯 XLSX 内嵌图所在行 | Python 辅助工具 |
| [ai-asset-legibility-audit](ai-asset-legibility-audit) | 确认图片选区，比较文字与数字的几何结构 | Python 辅助工具 |
| [falsifiable-assertion-anchors](falsifiable-assertion-anchors) | 临时回滚修复，检查回归测试是否能发现缺陷 | Python 辅助工具 |
| [local-browser-human-handoff](local-browser-human-handoff) | 登录、验证码等步骤交给本人处理 | 操作说明 |
| [same-object-visual-dictionary](same-object-visual-dictionary) | 将同对象的已有图片变体整理成提示词网页 | Python 辅助工具 |

## 使用

每个目录内有 SKILL.md 和说明。将所需目录复制到宿主支持的技能目录；可执行工具按各目录 README 操作。
Python 需要 3.10 或以上。完整图片测试还需 NumPy 和 Pillow。

```sh
python -m pip install numpy Pillow
python -m unittest discover -s tests -v
cd shortvideo_pipeline
python -m unittest discover -s tests -v
python -m shortvideo_pipeline.cli self-test
```

本地记录：公共回归测试 24 项、短视频原有测试 16 项通过；11 个技能入口通过格式校验；短视频包完成离线安装和命令行自检。远程 CI 的实际结果见 Actions，不把本地通过写成云端通过。

## 当前边界

3 个包是说明型技能；其余带辅助工具，也不代表已打通真实平台。没有自动获客、真实成交、生产视频渲染或实时平台可达性的证明。模式扫描可能漏报，形状分数不能证明来源或文字语义。

公开日期为 2026-10-15。旧目录和代码注释可用于追溯线索，不能替代完整开发历史；这次发布没有补造过去的提交。
