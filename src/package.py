from src.console import ServerTitle, ClientTitle

Title = 'Rooms&Doors' if not ServerTitle else (ServerTitle if not ClientTitle else ClientTitle)