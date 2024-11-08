from src.console import ServerTitle, ClientTitle

if ClientTitle == '':
    if ServerTitle == '':
        Title = 'Rooms&Doors'
    else:
        Title = ServerTitle
else:
    Title = ClientTitle