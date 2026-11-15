# turns the Claude artifact (pebbles.html) into the standalone web app (index.html) for GitHub Pages
s=open('claude-version.html').read()
s=s.replace('<title>Pebbles</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n','',1)
head='''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Pebbles">
<meta name="theme-color" content="#D9DEF5">
<title>Pebbles</title>
<link rel="manifest" href="manifest.webmanifest?v=3">
<link rel="apple-touch-icon" href="apple-touch-icon.png?v=3">
<link rel="icon" type="image/png" href="icon-192.png?v=3">
'''
k=s.index('</style>')+len('</style>')
open('index.html','w').write(head+s[:k]+'\n</head>\n<body>\n'+s[k:]+'\n</body>\n</html>\n')
