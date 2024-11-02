import src.TextureBuilder.builder

def print_tips_h():
    print('TIPS_H\n')

    for key, value in TIPS_H.items():
        print(f'{key}: {value}')
def print_tips():
    print('TIPS\n')

    for key, value in TIPS.items():
        if key == 'in_body':
            for ley, lue in value.items():
                print(f'body: ({ley}: {lue})')
                if ley == 'rect':
                    for ey, ue in lue.items():
                        print(f'body/rect: ({ey}: {ue})')
                if ley == 'triangle':
                    for ey, ue in lue.items():
                        print(f'body/triangle: ({ey}: {ue})')
        else:
            print(f'global: ({key}: {value})')

TIPS_H = {
    "必要": "必须填写, 否则报错!",
    "建议": "最好填写, 不填写为默认值",
    "可选": "自定义内容, 不填写为不触发",
    "特殊": "特殊的内容",
    "非必要": "如果要自定义的内容, 填写, 否则默认"
}

TIPS = {
    "id": "字符串, 建议, 决定生成文件后缀名, 默认: 'png'",
    "name": "字符串, 建议, 决定生成名, 默认: 'texture'",
    "type": "字符串, 必要, 决定是否识别, 必要值: 'texture'",
    "size": "字符串, 建议, 决定图片的大小, 格式: '高度x宽度', 默认: '64x64'",
    "width": "整数, 可选, 决定图片的长度, 层级: '低于size', 默认: 64",
    "w": "整数, 可选, 决定图片的长度, 层级: '低于width', 默认: 64",
    "height": "整数, 可选, 决定图片的宽度, 层级: '低于size', 默认: 64",
    "h": "整数, 可选, 决定图片的宽度, 层级: '低于height', 默认: 64",
    "background": "布尔, 可选, 决定是否绘制背景, 默认: false",
    "bg": "布尔, 可选, 决定是否绘制背景, 层级: '低于background', 默认: false",
    "background-color": "列表[整数], 层级: '低于background-color', 可选, 当bg为true时, 更换背景颜色, 默认: [0,0,0]",
    "bgc": "列表[整数], 可选, 当bg为true时, 更换背景颜色, 默认: [0,0,0]",
    "alpha": "整数, 可选, 决定绘制的透明度, 范围: 0~255, 默认: 255",
    "a": "整数, 可选, 决定绘制的透明度, 层级: '低于alpha', 范围: 0~255, 默认: 255",
    "body": "字典, 特殊, 决定子绘画内容, 格式: 'name': {value}",
    "in_body": {
        "name": "字符串, 必要, 无任何作用, 仅在构建时(控制台)显示, 格式: 全局body格式name",
        "value": "字典, 特殊, 决定body子绘画内容",
        "type": "字符串, 非必要, 默认: rect, TIPS: 每个type参数不一样",
        "rect": {
            "self": "body子类",
            "x": "整数, 建议, 决定Body的x位置, 默认: 0",
            "y": "整数, 建议, 决定Body的y位置, 默认: 0",
            "size": "字符串, 建议, 决定Body的大小, 格式: '高度x宽度', 默认: '64x64'",
            "width": "整数, 可选, 决定Body的长度, 层级: '低于size', 默认: 64",
            "height": "整数, 可选, 决定Body的宽度, 层级: '低于size', 默认: 64",
            "fill": "布尔, 可选, 决定是否填充, 默认: true",
            "alpha": "整数, 可选, 决定绘制填充的透明度, 范围: 0~255, 默认: 255",
            "color": "列表[整数], 可选, 当fill为true时, 更换填充颜色, 默认: [0,0,0]",
            "outline": "布尔, 可选, 决定是否绘制边框, 默认: false",
            "ol": "布尔, 可选, 决定是否绘制边框, 层级: '低于outline', 默认: false",
            "outline-size": "整数, 可选, 层级: '低于outline', 默认: 0",
            "ols": "整数, 可选, 层级: 'outline-size', 默认: 1",
            "outline-alpha": "整数, 可选, 决定绘制边框的透明度, 范围: 0~255, 默认: 255",
            "ola": "整数, 可选, 决定绘制边框的透明度, 范围: 0~255, 默认: 255"
        },
        "triangle": {
            "self": "body子类",
        }
    }
}

MODE_JSON: str = 'json'
MODE_DICT: str = 'dict'
MODE_BYTES: str = 'bytes'
MODE_LOAD: str = 'load'