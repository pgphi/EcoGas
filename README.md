___

Author: Philipp Ganster

Link to Project: https://gasspeicher-deutschland.herokuapp.com/

___

# About this Project

    Due to a spike in german gas prices, the aim of this project is
    to raise awareness in regard to gas consumption of Germany, by 
    showing an overview of all german gas providers and their:
    
    - Storage in TWh
    - Capacity Full in %
    - Daily Change in Demand in %
    - Daily Change in Demain in GWh

    Advanced Python Schedular is used for running script 
    every day at 8pm, since API Data is refreshed every day at 7:30pm (MESZ)
    https://apscheduler.readthedocs.io/en/3.x/

    


### Further information

- Streamlit Documentation: https://docs.streamlit.io/library/api-reference
- API Data: https://agsi.gie.eu/

### About the Development Process (Pipeline for this Project)

    1. Develop App locally with Pycharm CE
    2. Use Streamlit (streamlit run main.py) for Agile Testing
    3. Commit and Push Project to GitHub Repository
    4. Deploy Repository on GitHub to Heroku
    5. Use GitHub Desktop for continuous Development
 
 ### Information about the Model for Price Prediction
    Polynomial Function MAE = 0.008515221391126407
    Polynomial Function R Squared = 0.6370797480659653
    
$\tiny f(x_1 , x_2) = 5.02 - (6.69 {e-09}) * x_1 + (1.25 {e-09}) * x_2 + (2.24 {e-18}) * x_1^2 - (7.83 {e-19}) * x_2^2 - (3.19 {e-19}) *x_1 * x_2$
