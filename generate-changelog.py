"""Regenerate the public HTML page and Markdown history from releases.json."""
from pathlib import Path
import json
from html import escape
root=Path(__file__).resolve().parent
data=json.loads((root/'releases.json').read_text())
original=(root/'index.html').read_text()
style=original.split('<style>',1)[1].split('</style>',1)[0]
extra='''
.status { display:inline-block; border-radius:999px; padding:5px 10px; font-size:.8rem; background:#EEEAFB; color:#5546C6; font-weight:600; }
.release-heading { display:flex; gap:12px; align-items:center; flex-wrap:wrap; margin-bottom:12px; }
.release-heading h2 { margin:0; }
.note { border-left:3px solid #B9B0FF; padding-left:12px; }
.feedback-actions { display:flex; gap:12px; flex-wrap:wrap; }
.feedback-link.secondary { background:transparent; color:#5546C6; border:1px solid #B9B0FF; }
@media (prefers-color-scheme:dark) { .feedback-link.secondary { color:#C9C1FF; } }
.feedback-link { display:inline-block; border-radius:12px; padding:12px 18px; background:#5546C6; color:white; text-decoration:none; font-weight:600; }
.beta-calculator { margin-top:12px; }
@media (prefers-color-scheme:dark) { .status { background:#393052; color:#C9C1FF; } }
'''
def bilingual(tag,en,zh,css=''):
 return f'<{tag} class="en {css}">{escape(en)}</{tag}><{tag} class="zh {css}">{escape(zh)}</{tag}>'
sections=[]
md=['# PayCalculator AU — Release history / 更新日志','',f'Last updated / 更新日期: {data["updated"]}', '', 'Release availability is listed for each version. / 每个版本分别标明分发状态。','']
for release in data['releases']:
 v=escape(release['version'])
 heading=f'<div class="release-heading"><h2>v{v}</h2>'+bilingual('span',release['status_en'],release['status_zh'],'status')+'</div>'
 content=bilingual('p',release['summary_en'],release['summary_zh'])
 content+='<ul>'+''.join('<li><span class="en">'+escape(f['en'])+'</span><span class="zh">'+escape(f['zh'])+'</span></li>' for f in release['features'])+'</ul>'
 if release.get('note_en'): content+=bilingual('p',release['note_en'],release['note_zh'],'muted note')
 sections.append(f'<section id="v{v}">{heading}{content}</section>')
 md += [f'## {release["version"]} — {release["status_en"]} / {release["status_zh"]}','',release['summary_en'],release['summary_zh'],'']
 for f in release['features']:md.append('- '+f['en']+' / '+f['zh'])
 if release.get('note_en'):md += ['',release['note_en'],release['note_zh']]
 md.append('')
feedback=bilingual('h2','Ideas & feedback','新需求与反馈')+bilingual('p','Tell us what would make PayCalculator AU more useful. Suggestions and bug reports are welcome.','告诉我们怎样让 PayCalculator AU 更好用，欢迎提出新需求或报告问题。')
feedback+='<div class="feedback-actions"><a class="feedback-link" href="mailto:tmt@goldman-stanley.com?subject=PayCalculator%20AU%20feedback"><span class="en">Email feedback</span><span class="zh">邮件留言</span></a><a class="feedback-link secondary" href="https://github.com/goldman-stanley/paycalculator-au-pages/issues/new/choose"><span class="en">Comment on GitHub</span><span class="zh">登录 GitHub 留言</span></a></div>'
feedback+=bilingual('p','Email us for a private conversation, or sign in to GitHub to submit an idea or report a bug. We can reply by email or in the same GitHub issue. GitHub posts and replies are public.','希望私下沟通可发送邮件；也可登录 GitHub 提交新需求或报告问题。我们会通过邮件或在同一条 GitHub 记录中回复。GitHub 留言及回复公开可见。','muted')
feedback+='<p><a href="https://github.com/goldman-stanley/paycalculator-au-pages/issues"><span class="en">Browse suggestions and replies →</span><span class="zh">查看已有建议与回复 →</span></a></p>'
feedback+=bilingual('p','Include your app version for bug reports. Please avoid personal tax or bank details.','报告问题时请附应用版本，勿附个人税号或银行资料。','muted')
html=f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="description" content="PayCalculator AU release history, new features and feedback."><link rel="icon" type="image/png" href="app-icon.png"><title>PayCalculator AU — What's new</title><style>{style}{extra}</style></head>
<body data-language="en"><header><button class="language" type="button" aria-label="Switch language" onclick="switchLanguage()">中文</button><img class="brand-icon" src="app-icon.png" alt="" width="64" height="64"><h1>PayCalculator AU</h1>{bilingual('p',"What's new",'更新日志')}<a class="feedback-link beta-calculator" href="https://goldman-stanley.github.io/paycalculatorau/"><span class="en">Open Web Beta calculator →</span><span class="zh">打开网页版计算器 Beta →</span></a></header>
<main><nav aria-label="Site navigation"><a href="index.html#privacy"><span class="en">Privacy</span><span class="zh">隐私</span></a><a href="index.html#support"><span class="en">Support</span><span class="zh">支持</span></a><a href="#feedback"><span class="en">Ideas & feedback</span><span class="zh">需求与反馈</span></a></nav>{bilingual('p','Release history · Updated '+data['updated'],'版本记录 · 更新日期 '+data['updated'],'muted')}
{''.join(sections)}
<section id="feedback">{feedback}</section></main><footer>PayCalculator AU · Australia</footer>
<script>
function setLanguage(next) {{ document.body.dataset.language = next; document.documentElement.lang = next; document.querySelector('.language').textContent = next === 'en' ? '中文' : 'English'; }}
function switchLanguage() {{ const next = document.body.dataset.language === 'en' ? 'zh' : 'en'; setLanguage(next); const url = new URL(location.href); url.searchParams.set('lang', next); history.replaceState(null, '', url); }}
setLanguage(new URLSearchParams(location.search).get('lang') === 'zh' ? 'zh' : 'en');
</script></body></html>'''
(root/'changelog.html').write_text(html)
(root/'CHANGELOG.md').write_text('\n'.join(md))
