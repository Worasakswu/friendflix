# 🎓 Friendflix — Congrats, Friend!

เว็บแสดงความยินดีกับ **เฟรน** ที่เรียนจบจาก **มหาวิทยาลัยเกษตรศาสตร์ (KU 82)** ในธีม Netflix

**🔗 เปิดเว็บ:** https://friendflix.streamlit.app

## Flow

1. **Instagram** — แตะสตอรี่ `friend__ft` ที่มีวงแดง
2. **Intro** — โลโก้ **F** + เสียง ta-dum
3. **Who's watching?** — เลือกโปรไฟล์ Friend
4. **Home** — *FRIEND* series, Continue Watching (ปี 1–4), Top 10, Categories
5. **Details** — *Friend: The Graduate* · Download (โปสเตอร์ที่ระลึก) · Rate · Share
6. **Play** — สไลด์โชว์ + เพลง → **Series Finale: Congratulations 🎓**

มีหน้า Search, Categories, New & Hot และ My Friendflix ด้วย

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

`index.html` เปิดตรง ๆ ผ่าน static server ได้เหมือนกัน (`python -m http.server`)

## Files

| Path | |
| --- | --- |
| `index.html` | หน้าเว็บทั้งหมด (HTML/CSS/JS) |
| `app.py` | Streamlit wrapper — ฝังรูปเป็น data URI แล้วแสดงเต็มจอ |
| `assets/` | รูปของเฟรน |
