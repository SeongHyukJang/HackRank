from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print("->", attr[0], ">", attr[1])

n = int(input())

parser = MyHTMLParser()

for i in range(n):
    parser.feed(input())