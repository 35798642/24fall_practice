

# 裁判文书系统设计与实现

本项目旨在开发一个裁判文书系统，可自动提取裁判文书中的关键信息，如案由、法院、审判员、原告和被告等等。采用PyQt的前端框架，统一信息抽取模型UIE算法来自动提取司法文本中的关键信息。

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
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

### 文件目录说明
eg:

```
filetree 
├── ARCHITECTURE.md
├── LICENSE.txt
├── README.md
├── /account/
├── /bbs/
├── /docs/
│  ├── /rules/
│  │  ├── backend.txt
│  │  └── frontend.txt
├── manage.py
├── /oa/
├── /static/
├── /templates/
├── useless.md
└── /util/

```


### 使用到的框架

- [xxxxxxx](https://getbootstrap.com)
- [xxxxxxx](https://jquery.com)
- [xxxxxxx](https://laravel.com)

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

xxx@xxxx

知乎:xxxx  &ensp; qq:xxxxxx    

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/35798642/24fall_practice/blob/master/LICENSE.txt)

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
