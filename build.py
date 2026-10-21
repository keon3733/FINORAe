import json,re
svg=open('src/logo.svg').read()
svg=re.sub(r'\s*\n\s*','',svg).replace('xmlns="http://www.w3.org/2000/svg" ','')
css=open('src/style.css').read()
js=open('src/core.js').read().replace('/*LOGO*/','const LOGO='+json.dumps(svg)+';')+open('src/views.js').read()+open('src/app.js').read()
html=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#43158B">
<meta name="description" content="Finora: track income, expenses, budgets and savings goals.">
<title>Finora</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap">
<style>
{css}
</style>
</head>
<body>
<div id="app"></div>
<div class="toasts" id="toasts" aria-live="polite"></div>
<script>
{js}
</script>
</body>
</html>
'''
open('index.html','w').write(html)
print(len(html))
