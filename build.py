import os

if __name__ == '__main__':
    os.system("pyinstaller -F run.py -n RoomsAndDoors -w -i assets\images\icons\icon.ico")
    print('构建已完成')