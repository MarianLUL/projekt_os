# 🌤️ Weather App - FastAPI + Frontend

**Version:** 0.2.0

Jednoduché webové aplikace pro zobrazení počasí. Backend běží na FastAPI, frontend je statický HTML se styly. Data o počasí pochází z Visual Crossing API.

---

## Co potřebuješ mít nainstalované

### Minimální (pro spuštění bez Dockeru)
- **Python 3.8+** (Windows: stáhni z [python.org](https://www.python.org))
- **Git** (pro naklonování repozitáře)

### Pokud chceš Docker
- **Docker Desktop** (Windows: [stáhni zde](https://www.docker.com/products/docker-desktop))

## Postup instalace a spuštění

### 1️⃣ Klonuj nebo stáhni projekt

```powershell
# Přes Git (pokud máš nainstalovaný Git)
git clone <URL_REPO>
cd projekt_pocasi

# Nebo ručně: stáhni ZIP a rozbal do složky
```

### 2️⃣ Nastav API klíč

Projekt používá **Visual Crossing API** pro data o počasí.

1. Jdi na [visualcrossing.com](https://www.visualcrossing.com/)
2. Zaregistruj se (free plan má 1000 requestů/den)
3. Zkopíruj si svůj API klíč

Potom v `backend/` složce vytvoř soubor `.env.example`:

```powershell
# V PowerShell, z kořenu projektu
copy backend\.env.example backend\.env
```

Otevři `backend\.env` a vlož svůj klíč:

```
VISUALCROSSING_API_KEY=tvůj_klíč_zde
```

**⚠️ Důležité:** Nikdy nedávej `.env` na GitHub! Je už v `.gitignore`, ale kontroluj to.

---

## Spuštění aplikace

Máš tři možnosti. Vyber jednu:

### Možnost A: Makefile (nejrychlejší, pokud máš `make`)

Pokud máš na PC nainstalovaný `make` (např. přes Git Bash nebo MinGW):

```powershell
# Vytvoří venv a nainstaluje všechno
make install

# Spustí backend
make run-backend
```

Otevři v prohlížeči: **http://localhost:8000**

Chceš také frontend server? V novém okně terminálu:

```powershell
make run-frontend
```

Potom jdi na: **http://localhost:8080**

### Možnost B: Ručně s venv (doporučeno pro Windows)

```powershell
# 1. Jdi do backend složky
cd backend

# 2. Vytvoř virtuální prostředí (pomocí py launcher)
py -3 -m venv venv
# nebo
python -m venv venv
```
```
# 3. Aktivuj venv (PowerShell)
.\venv\Scripts\Activate.ps1
# nebo pro linux
source venv/bin/activate

# Pokud ti to nedovolí v PowerShell, zkus Command Prompt:
# .\venv\Scripts\activate.bat

# 4. Nainstaluj závislosti
pip install -r requirements.txt

# 5. Spustí aplikaci
python -m uvicorn main:app --reload --port 8000
```

Potom otevři: **http://localhost:8000**

### Možnost C: Docker Compose (pokud máš Docker Desktop)

```powershell
# V kořenu projektu
docker-compose up --build
```

- Backend běží na: **http://localhost:8000**
- Frontend běží na: **http://localhost:8080**

(Poznámka: Docker Desktop musí být spuštěný!)

---

## Jak se aplikace používá

1. Otevři v prohlížeči: **http://localhost:8000**
2. Zadej město (např. "Praha", "Brno", "London")
3. Klikni na "Hledat"
4. Vidíš:
   - 🌤️ Ikonu počasí
   - 🌡️ Aktuální teplotu
   - Pocitovou teplotu
   - Vlhkost vzduchu
   - Tlak
   - Rychlost větru

---

## Struktura projektu

```
projekt_pocasi/
├── backend/                    # FastAPI server
│   ├── main.py                # Hlavní aplikace
│   ├── requirements.txt        # Python závislosti
│   ├── .env.example            # Template pro API klíč
│   ├── .env                    # Tvůj lokální klíč (gitignore!)
│   └── venv/                   # Virtuální prostředí
├── frontend/                   # Statické HTML/CSS/JS
│   ├── index.html              # Hlavní stránka
│   └── style.css               # Styly
├── docker-compose.yml          # Spuštění s Dockerem
├── Dockerfile.backend          # Backend image
├── Dockerfile.frontend         # Frontend image
├── Makefile                    # Skratkové příkazy
├── CHANGELOG.md                # Historie verzí
└── README.md                   # Tento soubor
```

---

## Troubleshooting

### "Python was not found"
- Stáhni Python z [python.org](https://www.python.org)
- Při instalaci zaškrtni: ✅ "Add Python to PATH"
- Restartuj PowerShell/Terminal

### "No module named uvicorn"
- Ujisti se, že jsi v aktivovaném `venv`
- Znovu spusť: `pip install -r requirements.txt`

### "Cannot connect to API"
- Zkontroluj, že je `.env` v `backend/` složce s tvým klíčem
- Zkontroluj, že backend běží na http://localhost:8000
- Zkus: `curl http://localhost:8000/weather/Praha`

### Docker se nespustí
- Je Docker Desktop spuštěný? (Měl by běžet v pozadí)
- Zkus: `docker-compose down` a pak znovu `docker-compose up --build`

### Frontend se nemůže připojit k backendu
- Je backend spuštěný?
- Otvírej frontend přes **http://localhost:8000**, ne přes soubor
- Pokud používáš Docker, oba kontejnery musí být v síti

---

## Vývoj a přizpůsobení

### Změna API endpointu
Uprav `backend/main.py`, funkce `get_weather()` — tam si můžeš vyměnit Weather API.

### Změna stylů
Všechny styly jsou v `frontend/style.css` — CSS proměnné na začátku:

```css
:root {
  --primary-color: #2c3e50;
  --secondary-color: #3498db;
  /* ... */
}
```

### Spuštění v produkci

---

## Licence

MIT License - používej jak chceš

---

## Otázky?

Pokud něco nefunguje, zkontroluj:
1. ✅ Je Python 3.8+ nainstalovaný?
2. ✅ Máš `.env` soubor s Visual Crossing API klíčem?
3. ✅ Je backend spuštěný na portu 8000?
4. ✅ Otvíráš správnou URL v prohlížeči?

Hodně štěstí! 🚀



