import streamlit as st
import pandas as pd

def weighted_tranches_3(buy_price, percentage_increase, capital):
    # Tranche allocations
    first_tranche_alloc = 0.025
    second_tranche_alloc = 0.015
    third_tranche_alloc = 0.01

    # Capital Allocation
    first_tranche_capital = capital * first_tranche_alloc
    second_tranche_capital = capital * second_tranche_alloc
    third_tranche_capital = capital * third_tranche_alloc

    # Calculations for the first tranche
    first_tranch_avg_cost = buy_price
    first_tranch_curr_price = buy_price * (1 + percentage_increase / 100)

    # Calculations for the second tranche
    second_tranch_buy_price = first_tranch_curr_price
    second_tranch_curr_price = second_tranch_buy_price * (1 + percentage_increase / 100)
    second_tranch_avg_cost = (2.5 * first_tranch_avg_cost + 1.5 * second_tranch_buy_price) / 4

    # Calculations for the third tranche
    third_tranch_buy_price = second_tranch_curr_price
    third_tranch_curr_price = third_tranch_buy_price * (1 + percentage_increase / 100)
    third_tranch_avg_cost = (2.5 * buy_price + 1.5 * second_tranch_buy_price + 1 * third_tranch_buy_price) / 5

    # Profit calculations
    first_tranche_profit = third_tranch_curr_price - first_tranch_avg_cost
    second_tranche_profit = third_tranch_curr_price - second_tranch_avg_cost
    third_tranche_profit = third_tranch_curr_price - third_tranch_avg_cost

    # Qty to be added
    ft_qty_to_be_bought = round(first_tranche_capital / buy_price, 0)
    sc_qty_to_be_bought = round(second_tranche_capital / second_tranch_buy_price, 0)
    tc_qty_to_be_bought = round(third_tranche_capital / third_tranch_buy_price, 0)

    # Total profit and percentage calculations
    total_profit = first_tranche_profit + second_tranche_profit + third_tranche_profit
    total_move = percentage_increase * 3
    total_investment = buy_price + second_tranch_buy_price + third_tranch_buy_price
    percentage_profit = (total_profit / total_investment) * 100

    # Creating the output DataFrame
    data = {
        'Tranche': ['1st tranche 2.5%', '2nd tranche 1.5%', '3rd tranche 1%'],
        'Avg cost': [first_tranch_avg_cost, second_tranch_avg_cost, third_tranch_avg_cost],
        'Buy Price': [buy_price, second_tranch_buy_price, third_tranch_buy_price],
        '% increase': [percentage_increase, percentage_increase, percentage_increase],
        'Current Price': [first_tranch_curr_price, second_tranch_curr_price, third_tranch_curr_price],
        'Profit': [first_tranche_profit, second_tranche_profit, third_tranche_profit],
        'Capital To be deployed': [first_tranche_capital, second_tranche_capital, third_tranche_capital],
        'Qty to be bought': [ft_qty_to_be_bought, sc_qty_to_be_bought, tc_qty_to_be_bought]
    }

    df = pd.DataFrame(data, index=[1, 2, 3])

    summary_data = {
        'Metric': ['Total Profit', 'Total % Move', '% Profit'],
        'Value': [total_profit, total_move, percentage_profit]
    }
    
    summary_df = pd.DataFrame(summary_data)
    return df, summary_df

def weighted_tranches_5(buy_price, percentage_increase, capital):
    # Tranche allocations
    tranche_alloc = 0.01

    # Capital Allocation
    first_tranche_capital = capital * tranche_alloc
    second_tranche_capital = capital * tranche_alloc
    third_tranche_capital = capital * tranche_alloc
    forth_tranche_capital = capital * tranche_alloc
    fifth_tranche_capital = capital * tranche_alloc

    # Calculations for the first tranche
    first_tranch_avg_cost = buy_price
    first_tranch_curr_price = buy_price * (1 + percentage_increase / 100)

    # Calculations for the second tranche
    second_tranch_buy_price = first_tranch_curr_price
    second_tranch_curr_price = second_tranch_buy_price * (1 + percentage_increase / 100)
    second_tranch_avg_cost = (first_tranch_avg_cost + second_tranch_buy_price) / 2

    # Calculations for the third tranche
    third_tranch_buy_price = second_tranch_curr_price
    third_tranch_curr_price = third_tranch_buy_price * (1 + percentage_increase / 100)
    third_tranch_avg_cost = (buy_price + second_tranch_buy_price + third_tranch_buy_price) / 3

    # Calculations for the forth tranche
    forth_tranch_buy_price = third_tranch_curr_price
    forth_tranch_curr_price = forth_tranch_buy_price * (1 + percentage_increase / 100)
    forth_tranch_avg_cost = (buy_price + second_tranch_buy_price + third_tranch_buy_price + forth_tranch_buy_price) / 4    

    # Calculations for the fifth tranche
    fifth_tranch_buy_price = forth_tranch_curr_price
    fifth_tranch_curr_price = fifth_tranch_buy_price * (1 + percentage_increase / 100)
    fifth_tranch_avg_cost = (buy_price + second_tranch_buy_price + third_tranch_buy_price + forth_tranch_buy_price + fifth_tranch_buy_price ) / 5
    
    # Profit calculations
    first_tranche_profit = fifth_tranch_curr_price - buy_price
    second_tranche_profit = fifth_tranch_curr_price - second_tranch_buy_price
    third_tranche_profit = fifth_tranch_curr_price - third_tranch_buy_price
    forth_tranche_profit = fifth_tranch_curr_price - forth_tranch_buy_price
    fifth_tranche_profit = fifth_tranch_curr_price - fifth_tranch_buy_price

    # Qty to be added
    ft_qty_to_be_bought = round(first_tranche_capital / buy_price, 0)
    sc_qty_to_be_bought = round(second_tranche_capital / second_tranch_buy_price, 0)
    tc_qty_to_be_bought = round(third_tranche_capital / third_tranch_buy_price, 0)
    fc_qty_to_be_bought = round(forth_tranche_capital / forth_tranch_buy_price, 0)
    ff_qty_to_be_bought = round(fifth_tranche_capital / fifth_tranch_buy_price, 0)

    # Total profit and percentage calculations
    total_profit = first_tranche_profit + second_tranche_profit + third_tranche_profit + forth_tranche_profit + fifth_tranche_profit
    total_move = percentage_increase * 5
    total_investment = buy_price + second_tranch_buy_price + third_tranch_buy_price + forth_tranch_buy_price + fifth_tranch_buy_price
    percentage_profit = (total_profit / total_investment) * 100

    # Creating the output DataFrame
    data = {
        'Tranche': ['1st tranche', '2nd tranche', '3rd tranche', '4th tranche', '5th tranche'],
        'Avg cost': [first_tranch_avg_cost, second_tranch_avg_cost, third_tranch_avg_cost, forth_tranch_avg_cost, fifth_tranch_avg_cost],
        'Buy Price': [buy_price, second_tranch_buy_price, third_tranch_buy_price, forth_tranch_buy_price, fifth_tranch_buy_price],
        '% increase': [percentage_increase, percentage_increase, percentage_increase, percentage_increase, percentage_increase],
        'Current Price': [first_tranch_curr_price, second_tranch_curr_price, third_tranch_curr_price, forth_tranch_curr_price, fifth_tranch_curr_price],
        'Profit': [first_tranche_profit, second_tranche_profit, third_tranche_profit, forth_tranche_profit, fifth_tranche_profit],
        'Capital To be deployed': [first_tranche_capital, second_tranche_capital, third_tranche_capital, forth_tranche_capital, fifth_tranche_capital],
        'Qty to be bought': [ft_qty_to_be_bought, sc_qty_to_be_bought, tc_qty_to_be_bought, fc_qty_to_be_bought, ff_qty_to_be_bought]
    }

    df = pd.DataFrame(data, index=[1, 2, 3, 4, 5])

    summary_data = {
        'Metric': ['Total Profit', 'Total % Move', '% Profit'],
        'Value': [total_profit, total_move, percentage_profit]
    }
    
    summary_df = pd.DataFrame(summary_data)
    return df, summary_df

# Streamlit app
st.title("Tranches Calculator")

st.sidebar.header("Input Parameters")
buy_price = st.sidebar.number_input("Buy Price", min_value=0.0, value=100.0)
percentage_increase = st.sidebar.number_input("Percentage Increase", min_value=0.0, value=5.0)
capital = st.sidebar.number_input("Initial Capital", min_value=0.0, value=1000000.0)

# Option to choose between 3 or 5 tranches
tranche_option = st.sidebar.selectbox("Choose Tranche Option", ("3 weighted tranches for pyramiding", "5 equal tranches"))

if st.sidebar.button("Calculate"):
    if tranche_option == "3 weighted tranches for pyramiding":
        tranche_df, summary_df = weighted_tranches_3(buy_price, percentage_increase, capital)
    else:
        tranche_df, summary_df = weighted_tranches_5(buy_price, percentage_increase, capital)
    
    st.write("### Tranche Details")
    st.dataframe(tranche_df.reset_index(drop=True))  # Reset the index and drop the old one
    
    st.write("### Summary")
    st.dataframe(summary_df.reset_index(drop=True))  # Reset the index and drop the old one
