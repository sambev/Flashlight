import matplotlib.colors as colors

def rgbFromHex(hexString):
    if hexString.find("#") != -1:
        hexString = hexString[1:]

    if len(hexString) < 6:
        hexString = "".join([2*value for value in hexString])

    hexString = "#"+hexString

    rgb = colors.hex2color(hexString)

    return tuple([int(255.0*x) for x in rgb])

def colorString(rgb, swift = False):
    isGray = (rgb[0] == rgb[1] and rgb[1] == rgb[2])
    if isGray:
        white = rgb[0]/255.0
        if swift:
            return "UIColor(white: {0:.3f})".format(white)
        else:
            return "[UIColor colorWithWhite: {0:.3f}f]".format(white)
    else:
        if swift:
            return "UIColor(red: {0:.3f}, green: {1:.3f}, blue: {2:.3f})".format(rgb[0], rgb[1], rgb[2])
        else:
            return "[UIColor colorWithRed: {0:.3f}f green: {1:.3f}f blue: {2:.3f}f]".format(rgb[0], rgb[1], rgb[2])


def results(parsed, original_query):
    useSwift = ("translate_to_swift" in parsed)
    hexValue = parsed["*hex_color"]
    rgb = rgbFromHex(hexValue)
    string = colorString(rgb, useSwift)

    html = """
    <div style='font-weight: normal; font-family: "HelveticaNeue-Light", "Helvetica Neue Light", "Helvetica Neue", Helvetica, Arial; line-height: 1.2'>
    <h2 >{0}</h2>
    <p style='color: gray'>Press enter to copy</p>
    </div>
    """.format(string)

    return {"title": "'UIColor from {0}'".format(hexValue), "html": html, "run_args": [string]}

def run(message):
    import os
    os.system('echo ' + message + " | pbcopy && osascript -e 'display notification \"Color copied to clipboard.\" with title \"Flashlight\"'")

