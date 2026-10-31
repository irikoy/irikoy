import json,os,urllib.request
REPO="irikoy/qBittorrent-Iriel-Dark-Theme"
SANS="-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
STAR="M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.75.75 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Z"
req=urllib.request.Request(f"https://api.github.com/repos/{REPO}",headers={"User-Agent":"profile-card",**({"Authorization":"Bearer "+os.environ["GITHUB_TOKEN"]} if os.environ.get("GITHUB_TOKEN") else {})})
stars=json.load(urllib.request.urlopen(req))["stargazers_count"]
W,H=560,96
n=str(stars); pw=int(46+len(n)*8)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Iriel, a dark qBittorrent theme. {stars} stars">
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="14" fill="#0a0a0a" stroke="#ffffff" stroke-opacity="0.16"/>
<text x="24" y="40" font-family="{SANS}" font-size="20" font-weight="700" letter-spacing="-0.4" fill="#ededed">Iriel</text>
<text x="24" y="66" font-family="{SANS}" font-size="13.5" fill="#8b8b8b">A dark qBittorrent theme inspired by Vercel's Geist design system.</text>
<g transform="translate({W-24-pw},20)">
<rect x="0.5" y="0.5" width="{pw-1}" height="26" rx="8" fill="none" stroke="#ffffff" stroke-opacity="0.16"/>
<g transform="translate(11,6)" fill="#ededed"><path d="{STAR}"/></g>
<text x="33" y="17.5" font-family="{SANS}" font-size="12.5" font-weight="600" fill="#ededed">{n}</text>
</g>
</svg>'''
open(os.path.join(os.path.dirname(__file__),"..","assets","card-project.svg"),"w",encoding="utf-8").write(svg)
print("stars",stars)
