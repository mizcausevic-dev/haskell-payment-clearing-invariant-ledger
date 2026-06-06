$ErrorActionPreference = "Stop"
New-Item -ItemType Directory -Force -Path "screenshots" | Out-Null
@'
from PIL import Image, ImageDraw, ImageFont
W,H=1280,720
bg=(5,8,18); panel=(13,23,39); text=(244,241,234); muted=(168,179,199); cyan=(37,215,239); green=(88,240,179); pink=(255,114,182); violet=(157,140,255)
try:
    title=ImageFont.truetype('C:/Windows/Fonts/segoeuib.ttf', 58)
    body=ImageFont.truetype('C:/Windows/Fonts/segoeui.ttf', 25)
    small=ImageFont.truetype('C:/Windows/Fonts/consolab.ttf', 18)
    serif=ImageFont.truetype('C:/Windows/Fonts/georgiab.ttf', 46)
except Exception:
    title=body=small=serif=ImageFont.load_default()
def wrap(draw, text_value, font, max_width):
    words=text_value.split()
    lines=[]; current=''
    for word in words:
        candidate=(current + ' ' + word).strip()
        if draw.textbbox((0,0), candidate, font=font)[2] <= max_width:
            current=candidate
        else:
            if current:
                lines.append(current)
            current=word
    if current:
        lines.append(current)
    return lines
im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
d.rounded_rectangle([48,48,1232,672], radius=28, fill=panel, outline=cyan, width=2)
d.text((96,106),'HASKELL PAYMENT CLEARING INVARIANT LEDGER',font=small,fill=green)
d.text((96,178),'Settlement exceptions stay provable',font=serif,fill=text)
d.text((96,238),'before liquidity risk becomes a board surprise.',font=serif,fill=text)
d.text((96,332),'Unmatched debits, late batches, holds, overrides, and reconciliation',font=body,fill=muted)
d.text((96,372),'delay resolve into one operator-safe clearing proof.',font=body,fill=muted)
for i,(label,val) in enumerate([('AGGREGATE SCORE','67.74'),('ESCALATION LANES','2'),('VOLUME AT RISK','$4.48M'),('TOP LANE','same-day ACH')]):
    x=96+i*272
    d.rounded_rectangle([x,490,x+240,604],radius=18,fill=(16,28,48),outline=(40,48,66),width=1)
    d.text((x+20,528),label,font=small,fill=muted)
    d.text((x+20,562),val,font=title if i < 3 else small,fill=text)
im.save('screenshots/01-overview-proof.png')
im=Image.new('RGB',(W,H),bg); d=ImageDraw.Draw(im)
d.text((64,70),'Clearing invariant lanes',font=serif,fill=text)
def card(x,y,w,h,outline,label,heading,bodytxt,metric):
    d.rounded_rectangle([x,y,x+w,y+h],radius=22,fill=panel,outline=outline,width=2)
    d.text((x+28,y+34),label,font=small,fill=cyan)
    d.text((x+28,y+88),heading,font=body,fill=text)
    yy=y+150
    for line in wrap(d,bodytxt,body,w-56):
        d.text((x+28,yy),line,font=body,fill=muted)
        yy += 34
    d.text((x+28,y+h-86),metric,font=title,fill=text)
card(64,150,360,430,pink,'ESCALATE','Same-day ACH','Debit-credit parity and liquidity holds need proof before cutover.','100.0')
card(464,150,360,430,violet,'WATCH','Card clearing','Adjustment reason codes need settlement evidence.','71.6')
card(864,150,360,430,green,'CONTAINED','Wire review','Daily liquidity controls remain usable.','31.6')
im.save('screenshots/02-ledger-proof.png')
'@ | python -

