def make_prediction(date, number, error):
    """

    :param date: date ('%Y/%m/%d') (str)
    :param number: kWh consumption (int or float)
    :param error: mean absolute error of price in euro/kWh
    :return: gas_costs in Euro based on kWh consumption i.E. 10000 Euros for 10000kWh
    """

    try:
        x1 = int(date.strftime("%s"))
        x2 = int(number) / 1000000000  # convert kWh to TWh
        y_pred = 5.014586015417417 + -6.691310239483297e-09 * x1 + 1.2486026421482226e-09 * x2 \
                 + 2.2363262130192694e-18 * x1 ** 2 + -7.831611461243813e-19 * x2 ** 2 \
                 + -3.191085831814934e-19 * x1 * x2
        x2 = x2 * 1000000000  # convert kWh to TWh for making suitable predictions for kWh
        gas_costs = round(y_pred * x2, 2)  # gas_costs in Euro = EUR/kWh * kWh
        cost_variance = round(x2 * error, 2)  # gas consumption in kWh * mae of model

    # Input is case sensitive
    except ValueError:
        print("Did you write the date right? For Example 01.01.2020 no '-' or shortcuts for the Year" + "\n" +
              "Please input whole numbers for your gas consumption i.e. 15000, 23543 etc. without points or comas"
              + "\n" + "Please right 'yes' or 'no'")

    return [gas_costs, cost_variance]


def mc_simulation():
    None
