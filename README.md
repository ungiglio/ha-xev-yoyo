# XEV Yoyo - Home Assistant Integration

<<<<<<< Updated upstream
Integrazione non ufficiale per monitorare la tua **XEV Yoyo** direttamente su Home Assistant. Grazie al reverse engineering dell'API ufficiale, questa integrazione permette di visualizzare i dati del veicolo senza passare dall'app mobile.
=======
Unofficial Home Assistant integration for the **XEV Yoyo Pro**, developed through reverse engineering of the official API.
>>>>>>> Stashed changes

## 📊 Features
* 🔋 **Battery Level**: SoC in percentage.
* 🛣️ **Range**: Estimated remaining distance in km.
* 📈 **Odometer**: Total mileage.
* 📍 **GPS Location**: Real-time position on the map.
* 🔒 **Lock Status**: Monitoring of the door locks.
* 🪟 **Windows**: Binary status (Closed vs. Any Open).

## ⚠️ Known Limitations
* **Windows**: The API only provides a global value (20 for all closed, 100 for any open). Individual window positions or percentage of opening are not available.
* **AC & Electronics**: Status for Air Conditioning, Fans, and Electronic Locks are currently static in the cloud API and do not reflect real-time vehicle changes.

## 🚀 Installation (HACS)
1. Open **HACS** > **Custom repositories**.
2. Add this GitHub URL as an **Integration**.
3. Install and **Restart** Home Assistant.
4. Go to **Settings > Devices & Services** and add "XEV Yoyo Pro".

---

# XEV Yoyo Pro - Integrazione Home Assistant (Italiano)

<<<<<<< Updated upstream
## ⚠️ Disclaimer
Questa integrazione non è affiliata né supportata da XEV. L'uso è a proprio rischio. Poiché utilizza API private, potrebbe smettere di funzionare in caso di aggiornamenti da parte del produttore.
=======
Integrazione non ufficiale creata tramite reverse engineering delle API XEV.

## 📊 Funzionalità
* 🔋 **Batteria**: Livello di carica in percentuale.
* 🛣️ **Autonomia**: Km residui stimati.
* 📈 **Contachilometri**: Chilometraggio totale.
* 📍 **Posizione GPS**: Visualizzazione su mappa.
* 🔒 **Serratura**: Stato di blocco/sblocco porte.
* 🪟 **Finestrini**: Stato binario (Tutti chiusi vs Almeno uno aperto).

## ⚠️ Limitazioni Note
* **Finestrini**: L'API fornisce solo un valore globale (20 per tutti chiusi, 100 per qualunque apertura). Non è possibile distinguere il lato o la percentuale.
* **AC e Servizi**: I dati relativi ad Aria Condizionata, Ventole e Blocchi Elettronici sono statici nell'API cloud e non riflettono lo stato reale istantaneo.
>>>>>>> Stashed changes
