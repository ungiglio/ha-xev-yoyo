# XEV Yoyo - Home Assistant Integration

Integrazione non ufficiale per monitorare la tua **XEV Yoyo** direttamente su Home Assistant. Grazie al reverse engineering dell'API ufficiale, questa integrazione permette di visualizzare i dati del veicolo senza passare dall'app mobile.

## 📊 Sensori inclusi
- 🔋 **Livello Batteria**: Stato della carica in percentuale.
- 🛣️ **Autonomia**: Km residui stimati.
- 📈 **Odometer**: Chilometraggio totale del veicolo.
- ⚡ **Stato**: Monitoraggio (In Carica, Standby, Disconnessa).

## 🚀 Installazione

### Tramite HACS (Consigliato)
1. Apri **HACS** in Home Assistant.
2. Clicca sui tre puntini in alto a destra e seleziona **Repository personalizzati**.
3. Incolla l'URL di questo repository e seleziona la categoria **Integrazione**.
4. Clicca su **Installa**.
5. Riavvia Home Assistant.

### Manuale
Copia la cartella `custom_components/xev_yoyo` nella cartella `custom_components` della tua installazione di Home Assistant e riavvia.

## ⚙️ Configurazione
Una volta installata, vai in **Impostazioni -> Dispositivi e Servizi -> Aggiungi Integrazione** e cerca "XEV Yoyo Pro".
Ti verranno richiesti i seguenti dati (ottenibili tramite sniffing del traffico dell'app):
- **UUID**
- **App Key**
- **Bearer Token**
- **Vehicle ID**

## ⚠️ Disclaimer
Questa integrazione non è affiliata né supportata da XEV. L'uso è a proprio rischio. Poiché utilizza API private, potrebbe smettere di funzionare in caso di aggiornamenti da parte del produttore.
