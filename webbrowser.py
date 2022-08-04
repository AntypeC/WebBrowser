import webbrowser

url = "www.google.com"
# edge_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

class browser():

    webbrowser.register(name='edge', klass=None)
    webbrowser.open(url, new=1, autoraise=True)

browser()