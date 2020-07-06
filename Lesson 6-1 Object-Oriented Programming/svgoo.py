
WIDTH=700
HEIGHT=700

class SVGDrawing:

    svgdata: list

    def __init__(self):
        self.svgdata = []

    def addRect(self, x: float, y: float, width: float, height: float, color: str):
        self.svgdata.append(
            f"<rect x='{x}' y='{y}' width='{width}' height='{height}' fill='{color}' />"
        )

    def addLine(self, x1: float, y1: float, x2: float, y2: float, color: str):
        self.svgdata.append(
            f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{color}' />"
        )

    def toHTML(self) -> str:
        svgstring = '\n'.join(self.svgdata)
        return SVGDrawing.HTML_PAGE.format(WIDTH, HEIGHT, svgstring)

    HTML_PAGE = """
<!DOCTYPE html>
<html>
<body>

<svg width="{0}" height="{1}">
  {2}
</svg>

</body>
</html>
"""

def makedrawing(): 
    drawing = SVGDrawing()

    drawing.addRect(x=0, y=0, width=700, height=700, color='black')

    for x in range(0, WIDTH+1, 100):
        drawing.addLine(x1=x, y1=0, x2=x, y2=HEIGHT, color='green')

    return drawing

drawing = makedrawing()
html = drawing.toHTML()

with open('demo.html', 'w') as f:
    f.write(html)
    
