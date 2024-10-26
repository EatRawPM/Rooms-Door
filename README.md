# Rooms & Door
Horror games, including backrooms.

## 介绍

## 库

### 使用的Python库
* PyGame
* pillow

### 安装指令
```
pip install -r requirements.txt
```

#### 快速安装

在指令后加上

```
-i https://mirrors.aliyun.com/pypi/simple/
```

## 打包

### 使用pyinstaller打包。

### 打包

#### 测试打包

```
pyinstaller -F run.py -n RoomsAndDoors -i .\assets\images\icons\icon.ico
```

#### 正式打包

```
pyinstaller -F run.py -n RoomsAndDoors -w -i .\assets\images\icons\icon.ico
```
