# Flatex-Documents-Download-Helper

Das Skript erlaubt es mittels per Selenium gesteuerten Chrome-Browser PDF-Dokumente aus dem 
Dokumentenarchiv  von Flatex herunterzuladen. 

### Entwicklungs- und Testumgebung

- Windows 10 (64 Bit) Version 20H2
- Python 3.8.3
- Chrome Browser Version 88.0.4324.104

### Anleitung

1. Python herunterladen und installieren: https://www.python.org/downloads/
2. Requirements installieren: `pip install -r requirements.txt`
3. Chrome Browser herunterladen: https://www.google.com/chrome/
4. Zur Browser Version passenden Chrome Driver herunterladen
    - Download: https://chromedriver.chromium.org/downloads
    - Den Chrome Driver (also der Ordner, in dem er sich befindet) in den PATH (in den Windows Umgebungsvariablen) 
     eintragen, damit er von Selenium gefunden wird
5. Den Chrome Browser so konfigurieren, dass PDF-Dateien direkt heruntergeladen werden anstatt sie im Chrome zu öffnen
    - entsprechendes Menü über folgende URL im Chrome-Browser öffnen: `chrome://settings/content/pdfDocuments`
    - Menüpunkt aktivieren: *PDF-Dateien herunterladen, anstatt sie automatisch in Chrome zu öffnen*
6. Chrome über die Kommandozeile starten
    - Befehl: `chrome.exe -remote-debugging-port=9999`
    - Der verwendete Port (hier bspw. `9999`) muss später auch als Parameter im Skript übergeben werden. 
      Dies erlaubt es Selenium sich auf einen *bereits geöffneten* Chrome-Browser zu verbinden, anstatt einen neuen 
      zu starten
    - Das Browserfenster maximieren, um zu gewährleisten, dass alle HTML-Elemente angezeigt werden
5. Vorbereitungen im Flatex Konto vornehmen
    - Flatex (https://www.flatex.de) im eben geöffneten Chrome-Browser aufrufen
    - manuell ins Flatex Konto einloggen 
    - über das Menü "Post" ins "Dokumentenarchiv" navigieren
6. Manuelle Filtereinstellungen im Dokumentenarchiv vornehmen
    - Die Filter entsprechend anpassen, sodass die gewünschten Dokumente aufgelistet werden (das Programm kann nur die 
      momentan sichtbaren Dokumente in der Liste herunterladen)
    - Achtung: Flatex stellt maximal 100 Dokumente auf einmal dar (eine entsprechende Warnung wird über der Liste 
      angezeigt)
    - das bedeutet, man muss den Filter (gewünschtes Datum, gewünschte Dokumentenart, etc.) entsprechend anpassen, 
      sodass maximal 100 Dokumente auf einmal angezeigt werden. Ebenfalls wichtig ist es, den Filter auf "Alle" und 
      nicht nur auf "Gelesene" oder "Ungelesene" zu stellen, da sonst nicht alle Dokumente angezeigt werden.
7. Sobald der Filter eingestellt ist und die gewünschten Dokumente in der Liste angezeit werden, kann das Skript über 
   die Kommandozeile gestartet werden.
    - Befehl: `python flatex.py --port 9999`
    - Der Download lief bei mir schneller, wenn das Browserfenster währenddessen im Vordergrund lief
