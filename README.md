# WFS Downloader

Hier finden sich einige Beispiele wie der WFS Download Client genutzt werden kann.



## Landschaftsrahmenpläne für die Planungsräume I bis III

Herausgegeben vom Ministerium für Energiewende, Klimaschutz, Umwelt und Natur des Landes Schleswig-Holstein vom Referat für Landschaftsplanung, Eingriffsregelung, UVP, Sport und Erholung.


### Schutzgebiete für Natur und Landschaft, Biotopverbund und Avifauna

- app:KARTE1_NAHRUNG_GANS_2020
- app:KARTE1_NSG_BESTAND_2020
- app:KARTE1_BIOSPHAERENRESERV_POINT_2020
- app:KARTE1_BIOSPHAERENRESERVATE_2020
- app:KARTE1_SEEADLER_DICHT_V2_2020
- app:KARTE1_WSG_AUSSENGRENZE_2020
- app:KARTE1_WSG_P_2020
- app:KARTE1_NP_LLUR_V2_2020
- app:KARTE1_NATURA2000_2020
- app:KARTE1_NATURWALD_2020
- app:KARTE1_SONDERGEB_BUND_2020
- app:KARTE1_WGG_2020
- app:KARTE1_NSG_VORSCHLAG_2020
- app:KARTE1_VORRANGFLIESSGEWAESSER_2020
- app:KARTE1_VORRANGSEEN_2020
- app:KARTE1_WIESENVOGELGE_2020
- app:KARTE1_KUESTREIF_NAHR_2020
- app:KARTE1_WSG_ZONEN_2020
- app:KARTE1_P21GR20HA_LA_V2_2020
- app:KARTE1_BVS_2020
- app:KARTE1_FFH_GEBIETE_POINT_2020
- app:KARTE1_SEEADLER_PUF_V2_2020
- app:KARTE1_SPA_GEBIETE_PO_2020

```sh
python3 wfs_downloader.py --prefix sh --version 2.0.0 --service WFS --format 'application/gml+xml; version=3.2' --from_crs EPSG:25832 --to_crs EPSG:4326 --url https://umweltgeodienste.schleswig-holstein.de/WFS_LRP_Karte1_2020
```


### Landschaft und Erholung

- app:KARTE2_LSG_BESTAND_2020
- app:KARTE2_GEB_BESON_ERHOLEIGN_2020
- app:KARTE2_BEET_UND_GRUEPPEN_2020
- app:KARTE2_HISTOR_KNICKLANDSCH_2020
- app:KARTE2_NATURPARK_2020
- app:KARTE2_LSG_VORSCHLAG_2020

```sh
python3 wfs_downloader.py --prefix sh --version 2.0.0 --service WFS --format 'application/gml+xml; version=3.2' --from_crs EPSG:25832 --to_crs EPSG:4326 --url https://umweltgeodienste.schleswig-holstein.de/WFS_LRP_Karte2_2020
```


### Klimaschutz, Boden und Rohstoffe

- app:KARTE3_GEOTOPE_NO_POTGEB_2020
- app:KARTE3_HW_RISK_FLUVIAL_LOW_2020
- app:KARTE3_UESG_2020
- app:KARTE3_BUEK250_KLIMASENS_BOED_2020
- app:KARTE3_ROHSTOFFKULISSEN_ZSM_2020
- app:KARTE3_WALD_BASISDLM_AAA_2020

```sh
python3 wfs_downloader.py --prefix sh --version 2.0.0 --service WFS --format 'application/gml+xml; version=3.2' --from_crs EPSG:25832 --to_crs EPSG:4326 --url https://umweltgeodienste.schleswig-holstein.de/WFS_LRP_Karte3_2020
```