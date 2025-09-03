# Portfolio-Optimisation

This folder contains different files that all compare different apsect of portfolio optimization. 

- cac40_download.py is just downloads the closure price of all the stocks in the CAC40 (the top 40 french firms with biggest capitalisation) from yahoo finance starting from January 1st 2022 to July 1st 2025. Then it saves them in cac40.csv

- constraint_comparison.ipynb aims to compare different constraints in portfolio optimisaion, based on their performances: allocation diversity, return, Sharpe ratio, maximum drawdown, VaR and CVaR at 95%. We will focus on the long-only, L/S and leverage constaints with a simple MV optimisation problem. Secondly we add a risk aversion parameter to the Markowitz problem simuation. We find the best value of it over the data from Jan. 2022 to Dec. 2024 and we analyse the performances of the cumputed allocation over the first semester of 2025.

- objective_comparison.ipynb aims to compare different objectives in portfolio optimisaion, based on their performances: allocation diversity, return, Sharpe ratio, maximum drawdown, VaR and CVaR at 95%. We will first focus on minimizing the risk, captured by Mean-Variance, MAD and CVaR, everything under a minimum retrun constraint. Secondly, we maximize the Sharpe ratio, still under the same minimum return constraint.
