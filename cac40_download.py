import yfinance as yf

cac40_tickers = [
    "^FCHI",     # CAC40 index
    "ACA.PA",   # Crédit Agricole
    "AC.PA",    # Accor
    "AIR.PA",   # Airbus
    "AI.PA",    # Air Liquide
    "BNP.PA",   # BNP Paribas
    "BN.PA",    # Danone
    "BVI.PA",   # Bureau Veritas
    "CAP.PA",   # Capgemini
    "CA.PA",    # Carrefour
    "CS.PA",    # Axa
    "DG.PA",    # Vinci
    "DSY.PA",   # Dassault Systèmes
    "EDEN.PA",  # Edenred
    "EL.PA",    # EssilorLuxottica
    "ENGI.PA",  # Engie
    "EN.PA",    # Bouygues
    "ERF.PA",   # Eurofins Scientific
    "GLE.PA",   # Société Générale
    "KER.PA",   # Kering
    "LR.PA",    # Legrand
    "MC.PA",    # LVMH
    "ML.PA",    # Michelin
    "MT.AS",    # ArcelorMittal
    "ORA.PA",   # Orange
    "OR.PA",    # L'Oreal
    "PUB.PA",   # Publicis Groupe
    "RMS.PA",   # Hermès
    "RNO.PA",   # Renault
    "RI.PA",    # Pernod Ricard
    "SAN.PA",   # Sanofi
    "SAF.PA",   # Safran
    "SGO.PA",   # Saint-Gobain
    "SU.PA",    # Schneider Electric
    "STMPA.PA", # STMicroelectronics
    "STLAP.PA", # Stellantis
    "TEP.PA",   # Teleperformance
    "TTE.PA",   # TotalEnergies
    "HO.PA",    # Thales
    "URW.PA",   # Unibail-Rodamco-Westfield
    "VIE.PA",   # Veolia
]

cac40 = yf.download(cac40_tickers, start="2022-01-01", end="2025-07-01", auto_adjust=True,progress=False)
cac40_prices = cac40["Close"]
cac40_prices.to_csv("cac40.csv")