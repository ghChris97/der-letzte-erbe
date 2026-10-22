import shutil, os
src=open('src/index.html',encoding='utf-8').read()
os.makedirs('dist/img',exist_ok=True)
os.makedirs('dist/audio',exist_ok=True)
for f in os.listdir('src/audio'):
    shutil.copy(os.path.join('src/audio',f),os.path.join('dist/audio',f))
for f in os.listdir('src/img'):
    shutil.copy(os.path.join('src/img',f),os.path.join('dist/img',f))
t=src.index('</title>')+8
head_extra='''<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, interactive-widget=resizes-content">
<meta name="theme-color" content="#07090d">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="robots" content="noindex">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="img/icon-192.png">
<style>
:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);box-sizing:border-box}
body{margin:0;font-size:14px}
img{max-width:100%}
[hidden]{display:none!important}
@media (max-width:520px){
  :root{padding:0}
  body{padding:0!important}
  .phone{max-width:none;height:100%;border-radius:0;box-shadow:none}
  .status{padding-top:max(14px, env(safe-area-inset-top,0px))}
}
</style>
'''
head, rest = src[:t], src[t:]
MOBILE='''<style>
@media (max-width:520px){
  :root{padding:0!important}
  html,body{height:100%}
  body{padding:0!important}
  .phone{max-width:none!important;width:100%!important;height:100%!important;border-radius:0!important;box-shadow:none!important}
  .status{padding-top:max(14px, env(safe-area-inset-top,0px))}
}
</style>
'''
pre, post = rest.split('<div class="phone"',1)
html='<!doctype html>\n<html lang="de">\n<head>\n'+head_extra+head+'\n'+pre+MOBILE+'</head>\n<body>\n<div class="phone"'+post+'\n</body>\n</html>\n'
open('dist/index.html','w',encoding='utf-8').write(html)
shutil.copy('src/sw.js','dist/sw.js')
shutil.copy('netlify.toml','dist/netlify.toml')
open('dist/manifest.webmanifest','w').write('{"name":"Falkenrieds Handy","short_name":"Akte 1475","start_url":"./","scope":"./","display":"standalone","background_color":"#07090d","theme_color":"#07090d","lang":"de","icons":[{"src":"img/icon-192.png","sizes":"192x192","type":"image/png","purpose":"any"},{"src":"img/icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"}]}')
print("built", len(html))
