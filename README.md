[![v1.0.0](https://img.shields.io/badge/release-v1.0.0-blue)](https://github.com/ungiglio/ha-xev-yoyo/releases/tag/v1.0.0) [![License MIT](https://img.shields.io/badge/license-MIT-lightgrey)](https://github.com/ungiglio/ha-xev-yoyo?tab=MIT-1-ov-file)

# XEV Yoyo - Home Assistant Integration

Unofficial Home Assistant integration for the **XEV Yoyo** electric vehicle. This component has been developed by reverse engineering the official mobile application APIs to allow local monitoring of vehicle data.

## Features

* **Battery Management**: Real-time State of Charge (SoC) percentage.
* **Range Estimation**: Remaining autonomy expressed in kilometers.
* **Odometer**: Total mileage tracking.
* **Location Tracking**: GPS coordinates for map visualization.
* **Security**: Monitoring of door lock status.
* **Windows**: Binary status (reports if all windows are closed or if any are open).

## Technical Limitations

* **Windows**: The cloud API currently provides a global value (e.g., `20` for all closed, `100` for any opening). It is not possible to distinguish between left/right windows or identify the specific percentage of opening.
* **Real-time Updates**: Status for Air Conditioning, Fans, and specific Electronic Locks are static in the current API version and may not reflect immediate changes made inside the vehicle.
* **Cloud Dependency**: This integration relies on XEV cloud servers; an active internet connection for the vehicle is required.

## Installation via HACS

1. Navigate to Settings > Marketplace (for Home Assistant 2026.11 and newer) or HACS (Must be installed) > Integrations (for older versions).
2. Search for "XEV Yoyo" and select it from the list.
3. Click Download and, once finished, restart Home Assistant.
4. Go to Settings > Devices & Services > Add Integration.
5. Search for "XEV Yoyo" and follow the setup instructions.

---

# XEV Yoyo - Integrazione Home Assistant (Italiano)

Integrazione non ufficiale per il veicolo elettrico **XEV Yoyo**, sviluppata tramite reverse engineering delle API ufficiali utilizzate dall'app mobile.

## Funzionalità

* **Batteria**: Livello di carica residua (SoC) in percentuale.
* **Autonomia**: Chilometri residui stimati.
* **Contachilometri**: Monitoraggio del chilometraggio totale del veicolo.
* **Posizione**: Tracker GPS per la visualizzazione sulla mappa di Home Assistant.
* **Serrature**: Stato di blocco/sblocco delle portiere.
* **Finestrini**: Stato binario (segnala se i finestrini sono tutti chiusi o se almeno uno risulta aperto).

## Limitazioni Note

* **Dettaglio Finestrini**: L'API fornisce un valore aggregato (es. `20` per "tutto chiuso", `100` per "apertura rilevata"). Non è possibile determinare quale specifico finestrino sia aperto o la sua percentuale.
* **Servizi Ausiliari**: I dati relativi a Climatizzatore (AC), ventole e blocchi elettronici secondari sono attualmente statici nel cloud XEV e potrebbero non riflettere lo stato istantaneo del veicolo.
* **Dipendenza Cloud**: L'integrazione richiede che il veicolo sia connesso alla rete e che i server XEV siano raggiungibili.

## Installazione

1. Naviga in Impostazioni > Marketplace (Per Home Assistant 2026.11 e più recenti) oppure HACS (già installato) > Integrazioni (Per le versioni più vecchie).
2. Cerca "XEV Yoyo" e selezionalo dai risultati.
3. Clicca su Scarica e, una volta terminato, riavvia Home Assistant.
4. Vai in Impostazioni > Dispositivi e Servizi > Aggiungi integrazione.
5. Cerca "XEV Yoyo" e segui la procedura di configurazione.

---

This integration is not affiliated with or endorsed by XEV. All logos and trademarks are the property of their respective owners.