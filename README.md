# ReportBot
~ 报告生成小助手

## Background

- 想回顾一下自己过去这一周都做了什么？
- 想把自己在 Issue 和 Comments 中写过的文字都保留一份存档？
- 想追踪自己感兴趣的人，比如 @ZoomQuiet 这一年来都做了些什么？
- ...

手工查阅好麻烦，能不能一键生成 Markdown 文档呢？
别急，ReportBot 来帮你

## Usage

~ du4proto 仓库 -> DU_tools 分支 -> ReportBot 目录
[Link](https://github.com/DebugUself/du4proto/blob/DU_tools/ReportBot/repobot.py)

`$ python3 repobot.py`

- 输入你感兴趣的人的 Github Username, 如 `zoejane`
- 输入你想追踪的多少天, 比如 `7`

小助手就会自动在你运行程序的目录下，生成三份 Markdown 格式的报告啦

- username-commits-report.md
- username-issues-report.md
- username-commit-comments-report.md

运行需要 PyGithub 支持 

`$ pip3 install PyGithub`

## 彩蛋

大妈 @ZoomQuiet 过去一年 (截止到2018.4.4.) 在怼圈的的各种嗯哼，里面可以发掘出超多大妈给的隐藏任务喔 :)

- [zoomquiet-issues-report-20180404.md](https://gist.github.com/zoejane/b3d66acdc29f8518cca58b1bd0bec5ee)
- [zoomquiet-commits-report-20180404.md](https://gist.github.com/zoejane/50384f5d3a10f95c065860d40d17f634)
- [zoomquiet-commit-comments-report-20180404.md](https://gist.github.com/zoejane/1c144d20b57c0e4ab5c6be963ce4c059)

## Links

- [5d [ANN] ReportBot 报告生成小助手发布 (附彩蛋:大妈嗯哼合集) · Issue #373 · DebugUself/du4proto](https://github.com/DebugUself/du4proto/issues/373)

## Changelog

- 180405 zoejane 发布 v18.4.5
- 180401 zoejane 启动 ReportBot 项目

