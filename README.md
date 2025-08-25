# Portfolio-Optimisation

This folder contains different files that all compare different apsect of portfolio optimization. 

- cac40_download.py is just downloads the closure price of all the stocks in the CAC40 (the top 40 french firms with biggest capitalisation) from yahoo finance starting from January 1st 2022 to July 1st 2025. Then it saves them in cac40.csv

- MV_constraints.ipynb aims to compare different (basic) constraints in portfolio optimisaion, based on their performances: allocation diversity, return, Sharpe ratio. We will focus on the long-only, L/S and leverage constaints with a simple MV optimisation problem. Secondly we add a risk aversion parameter to the Markowitz problem simuation. We find the best value of it over the first semester of 2025.
