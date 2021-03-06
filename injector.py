# Usage: mitmdump -s "js_injector.py src"
# (this script works best with --anticache)
from bs4 import BeautifulSoup
import mitmproxy 
import argparse

class Injector:
    def __init__(self, path):
        self.path = path

    def response(self, flow):
        if self.path:
            html = BeautifulSoup(flow.response.content, "html.parser")
            print(self.path)
            print(flow.response.headers["content-type"])
            if flow.response.headers["content-type"] == 'text/html':
                print(flow.response.headers["content-type"])
                script2 = html.new_tag(
                    "script",
                    src=self.path,
                    type='application/javascript')
                html.body.insert(0, script2)
                flow.response.content = str(html)
                print("Script injected.")

def start():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    args = parser.parse_args()
    return Injector(args.path)
