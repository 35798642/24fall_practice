

# 裁判文书系统设计与实现

本项目旨在开发一个裁判文书系统，可自动提取裁判文书中的关键信息，如案由、法院、审判员、原告和被告等等。采用PyQt的前端框架，统一信息抽取模型UIE算法来自动提取司法文本中的关键信息。

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
  - [运行](#运行)
- [文件目录说明](#文件目录说明)
- [使用到的框架](#使用到的框架)
- [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

###### 开发前的配置要求

1. python >= 3.9.0
2. openpyxl
3. csv
4. pandas
5. PyQt5
6. PyQt-Fluent-Widgets
7. textract
8. frontend
9. pymupdf
10. paddlepaddle
11. paddlenlp

###### **安装步骤**

1. Clone the repo

```sh
git clone https://github.com/35798642/24fall_practice.git
```
2. Pip install dependence
```sh
pip install xxx
```
###### **运行**
```sh
python Main.py
```
### 文件目录说明
eg:

```
filetree 
├── __init__.py 初始化文件
├── README.md 使用文档
├── /img/ 界面背景图片以及图标
├── /input/ 输入表格文件示例
├── /text/
│  ├── test1.txt
│  ├── test2.docx
│  ├── test3.pdf
├── Main.py 主函数，运行该文件
├── Button.py 按钮类，设置按钮样式并绑定监听信号
├── Left.py 界面左窗口，包括文本和文件输入功能、关键信息提取、高亮功能
├── SegmentedButton.py 选项卡切换按钮
├── Table.py 表格类，表格展示、编辑修改、表格格式文件的导入导出
└── MainWindow.py 主窗口，总体布局格式

```


### 使用到的框架

- [PyQt5](https://pypi.org/project/PyQt5/)
- [Paddlepaddle](https://www.paddlepaddle.org.cn)

### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

2565039577@qq.com
673787610@qq.com
1612594623@qq.com
1357775985@qq.com

### 鸣谢


- [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
- [Img Shields](https://shields.io)
- [Choose an Open Source License](https://choosealicense.com)
- [GitHub Pages](https://pages.github.com)
- [Animate.css](https://daneden.github.io/animate.css)
- [xxxxxxxxxxxxxx](https://connoratherton.com/loaders)

<!-- links -->
[your-project-path]:35798642/24fall_practice
[contributors-shield]: https://img.shields.io/github/contributors/35798642/24fall_practice.svg?style=flat-square
[contributors-url]: https://github.com/35798642/24fall_practice/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/35798642/24fall_practice.svg?style=flat-square
[forks-url]: https://github.com/35798642/24fall_practice/network/members
[stars-shield]: https://img.shields.io/github/stars/35798642/24fall_practice.svg?style=flat-square
[stars-url]: https://github.com/35798642/24fall_practice/stargazers
[issues-shield]: https://img.shields.io/github/issues/35798642/24fall_practice.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/35798642/24fall_practice.svg
[license-shield]: https://img.shields.io/github/license/35798642/24fall_practice.svg?style=flat-square
[license-url]: https://github.com/35798642/24fall_practice/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/shaojintian
