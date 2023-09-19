import streamlit as st
import pandas as pd
import yfinance as yf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import io

def main():

    st.markdown("<h1 style='text-align: center; color: #335575;'>Quantitative Approach for Stocks & Portfolio Analysis</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #335575;'>☄️<a href='https://twitter.com/RayanArab7' target='_blank'>Rayan Arab</a></p>", unsafe_allow_html=True)


    # User input for stock ticker and start date
    stocks = st.text_input('Enter Stock Tickers (comma-separated):', value='2222.SR,SPUS,TSLA,AMC').upper()
    start_date = st.date_input('Enter Starting Date', pd.to_datetime('2022-12-30'))
 
    # Check if tickers are valid
    tickers = stocks.split(',')
    invalid_tickers = []
    for ticker in tickers:
        try:
            data = yf.download(stocks,start=start_date)['Adj Close'].reset_index()  
        except:
            invalid_tickers.append(ticker)

    if invalid_tickers:
        st.error(f"***The following tickers cannot be found: {', '.join(invalid_tickers)}***")
 
    # Analysis
    else:
        if st.button("Analyze"):
            #Calling Historical Data
            historical = data.copy()
            historical['Date'] = historical['Date'].dt.strftime('%Y/%m/%d')
            historical = historical.set_index("Date")
            historical = historical.dropna()
            # Convert DataFrame to Excel and let the user download it
            towrite = io.BytesIO()
            historical.to_excel(towrite, index=True, engine='openpyxl')
            towrite.seek(0)  
            st.markdown("<p style='color: #335575;'>Guess what, smarty? 🌟 Here's the data just for you!↙️</p>", unsafe_allow_html=True)
            st.download_button(
            label="Download the historical adj closing price",
            data=towrite,
            file_name=stocks+"-historical_data.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
            daily_returns = historical.pct_change().dropna()
            st.write(historical)

            #------------------------------------------------------------------------------------
            # Buy and Hold Backtesting for each ticker
            st.markdown("<h2 style='text-align: left; color: #5C7791;'>Historical Buy & Hold Back-Testing</h1>", unsafe_allow_html=True)
            st.markdown("<p style='color: #335575;'>Let's play pretend! If you started with <b>$1000</b>💸 and picked these tickers, here's how your money would've grown for each ticker 🌱📈</p>", unsafe_allow_html=True)
            value = 1000
            historical_line = historical.pct_change().dropna()
            historical_line.iloc[0, :] = 1 * value - 1
            historical_line = (historical_line + 1).cumprod()
            st.line_chart(historical_line, use_container_width=True)

            #------------------------------------------------------------------------------------
            # Seperate Line
            st.markdown("<hr style='border:4px solid lightgrey'>", unsafe_allow_html=True)
            #------------------------------------------------------------------------------------
            # Statistical analysis for each ticker
            st.markdown("<h2 style='text-align: left; color: #5C7791;'>Statistical Analysis</h1>", unsafe_allow_html=True)

            trading_days = 252
            today_mp = np.round(historical_line.iloc[-1],2)
            hp_return = np.round((historical_line.iloc[-1]/historical_line.iloc[0]-1)*100,2)
            arithmetic_mean = np.round(daily_returns.mean()*trading_days*100,4)
            geometric_mean = np.round((((np.prod(1 + daily_returns))**(trading_days/len(daily_returns))) - 1)*100,4)
            standard_deviation = np.round(daily_returns.std()* np.sqrt(trading_days)*100,4)

            metrics = pd.concat([today_mp,hp_return,arithmetic_mean,geometric_mean,standard_deviation],axis=1)
            metrics.columns = ["Today Value","Holding Return %",'Arithmetic Mean %', 'Geometric Mean %', 'Standard Deviation %']

            st.write(metrics)
            with st.expander("👨‍🏫Expalin the table for me plz💤"):
                 st.markdown("""
                <style>
                .custom-text {
                    color: #335575;
                }st
                </style>
                <div class="custom-text">
                    <b>Today's Value:</b> It's like checking your land value when you want to sell it. Did the price increase or decrease? 🛩️🪂<br>
                    <b>Holding Return:</b> It’s about tracking the growth (or dip) of your money over time. Think of it as monitoring your GPA. 📊📈<br>
                    <b>Annualized Arithmetic Mean:</b> This is the average daily growth rate of your investment. Imagine tracking your daily study hours, then finding the average. 📚⏰<br>
                    <b>Annualized Geometric Mean:</b> If you were to spread out your investment's growth consistently across the year, this tells you its pace. Kinda like evenly spacing out your study sessions before finals. 📅📝<br>
                    <b>Annualized Standard Deviation:</b> Investments can be unpredictable. This tells you how wild or calm the ride was. 🎢📉
                </div>
                """, unsafe_allow_html=True)

            #-----------------------------------------------------------------------------------------------
            # Seperate Line
            st.markdown("<hr style='border:4px solid lightgrey'>", unsafe_allow_html=True)
            #-----------------------------------------------------------------------------------------------
            # Technical Analysis
            st.markdown("<h2 style='text-align: left; color: #5C7791;'>Technical Analysis</h1>", unsafe_allow_html=True)
            def compute_rsi(data, window=14):
                delta = data.diff()
                up, down = delta.clip(lower=0), -1*delta.clip(upper=0)
                ema_up = up.ewm(com=window, adjust=False).mean()
                ema_down = down.ewm(com=window, adjust=False).mean()
                rs = ema_up/ema_down
                rsi = 100 - (100 / (1 + rs))
                
                # Extracting the latest RSI value
                latest_rsi = np.round(rsi.tail(1),2)
                
                # Generating a signal based on the RSI value
                signals = []
                for value in latest_rsi:
                    if value > 70:
                        signals.append('Overbought')
                    elif value < 30:
                        signals.append('Oversold')
                    else:
                        signals.append('Neutral')

                latest_rsi['RSI Signal'] = signals
                latest_rsi.index = ['RSI Number','RSI Signal']
                return latest_rsi
            historical_rsi = historical.apply(compute_rsi)
            st.write(historical_rsi)
            #-----------------------------------------------------------------------------------------------
            # Seperate Line
            st.markdown("<hr style='border:4px solid lightgrey'>", unsafe_allow_html=True)
            #-----------------------------------------------------------------------------------------------
            # Correlation explanations and take away
            st.markdown("<h2 style='text-align: left; color: #5C7791;'>Stocks Correlation</h1>", unsafe_allow_html=True)

            corr = daily_returns.corr()
            fig, ax = plt.subplots(figsize=(10, 7))
            from matplotlib.colors import LinearSegmentedColormap
            colors = ["#335575", "#BDC7D2"]
            cmap_custom = LinearSegmentedColormap.from_list("blue_to_navy", colors)
            sns.heatmap(corr, annot=True, cmap=cmap_custom, vmin=-1, vmax=1, ax=ax, annot_kws={"size": 12}) 
            st.pyplot(fig)
            with st.expander("👨‍🏫Expalin Correlation for me plz💤"):
                st.markdown("""
                <div style="color: #335575;">

                🌙 **Stock Correlation: A Tale of Two Camels in the Desert!** 🐪🐪

                Let's embark on a desert journey with two camels. How these camels tread the sands is a lot like how stocks behave in the market:

                - **Positive Correlation:** Our two camels walk step-by-step, in perfect sync. If one speeds up, the other does too; if one takes a break, the other rests beside it. This is just like two stocks that tend to go up or down together. If one stock is having a good day, chances are the other is too! 🐪🐪

                - **Negative Correlation:** Imagine one camel decides to rest under a palm tree while the other feels adventurous and wanders off. They're doing the complete opposite of each other! Similarly, when one stock rises, the other tends to fall. It's like they're playing a seesaw game in the market. 🐪🌴

                - **Zero Correlation:** Here, our camels have a mind of their own. One might be grazing while the other is strolling. They're independent and don't really affect each other's path. In the stock world, this means the movement of one stock doesn't give us any clue about the movement of the other.

                </div>
                """, unsafe_allow_html=True)
            for i in range(corr.shape[0]):
                for j in range(i+1, corr.shape[1]):
                    value = corr.iloc[i, j]
                    stock1 = corr.index[i]
                    stock2 = corr.columns[j]
                    if value > 0.5:
                        st.markdown(f"📈 {stock1} and {stock2} have a **high positive correlation** of {value:.2f}. They tend to move in the same direction.")
                    elif value < -0.5:
                        st.markdown(f"📉 {stock1} and {stock2} have a **high negative correlation** of {value:.2f}. They tend to move in opposite directions, which can be great for diversification.")
            # Seperate Line
            st.markdown("<hr style='border:4px solid lightgrey'>", unsafe_allow_html=True)
        #-----------------------------------------------------------------------------------------------
if __name__ == '__main__':
    main()