{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction\n",
    "\n",
    "In this project, you will act as a data visualization developer at Yahoo Finance! You will be helping the \"Netflix Stock Profile\" team visualize the Netflix stock data. In finance, a _stock profile_ is a series of studies, visualizations, and analyses that dive into different aspects a publicly traded company's data. \n",
    "\n",
    "For the purposes of the project, you will only visualize data for the year of 2017. Specifically, you will be in charge of creating the following visualizations:\n",
    "+ The distribution of the stock prices for the past year\n",
    "+ Netflix's earnings and revenue in the last four quarters\n",
    "+ The actual vs. estimated earnings per share for the four quarters in 2017\n",
    "+ A comparison of the Netflix Stock price vs the Dow Jones Industrial Average price in 2017 \n",
    "\n",
    "Note: We are using the Dow Jones Industrial Average to compare the Netflix stock to the larter stock market. Learn more about why the Dow Jones Industrial Average is a general reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp).\n",
    "\n",
    "During this project, you will analyze, prepare, and plot data. Your visualizations will help the financial analysts asses the risk of the Netflix stock.\n",
    "\n",
    "After you complete your visualizations, you'll be creating a presentation to share the images with the rest of the Netflix Stock Profile team. Your slides should include:\n",
    "\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n",
    "\n",
    "Financial Data Source: [Yahoo Finance](https://finance.yahoo.com/quote/DATA/)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 1\n",
    "\n",
    "Let's get our notebook ready for visualizing! Import the modules that you'll be using in this project:\n",
    "- `from matplotlib import pyplot as plt`\n",
    "- `import pandas as pd`\n",
    "- `import seaborn as sns`"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "%matplotlib inline\n",
    "from matplotlib import pyplot as plt\n",
    "import pandas as pd\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 2"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's load the datasets and inspect them."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX.csv** into a DataFrame called `netflix_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Hint: Use the `pd.read_csv()`function).\n",
    "\n",
    "Note: In the Yahoo Data, `Adj Close` represents the adjusted close price adjusted for both dividends and splits. This means this is the true closing stock price for a given business day."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close   Adj Close  \\\n",
      "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "\n",
      "      Volume  \n",
      "0  181772200  \n",
      "1   91432000  \n",
      "2  110692700  \n",
      "3  149769200  \n",
      "4  116795800  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks = pd.read_csv('nflx.csv')\n",
    "print(netflix_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **DJI.csv** into a DataFrame called `dowjones_stocks`. Then, quickly inspect the DataFrame using `print()`.\n",
    "\n",
    "Note: You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date          Open          High           Low         Close  \\\n",
      "0  2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1  2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2  2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3  2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4  2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "\n",
      "      Adj Close      Volume  \n",
      "0  19864.089844  6482450000  \n",
      "1  20812.240234  6185580000  \n",
      "2  20663.220703  6941970000  \n",
      "3  20940.509766  5392630000  \n",
      "4  21008.650391  6613570000  \n"
     ]
    }
   ],
   "source": [
    "dowjones_stocks = pd.read_csv('dji.csv')\n",
    "print(dowjones_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Load **NFLX_daily_by_quarter.csv** into a DataFrame called `netflix_stocks_quarterly`. Then, quickly inspect the DataFrame using `print()`.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close   Adj Close  \\\n",
      "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "\n",
      "     Volume Quarter  \n",
      "0   9437900      Q1  \n",
      "1   7843600      Q1  \n",
      "2  10185500      Q1  \n",
      "3  10657900      Q1  \n",
      "4   5766900      Q1  \n"
     ]
    }
   ],
   "source": [
    "netflix_stocks_quarterly = pd.read_csv('nflx_daily_by_quarter.csv')\n",
    "print(netflix_stocks_quarterly.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Let's learn more about our data. The datasets are large and it may be easier to view the entire dataset locally on your computer. Open the CSV files directly from the folder you downloaded for this project.\n",
    " - `NFLX` is the stock ticker symbol for Netflix and `^DJI` is the stock ticker symbol for the Dow Jones industrial Average, which is why the CSV files are named accordingly\n",
    " - In the Yahoo Data, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    " - You can learn more about why the Dow Jones Industrial Average is a industry reflection of the larger stock market [here](https://www.investopedia.com/terms/d/djia.asp). \n",
    " \n",
    "Answer the following questions by inspecting the data in the **NFLX.csv**,**DJI.csv**, and **NFLX_daily_by_quarter.csv** in your computer."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What year is represented in the data? 2017-01-01 and 2017-12-01"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017-01-01\n",
      "2017-12-01\n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks['Date'].min())\n",
    "print(netflix_stocks['Date'].max())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "+ Is the data represented by days, weeks, or months? Months \n",
    "+ In which ways are the files different? \n",
    "+ What's different about the columns for `netflix_stocks` versus `netflix_stocks_quarterly`?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          Date        Open        High         Low       Close   Adj Close  \\\n",
      "0   2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1   2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2   2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3   2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4   2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "5   2017-06-01  163.520004  166.869995  147.300003  149.410004  149.410004   \n",
      "6   2017-07-01  149.800003  191.500000  144.250000  181.660004  181.660004   \n",
      "7   2017-08-01  182.490005  184.619995  164.229996  174.710007  174.710007   \n",
      "8   2017-09-01  175.550003  189.949997  172.440002  181.350006  181.350006   \n",
      "9   2017-10-01  182.110001  204.380005  176.580002  196.429993  196.429993   \n",
      "10  2017-11-01  197.240005  202.479996  184.320007  195.509995  195.509995   \n",
      "11  2017-12-01  186.990005  194.490005  178.380005  191.960007  191.960007   \n",
      "\n",
      "       Volume  \n",
      "0   181772200  \n",
      "1    91432000  \n",
      "2   110692700  \n",
      "3   149769200  \n",
      "4   116795800  \n",
      "5   135675800  \n",
      "6   185144700  \n",
      "7   136523100  \n",
      "8   111427900  \n",
      "9   208657800  \n",
      "10  161719700  \n",
      "11  115103700  \n",
      "           Date        Open        High         Low       Close   Adj Close  \\\n",
      "0    2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1    2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2    2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3    2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4    2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "..          ...         ...         ...         ...         ...         ...   \n",
      "246  2017-12-22  188.330002  190.949997  186.800003  189.940002  189.940002   \n",
      "247  2017-12-26  189.779999  189.940002  186.399994  187.759995  187.759995   \n",
      "248  2017-12-27  187.800003  188.100006  185.220001  186.240005  186.240005   \n",
      "249  2017-12-28  187.179993  194.490005  186.850006  192.710007  192.710007   \n",
      "250  2017-12-29  192.509995  193.949997  191.220001  191.960007  191.960007   \n",
      "\n",
      "       Volume Quarter  \n",
      "0     9437900      Q1  \n",
      "1     7843600      Q1  \n",
      "2    10185500      Q1  \n",
      "3    10657900      Q1  \n",
      "4     5766900      Q1  \n",
      "..        ...     ...  \n",
      "246   3878900      Q4  \n",
      "247   3045700      Q4  \n",
      "248   4002100      Q4  \n",
      "249  10107400      Q4  \n",
      "250   5187600      Q4  \n",
      "\n",
      "[251 rows x 8 columns]\n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks) # represented by months\n",
    "print(netflix_stocks_quarterly) # represented by days"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 4\n",
    "\n",
    "Great! Now that we have spent sometime looking at the data, let's look at the column names of the DataFrame `netflix_stocks` using `.head()`. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close   Adj Close  \\\n",
      "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "\n",
      "      Volume  \n",
      "0  181772200  \n",
      "1   91432000  \n",
      "2  110692700  \n",
      "3  149769200  \n",
      "4  116795800  \n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What do you notice? The first two column names are one word each, and the only one that is not is `Adj Close`! \n",
    "\n",
    "The term `Adj Close` is a confusing term if you don't read the Yahoo Documentation. In Yahoo, `Adj Close` is documented as adjusted close price adjusted for both dividends and splits.\n",
    "\n",
    "This means this is the column with the true closing price, so these data are very important.\n",
    "\n",
    "Use Pandas to change the name of of the column to `Adj Close` to `Price` so that it is easier to work with the data. Remember to use `inplace=True`.\n",
    "\n",
    "Do this for the Dow Jones and Netflix Quarterly pandas dataframes as well.\n",
    "Hint: Use [`.rename()`](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rename.html)).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "netflix_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)\n",
    "netflix_stocks_quarterly.rename(columns={'Adj Close': 'Price'}, inplace=True)\n",
    "dowjones_stocks.rename(columns={'Adj Close': 'Price'}, inplace=True)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Run `netflix_stocks.head()` again to check your column name has changed."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date        Open        High         Low       Close       Price  \\\n",
      "0  2017-01-01  124.959999  143.460007  124.309998  140.710007  140.710007   \n",
      "1  2017-02-01  141.199997  145.949997  139.050003  142.130005  142.130005   \n",
      "2  2017-03-01  142.839996  148.289993  138.259995  147.809998  147.809998   \n",
      "3  2017-04-01  146.699997  153.520004  138.660004  152.199997  152.199997   \n",
      "4  2017-05-01  151.910004  164.750000  151.610001  163.070007  163.070007   \n",
      "\n",
      "      Volume  \n",
      "0  181772200  \n",
      "1   91432000  \n",
      "2  110692700  \n",
      "3  149769200  \n",
      "4  116795800  \n"
     ]
    }
   ],
   "source": [
    "print(netflix_stocks.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Call `.head()` on the DataFrame `dowjones_stocks` and `netflix_stocks_quarterly`."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Date          Open          High           Low         Close  \\\n",
      "0  2017-01-01  19872.859375  20125.580078  19677.939453  19864.089844   \n",
      "1  2017-02-01  19923.810547  20851.330078  19831.089844  20812.240234   \n",
      "2  2017-03-01  20957.289063  21169.109375  20412.800781  20663.220703   \n",
      "3  2017-04-01  20665.169922  21070.900391  20379.550781  20940.509766   \n",
      "4  2017-05-01  20962.730469  21112.320313  20553.449219  21008.650391   \n",
      "\n",
      "          Price      Volume  \n",
      "0  19864.089844  6482450000  \n",
      "1  20812.240234  6185580000  \n",
      "2  20663.220703  6941970000  \n",
      "3  20940.509766  5392630000  \n",
      "4  21008.650391  6613570000  \n",
      "         Date        Open        High         Low       Close       Price  \\\n",
      "0  2017-01-03  124.959999  128.190002  124.309998  127.489998  127.489998   \n",
      "1  2017-01-04  127.489998  130.169998  126.550003  129.410004  129.410004   \n",
      "2  2017-01-05  129.220001  132.750000  128.899994  131.809998  131.809998   \n",
      "3  2017-01-06  132.080002  133.880005  129.809998  131.070007  131.070007   \n",
      "4  2017-01-09  131.479996  131.990005  129.889999  130.949997  130.949997   \n",
      "\n",
      "     Volume Quarter  \n",
      "0   9437900      Q1  \n",
      "1   7843600      Q1  \n",
      "2  10185500      Q1  \n",
      "3  10657900      Q1  \n",
      "4   5766900      Q1  \n"
     ]
    }
   ],
   "source": [
    "print(dowjones_stocks.head())\n",
    "print(netflix_stocks_quarterly.head())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 5\n",
    "\n",
    "In this step, we will be visualizing the Netflix quarterly data! \n",
    "\n",
    "We want to get an understanding of the distribution of the Netflix quarterly stock prices for 2017. Specifically, we want to see in which quarter stock prices flucutated the most. We can accomplish this using a violin plot with four violins, one for each business quarter!\n",
    "\n",
    "\n",
    "1. Start by creating a variable `ax` and setting it equal to `sns.violinplot()`. This will instantiate a figure and give us access to the axes through the variable name `ax`.\n",
    "2. Use `sns.violinplot()` and pass in the following arguments:\n",
    "+ The `Quarter` column as the `x` values\n",
    "+ The `Price` column as your `y` values\n",
    "+ The `netflix_stocks_quarterly` dataframe as your `data`\n",
    "3. Improve the readability of the chart by adding a title of the plot. Add `\"Distribution of 2017 Netflix Stock Prices by Quarter\"` by using `ax.set_title()`\n",
    "4. Change your `ylabel` to \"Closing Stock Price\"\n",
    "5. Change your `xlabel` to \"Business Quarters in 2017\"\n",
    "6. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "202.679993\n",
      "127.489998\n"
     ]
    }
   ],
   "source": [
    "f = plt.figure(figsize=(10, 5))\n",
    "ax = sns.violinplot(data=netflix_stocks_quarterly, x='Quarter', y='Price')\n",
    "ax.set_title('Distribution of 2017 Stock Prices by Quarter')\n",
    "plt.xlabel('Closing Stock Price')\n",
    "plt.ylabel('Business Quarters in 2017')\n",
    "plt.savefig('distribution_prices.png')\n",
    "plt.show()\n",
    "print(netflix_stocks_quarterly['Price'].max())\n",
    "print(netflix_stocks_quarterly['Price'].min())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "- What are your first impressions looking at the visualized data?  \n",
    "        The data clearly shows signs of growth where.\n",
    "- In what range(s) did most of the prices fall throughout the year?  \n",
    "        The range where the prices fall on throughout the year is from 128-203\n",
    "- What were the highest and lowest prices?  \n",
    "        The highest price was 202.67993\n",
    "        The lowest price was 127.489998"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 6\n",
    "\n",
    "Next, we will chart the performance of the earnings per share (EPS) by graphing the estimate Yahoo projected for the Quarter compared to the actual earnings for that quarters. We will accomplish this using a scatter chart. \n",
    "\n",
    "1. Plot the actual EPS by using `x_positions` and `earnings_actual` with the `plt.scatter()` function. Assign `red` as the color.\n",
    "2. Plot the actual EPS by using `x_positions` and `earnings_estimate` with the `plt.scatter()` function. Assign `blue` as the color\n",
    "\n",
    "3. Often, estimates and actual EPS are the same. To account for this, be sure to set your transparency  `alpha=0.5` to allow for visibility pf overlapping datapoint.\n",
    "4. Add a legend by using `plt.legend()` and passing in a list with two strings `[\"Actual\", \"Estimate\"]`\n",
    "\n",
    "5. Change the `x_ticks` label to reflect each quarter by using `plt.xticks(x_positions, chart_labels)`\n",
    "6. Assing \"`\"Earnings Per Share in Cents\"` as the title of your plot.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmcAAAFNCAYAAABFbcjcAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4yLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy+j8jraAAAgAElEQVR4nO3de5hddX33/fc3BwhCEsJRmmFMPKCCjIGOWCpqUZGgGGSghZYWeRC5uG28tTYooBeifWwpRqUUeHJTpHLfCOhNJ4haBeUgFlSYQDoFghBOYRKFECYDEVII+T5/rJVkzzCT7Elmz6zMvF/Xta6912+t9dvfvfeC+eS3DjsyE0mSJFXDuJEuQJIkSZsYziRJkirEcCZJklQhhjNJkqQKMZxJkiRViOFMkiSpQgxn0nYsIs6JiMtHuo7hEBFrIuL1I11HlUTE4xHxgRF67R9HxMdG4rWl0c5wJg2x8g/mi2WY2DBd3IjXysy/z8zTGtH3UIiIb0fES30+i/+sY7vbIqLX+8rMXTLz0QbUeEpE/Mc2bv9K+d6ei4jFEXH0ENW2Q0R8PSK6yv4fi4hvDkXf2yozj8rMK7d2+4j4i4joKN/Xb8uwd9i21hUR50XEVdvajzSSDGdSY3ykDBMbprmD7SAiJjSisBFwQZ/P4u0jXVAD/DIzdwF2Bb4FfC8idhtMBwN832cDrcAhwGTgcODebay1v9eOiBi2vwcR8VngQuDvgb2BZuBS4JjhqkGqMsOZNIwi4g0RcUtErIqIZyLiOxGxa83yxyPi8xHRCfw+It4YERkRH4uIZeU2X6hZf+MoQUTM2MK6O0XElRHRHRFLIuJzEdE1QJ0LImJ+n7bvl39UKWtcHhHPR8RvIuL9W/FZTIqIq8rPYnVE3B0Re0fEV4F3AxfXjjqW7+2N5fNvR8Sl5WjLmoi4IyJeGxEXlu/vwYg4qOa1zoqIR8p6H4iIY8v2twILgEPLflaX7TtGxPzyc3yq/Dx22tJ7ysz1wBXATsDrN9dPRPxJOSL2+Yj4HfCv/XT5DmBhZq7IwuOZ+b/7rDMrIjojoicivhsRk8r+p0XEDyNiZfmZ/DAimmo+k9si4qsRcQfwQlnvWyLipxHxbPm9/tlmvr+No5tRjj6W77W7HOE7aoDtpgJfAf46M9sz8/eZ+XJm/iAzzyzXGVfzna2KiI1hd3P7eUTMBs4BToiaUdqyvkfL7/+xiDhps1+kNMIMZ9LwCuAfgD8A3grsC5zXZ50/Bz5MMQqzrmw7DHgz8H7g3DJUDGSgdb8EzABeDxwB/OVm+ria4g9cQPGHHvggcG1EvBmYC7wjMycDRwKPb6avgXwMmErxGewOnAG8mJlfAH4BzN3CqOOfAV8E9gD+G/glcE85fx3wjZp1H6EIfFOBLwNXRcQ+mbmkfN1flq+1ISj/I7AfMAt4IzAdOHdLbyiK0a/TgDXAw3X081pgN+B1wOn9dPkr4LMR8cmIOHDD99HP5zAbmAm0AKeU7eMoAt/rKEamXgT6Hl7/q/J1JwMrgZ9SfPd7UeyHl0bEAVt636V3Ar+h+PwvAL41QL2HApOAhZvp638CHwXeS/HfSjdwSZ91XrWfZ+ZPKEbjvrthlDYidgYuAo4q99c/BhbX+Z6kkZGZTk5OQzhRBJU1wOqa6RMDrPtR4N4+255aMz8DSKCppu0u4MTy+XnAVXWu+yhwZM2y04CuAeoKYBnwnnL+E8At5fM3Ak8DHwAmbuGz+Dawts9ncWW57FTgTqCln+1uA07r05bAG2v6/ZeaZZ8CltTMHwis3kxdi4FjyuenAP/R573/HnhDTduhwGMD9HUKRYheDTxDEag+sKV+gD8BXgImbabO8cBfA3dQBNAVwMf67C9/WTN/AbBggL5mAd19PuOv1MyfAPyizzb/C/jSAP1t/I7Kz2BpzbLXlN/Xa/vZ7iTgd1vYb5YA76+Z3wd4GZjAIP6bKOd3Lr+b44CdBvvfs5PTSEyj5ZwWqWo+mpk/69sYEXtR/Cv+3RSjFeMoRgVqPdlPf7+ref4CsMtmXnugdf+gT9/9vQ4AmZkRcS3F6MntwF8AV5XLlkbEZyj+CB4QETcCn83MFQN0Nz8zv9hP+/+hGDW7NopDu1cBX8jMlzfz3mo9VfP8xX7mN35GEXEy8FmKP+yUy/YYoN89KcLFopqBn6AISgP5VWb2Opm9/K631M/KzFw7UKeZ+QrFiNEl5eHQU4ErIuKuLEb94NXf9x+Ur/8a4JsUo2rTyuWTI2J82S/03gdeB7xzw6Hd0gSK76keG+vIzBfK99zffroK2CMiJmTmun6Wb6hlYUSsr2l7heL8tFe9Hpv5byIzfx8RJwDzKEbz7gD+NjMf3NIbkkaKhzWl4fUPFP/qb8nMKRSHFvse+skGvfZvgaaa+X23sP41wPER8TqKQ1b/tmFBZl5dhpHXUdT7j4MtJovzjL6cmftTHGo6Gjh5w+LB9jeQsv5/oTgUu3sWhy7vY9Pn3ve1nqEIdwdk5q7lNDWLE/4Ho55+6n6fmfliZl5CEeb3r2OTv6U47PfOcl97T9leu7/Vvv6TwM9rat01i0OD/6PeGuv0S4rR1I9uZp0nKQ5D1tYyKTOX19H/qz7TzLwxM4+gGIF7kGJ/kCrLcCYNr8mUhzwjYjpw5jC+9veAs8sTxadThJUBZea9FOchXQ7cmJkbTpZ/c0S8LyJ2pPgj+yLFqMagRMTh5XlU44HnKA5bbejnKYpz44bCzhR/sFeWr/v/AG+rWf4U0BQRO8DGk/r/BfhmOfpFREyPiCMH86JD0U9EfKa8cGCniJgQxX3FJlPfFZuTKb6b1eXJ9F/awvo/BPaLiL+KiInl9I4tnN84aJnZQ3He3SUR8dGIeE35WkdFxAXlaguAr5bBmojYMyLqvZLzKWBGlFefRnGRyZzy3LP/pvjvb9D7qzScDGdSY/wget/ba8PJz18GDgZ6gB8B7cNY01eALuAx4GcUJ83/9xa2uYbi/Kmra9p2BM6nGBn6HcXJ4+dspo/P9fksninbX1vW8BzFOUY/pzx0CvwTxahdd0RcVOf761dmPgB8nWLE5imK89HuqFnlFuB+4Hc1tX0eWAr8KiKeo/i83rwVL7+t/bxY1v47is/7r4Hjsr77vV1IcdXohvPgfrK5lTPzeYqLPk6kOLftdxQjojsOot66ZOY3KA4zf5EiND9J8Y+F68tV/gm4AbgpIp4v639nnd3/3/JxVUTcQ/F37m8p3tOzFBcZfHII3obUMJHZqCMokqosIv4HxUnU7x3pWiRJmzhyJo0REbFPRLyrvIfUmylGEzZ3OwNJ0gjwak1p7NiB4tYIMyluLXAtxV3ZJUkV4mFNSZKkCvGwpiRJUoUYziRJkipkVJ1ztscee+SMGTNGugxJkqQtWrRo0TOZuWff9lEVzmbMmEFHR8dIlyFJkrRFEfFEf+0e1pQkSaoQw5kkSVKFGM4kSZIqxHAmSZJUIYYzSZKkCjGcSZIkVYjhTJIkqUJG1X3OJEmStlbndQ/RfvFyli2fQPP0dbTNnU7L8fsNex2OnEmSpDGv87qHmP+5p+leHTTts47u1cH8zz1N53UPDXsthjNJkjTmtV+8nGlT1jFtVxg3Lpi2K0ybso72i5cPey2GM0mSNOYtWz6BqVOyV9vUKcmy5cN/BpjhTJIkjXnN09fR81z0aut5Lmievm7YazGcSZKkMa9t7nS6n5tA92pYvz7pXg3dz02gbe70Ya/FcCZJksa8luP3Y94FezFt16TrtxOYtmsy74K9RuRqTW+lIUmSRBHQRiKM9eXImSRJUoU0NJxFxOyI+E1ELI2Iszaz3jsi4pWIOH6w20qSJI0mDTusGRHjgUuAI4Au4O6IuCEzH+hnvX8EbhzstsOqsxPa22HZMmhuhrY2aGkZsXIkSdLo1MiRs0OApZn5aGa+BFwLHNPPep8C/g14eiu2HR6dnTB/PnR3Q1NT8Th/ftEuSZI0hBoZzqYDT9bMd5VtG0XEdOBYYMFgtx1W7e0wbVoxjRu36Xl7+4iVJEmSRqdGhrPopy37zF8IfD4zX9mKbYsVI06PiI6I6Fi5cuVWlFmHZctg6tTebVOnFu2SJElDqJG30ugC9q2ZbwJW9FmnFbg2IgD2AD4UEevq3BaAzLwMuAygtbW13wC3zZqbi0OZ06ZtauvpKdolSZKGUCNHzu4G3hQRMyNiB+BE4IbaFTJzZmbOyMwZwHXAJzPz+nq2HVZtbUU46+6G9es3PW9rG7GSJEnS6NSwcJaZ64C5FFdhLgG+l5n3R8QZEXHG1mzbqFq3qKUF5s0rRs66uorHefO8WlOSJA25yGzMkcCR0Nramh0dHSNdhiRJ0hZFxKLMbO3b7i8ESJIkVYjhTJIkqUIMZ5IkSRViOJMkSaoQw5kkSVKFGM4kSZIqxHAmSZJUIYYzSZKkCjGcSZIkVYjhTJIkqUIMZ5IkSRViOJMkSaoQw5kkSVKFGM4kSZIqxHAmSZJUIYYzSZKkCjGcSZIkVYjhTJIkqUIMZ5IkSRViOJMkSaqQCSNdwPaisxPa22HZMmhuhrY2aGkZ6aokSdJo48hZHTo7Yf586O6Gpqbicf78ol2SJGkoGc7q0N4O06YV07hxm563t490ZZIkabQxnNVh2TKYOrV329SpRbskSdJQMpzVobkZenp6t/X0FO2SJElDyXBWh7a24jyz7m5Yv37T87a2ka5MkiSNNoazOrS0wLx5xXlmXV3F47x5Xq0pSZKGnrfSqFNLi2FMkiQ1niNnkiRJFWI4kyRJqhDDmSRJUoUYziRJkirEcCZJklQhhjNJkqQKMZxJkiRViOFMkiSpQgxnkiRJFWI4kyRJqhDDmSRJUoU0NJxFxOyI+E1ELI2Is/pZfkxEdEbE4ojoiIjDapY9HhH/tWFZI+uUJEmqiob98HlEjAcuAY4AuoC7I+KGzHygZrWbgRsyMyOiBfge8Jaa5Ydn5jONqlGSJKlqGjlydgiwNDMfzcyXgGuBY2pXyMw1mZnl7M5AIkmSNIY1MpxNB56sme8q23qJiGMj4kHgR8CpNYsSuCkiFkXE6QO9SEScXh4S7Vi5cuUQlS5JkjQyGhnOop+2V42MZebCzHwL8FHg72oWvSszDwaOAv46It7T34tk5mWZ2ZqZrXvuuedQ1C1JkjRiGhnOuoB9a+abgBUDrZyZtwNviIg9yvkV5ePTwEKKw6SSJEmjWiPD2d3AmyJiZkTsAJwI3FC7QkS8MSKifH4wsAOwKiJ2jojJZfvOwAeB+xpYqyRJUiU07GrNzFwXEXOBG4HxwBWZeX9EnFEuXwAcB5wcES8DLwInlFdu7g0sLHPbBODqzPxJo2qVJEmqith0seT2r7W1NTs6vCWaJEmqvohYlJmtfdv9hQBJkqQKMZxJkiRViOFMkiSpQgxnkiRJFWI4kyRJqhDDmSRJUoUYziRJkirEcCZJklQhhjNJkqQKMZxJkiRViOFMkiSpQgxnkiRJFWI4kyRJqhDDmSRJUoUYziRJkirEcCZJklQhhjNJkqQKMZxJkiRViOFMkiSpQgxnkiRJFTJhpAuQJI0NnZ3Q3g7LlkFzM7S1QUvLSFclVY8jZ5KkhuvshPnzobsbmpqKx/nzi3ZJvRnOJEkN194O06YV07hxm563t490ZVL1GM4kSQ23bBlMndq7berUol1Sb4YzSVLDNTdDT0/vtp6eol1Sb4YzSVLDtbUV55l1d8P69Zuet7WNdGVS9RjOJEkN19IC8+YV55l1dRWP8+Z5tabUH2+lIUkaFi0thjGpHo6cSZIkVYjhTJIkqUIMZ5IkSRViOJMkSaoQw5kkSVKFGM4kSZIqxHAmSZJUIYYzSZKkCjGcSZIkVYjhTJIkqUIaGs4iYnZE/CYilkbEWf0sPyYiOiNicUR0RMRh9W4rSZI0GjUsnEXEeOAS4Chgf+DPI2L/PqvdDLw9M2cBpwKXD2JbSZKkUaeRI2eHAEsz89HMfAm4FjimdoXMXJOZWc7uDGS920qSJI1GjQxn04Ena+a7yrZeIuLYiHgQ+BHF6Fnd20qSJI02jQxn0U9bvqohc2FmvgX4KPB3g9kWICJOL89X61i5cuVWFytJklQFjQxnXcC+NfNNwIqBVs7M24E3RMQeg9k2My/LzNbMbN1zzz23vWpJkqQR1MhwdjfwpoiYGRE7ACcCN9SuEBFvjIgonx8M7ACsqmdbSZKk0WhCozrOzHURMRe4ERgPXJGZ90fEGeXyBcBxwMkR8TLwInBCeYFAv9s2qlZJkqSqiE0XS27/Wltbs6OjY6TLkCRJ2qKIWJSZrX3b/YUASZKkCmnYYU1Jknrp7IT2dli2DJqboa0NWlpGuiqpcuoaOYuICyJiSkRMjIibI+KZiPjLRhcnSRolOjth/nzo7oampuJx/vyiXVIv9R7W/GBmPgccTXGbi/2AMxtWlSRpdGlvh2nTimncuE3P29tHujKpcuoNZxPLxw8B12Tmsw2qR5I0Gi1bBlOn9m6bOrVol9RLveHsB+VPLLUCN0fEnsDaxpUlSRpVmpuhp6d3W09P0S6pl3rD2ZeAQ4HWzHwZeAGY07CqJEmjS1tbcZ5ZdzesX7/peVvbSFcmVU694eyXmdmdma8AZObvgR83rixJ0qjS0gLz5hXnmXV1FY/z5nm1ptSPzd5KIyJeC0wHdoqIg9j0g+RTgNc0uDZJ0mjS0mIYk+qwpfucHQmcQvHD49+oaX8eOKdBNUmSJI1Zmw1nmXklcGVEHJeZ/zZMNUmSJI1Z9f5CwA8j4i+AGbXbZOZXGlGUJEnSWFVvOPs+0AMsAv67ceVIkiSNbfWGs6bMnN3QSiRJklT3rTTujIgDG1qJJEmS6h45Oww4JSIeozisGUBmptdES5IkDaF6w9lRDa1CkiRJQJ2HNTPzCWBf4H3l8xfq3VaSJEn1qytgRcSXgM8DZ5dNE4GrGlWUJEnSWFXv6NexFD90/nuAzFwBTG5UUZIkSWNVveHspcxMIAEiYufGlSRJkjR21RvOvhcR/wvYNSI+AfwM+JfGlSVJkjQ2bfZqzYh4I7B3Zs6PiCOA54A3Az8G/n0Y6pMkSRpTtnQrjQuBcwAy86fATwEiorVc9pGGVidJkjTGbOmw5ozM7OzbmJkdFD+CLkmSpCG0pXA2aTPLdhrKQiRJkrTlcHZ3eQFALxHxcWBRY0qSJEkau7Z0ztlngIURcRKbwlgrsAPFvc8kSZI0hDYbzjLzKeCPI+Jw4G1l848y85aGVyZJkjQG1fXD55l5K3Brg2uRJEka8/zxckmSpAoxnEmSJFWI4UySJKlCDGeSJEkVYjiTJEmqEMOZJElShRjOJEmSKsRwJkmSVCGGM0mSpAppaDiLiNkR8ZuIWBoRZ/Wz/KSI6CynOyPi7TXLHo+I/4qIxRHR0cg6JUmSqqKun2/aGhExHrgEOALoAu6OiBsy84Ga1R4D3puZ3RFxFHAZ8M6a5Ydn5jONqlGSJKlqGjlydgiwNDMfzcyXgGuBY2pXyMw7M7O7nP0V0NTAeiRJkiqvkeFsOvBkzXxX2TaQjwM/rplP4KaIWBQRpw+0UUScHhEdEdGxcuXKbSpYkiRppDXssCYQ/bRlvytGHE4Rzg6raX5XZq6IiL2An0bEg5l5+6s6zLyM4nAora2t/fYvSZK0vWjkyFkXsG/NfBOwou9KEdECXA4ck5mrNrRn5ory8WlgIcVhUkmSpFGtkeHsbuBNETEzInYATgRuqF0hIpqBduCvMvOhmvadI2LyhufAB4H7GlirJElSJTTssGZmrouIucCNwHjgisy8PyLOKJcvAM4FdgcujQiAdZnZCuwNLCzbJgBXZ+ZPGlWrJElSVUTm6DlNq7W1NTs6vCWaJEmqvohYVA5K9eIvBEiSJFWI4UySJKlCDGeSJEkVYjiTJEmqEMOZJElShRjOJEmSKsRwJkmSVCGGM0mSpAoxnEmSJFWI4UySJKlCDGeSJEkVYjiTJEmqEMOZJElShRjOJEmSKsRwJkmSVCGGM0mSpAoxnEmSJFWI4UySJKlCDGeSJEkVYjiTJEmqEMOZJElShRjOJEmSKsRwJkmSVCGGM0mSpAoxnEmSJFWI4UySJKlCDGeSJEkVYjiTJEmqEMOZJElShRjOJEmSKsRwJkmSVCGGM0mSpAoxnEmSJFWI4UySJKlCDGeSJEkVYjiTJEmqEMOZJElShRjOJEmSKqSh4SwiZkfEbyJiaUSc1c/ykyKis5zujIi317utJEnSaNSwcBYR44FLgKOA/YE/j4j9+6z2GPDezGwB/g64bBDbSpIkjTqNHDk7BFiamY9m5kvAtcAxtStk5p2Z2V3O/gpoqndbSZKk0aiR4Ww68GTNfFfZNpCPAz/eym0lSZJGhQkN7Dv6act+V4w4nCKcHbYV254OnA7Q3Nw8+ColSZIqpJEjZ13AvjXzTcCKvitFRAtwOXBMZq4azLYAmXlZZrZmZuuee+45JIVLkiSNlEaGs7uBN0XEzIjYATgRuKF2hYhoBtqBv8rMhwazrSRJ0mjUsMOambkuIuYCNwLjgSsy8/6IOKNcvgA4F9gduDQiANaVo2D9btuoWiVJkqoiMvs9lWu71Nramh0dHSNdhiRJ0hZFxKLMbO3b7i8ESJIkVYjhTJIkqUIMZ5IkSRViOJMkSaoQw5kkSVKFGM4kSZIqxHAmSZJUIYYzSZKkCjGcSZIkVYjhTJIkqUIMZ5IkSRViOJMkSaoQw5kkSVKFGM4kSZIqxHAmSZJUIYYzSZKkCjGcSZIkVciEkS6g0V5++WW6urpYu3btSJey3Zk0aRJNTU1MnDhxpEuRJGnMGPXhrKuri8mTJzNjxgwiYqTL2W5kJqtWraKrq4uZM2eOdDmSJI0Zo/6w5tq1a9l9990NZoMUEey+++6OOEqSNMxGfTgDDGZbyc9NkqThNybCWRUsXLiQiODBBx/c7HoXXnghL7zwwla/zre//W3mzp271dtLkqSRZTgbJtdccw2HHXYY11577WbX29ZwJkmStm+Gs746O+G88+DUU4vHzs5t7nLNmjXccccdfOtb39oYzl555RXmzZvHgQceSEtLC//8z//MRRddxIoVKzj88MM5/PDDAdhll1029nPddddxyimnAPCDH/yAd77znRx00EF84AMf4KmnntrmOiVJ0sgb9VdrDkpnJ8yfD9OmQVMTdHcX8/PmQUvLVnd7/fXXM3v2bPbbbz9222037rnnHn7961/z2GOPce+99zJhwgSeffZZdtttN77xjW9w6623sscee2y2z8MOO4xf/epXRASXX345F1xwAV//+te3ukZJklQNhrNa7e1FMJs2rZjf8Njevk3h7JprruEzn/kMACeeeCLXXHMNjz76KGeccQYTJhRfwW677TaoPru6ujjhhBP47W9/y0svveTtLiRJGiUMZ7WWLStGzGpNnVq0b6VVq1Zxyy23cN999xERvPLKK0QEf/iHf1jX1ZC169Te1uJTn/oUn/3sZ5kzZw633XYb55133lbXKEmSqsNzzmo1N0NPT++2np6ifStdd911nHzyyTzxxBM8/vjjPPnkk8ycOZODDz6YBQsWsG7dOgCeffZZACZPnszzzz+/cfu9996bJUuWsH79ehYuXFhTVg/Tp08H4Morr9zq+iRJUrUYzmq1tRXnmXV3w/r1m563tW11l9dccw3HHntsr7bjjjuOFStW0NzcTEtLC29/+9u5+uqrATj99NM56qijNl4QcP7553P00Ufzvve9j3322WdjH+eddx5/+qd/yrvf/e4tnp8mSZK2H5GZI13DkGltbc2Ojo5ebUuWLOGtb31r/Z10dhbnmC1bVoyYtbVt0/lm27tBf36SJKkuEbEoM1v7tnvOWV8tLWM6jEmSpJHlYU1JkqQKMZxJkiRViOFMkiSpQgxnkiRJFWI4kyRJqhDD2TAYP348s2bN2jidf/75A657/fXX88ADD2ycP/fcc/nZz362zTWsXr2aSy+9dJv7kSRJjeWtNIbBTjvtxOLFi+ta9/rrr+foo49m//33B+ArX/nKkNSwIZx98pOfHJL+JElSYzhy1kdnJ5x3Hpx6avHY2dm41zrrrLPYf//9aWlpYd68edx5553ccMMNnHnmmcyaNYtHHnmEU045heuuuw6AGTNmcM4553DooYfS2trKPffcw5FHHskb3vAGFixYAMCaNWt4//vfz8EHH8yBBx7I97///Y2v9cgjjzBr1izOPPNMAL72ta/xjne8g5aWFr70pS817o1KkqS6NXTkLCJmA/8EjAcuz8zz+yx/C/CvwMHAFzJzfs2yx4HngVeAdf3dQXeodXbC/PkwbVrx++fd3cX8vHnbdl/aF198kVmzZm2cP/vsszniiCNYuHAhDz74IBHB6tWr2XXXXZkzZw5HH300xx9/fL997bvvvvzyl7/kb/7mbzjllFO44447WLt2LQcccABnnHEGkyZNYuHChUyZMoVnnnmGP/qjP2LOnDmcf/753HfffRtH8G666SYefvhh7rrrLjKTOXPmcPvtt/Oe97xn69+oRlTndQ/RfvFyli2fQPP0dbTNnU7L8fuNdFmSpEFqWDiLiPHAJcARQBdwd0TckJkP1Kz2LPA/gY8O0M3hmflMo2rsq729CGbTphXzGx7b27ctnPV3WHPdunVMmjSJ0047jQ9/+MMcffTRdfU1Z84cAA488EDWrFnD5MmTmTx5MpMmTWL16tXsvPPOnHPOOdx+++2MGzeO5cuX89RTT72qn5tuuombbrqJgw46CChG3B5++GHD2Xaq87qHmP+5p5k2JWjaZx3dq4P5n3uaeWBAk6TtTCMPax4CLM3MRzPzJeBa4JjaFTLz6cy8G3i5gXXUbdkymDq1d9vUqUX7UJswYQJ33XUXxx13HNdffz2zZ8+ua7sdd9wRgHHjxm18vmF+3bp1fOc732HlypUsWrSIxYsXs/fee7N27dpX9ZOZnH322SxevJjFixezdOlSPv7xjw/Nm9Owa794OdOmrGParjBuXDBtV5g2ZR3tFy8f6dIkSYPUyHA2HXiyZr6rbKtXAjdFxKKIOH2glSLi9IjoiIiOlStXbmWpheZm6Onp3dbTU7QPtcpLt0gAAAijSURBVDVr1tDT08OHPvQhLrzwwo0ja5MnT+b555/f6n57enrYa6+9mDhxIrfeeitPPPFEv/0eeeSRXHHFFaxZswaA5cuX8/TTT2/DO9JIWrZ8AlOnZK+2qVOSZcu95keStjeN/D939NOW/bQN5F2ZuSIi9gJ+GhEPZubtr+ow8zLgMoDW1tbB9P8qbW3FOWZQjJj19BTnnW3rgFLfc85mz57Npz/9aY455hjWrl1LZvLNb34TgBNPPJFPfOITXHTRRRsvBBiMk046iY985CO0trYya9Ys3vKWtwCw++678653vYu3ve1tHHXUUXzta19jyZIlHHrooQDssssuXHXVVey1117b9mY1IpqnF4cyp+26qa3nuaB5+rqRK0qStFUic5vyzMAdRxwKnJeZR5bzZwNk5j/0s+55wJraCwIGs3yD1tbW7Ojo6NW2ZMkS3vrWt9Zdd2dncY7ZsmXFiFlb27adb7a9G+znp5Gx6ZyzdUydkvQ8F3Q/N4F5F+zlOWeSVFERsai/Cx4bOXJ2N/CmiJgJLAdOBP6ing0jYmdgXGY+Xz7/IDA0N/zagpaWsR3GtH1qOX4/5kGvqzU//kWDmSRtjxoWzjJzXUTMBW6kuJXGFZl5f0ScUS5fEBGvBTqAKcD6iPgMsD+wB7AwIjbUeHVm/qRRtUqjQcvx+xnGJGkUaOjZwpn578C/92lbUPP8d0BTP5s+B7y9kbVJkiRV0Zj4hYBGnVc32vm5SZI0/EZ9OJs0aRKrVq0yaAxSZrJq1SomTZo00qVIkjSmjPqbIDU1NdHV1cW23gNtLJo0aRJNTf0ddZYkSY0y6sPZxIkTmTlz5kiXIUmSVJdRf1hTkiRpe2I4kyRJqhDDmSRJUoU07OebRkJErASeaPDL7AE80+DXkLaF+6iqzn1UVTdc++jrMnPPvo2jKpwNh4jo6O93sKSqcB9V1bmPqupGeh/1sKYkSVKFGM4kSZIqxHA2eJeNdAHSFriPqurcR1V1I7qPes6ZJElShThyJkmSVCFjIpxFxBUR8XRE3FfTFhHxxYh4OCIeioifR0RLuew1EfGjiHgwIu6PiPNrttsxIr4bEUsj4tcRMaNm2U8iYnVE/LDP6/8iIhaX04qIuL7x71rbk4jYNyJujYgl5T736bLd/VSVEBGTIuKuiPjPcn/7ctnuPqpKiYjxEXHvhv1nu9xHM3PUT8B7gIOB+2ra5gL/DrymnP8gxT3SdgZeAxxetu8A/AI4qpz/JLCgfH4i8N2aPt8PfAT44WZq+Tfg5JH+TJyqNQH7AAeXzycDDwH7u586VWUCAtilfD4R+DXwR+6jTlWbgM8CV2/Yf7bHfXRMjJxl5u3As32aPw98KjNfKNe5CbgdOCkzX8jMW8v2l4B7gKZyu2OAK8vn1wHvj4go170ZeH6gOiJiMvA+wH/tqZfM/G1m3lM+fx5YAkzH/VQVkYU15ezEckrcR1UhEdEEfBi4vKZ5u9tHx0Q46ysipgA7Z+YjfRZ1UIxW1K67K0U6vrlsmg48CZCZ64AeYPc6X/pY4ObMfG4rS9cYUA6dH0QxMuF+qsooDxctBp4Gfkrxjwj3UVXJhcDngPWw/f69H5PhbDOi10zEBOAa4KLMfLS/dUr1XvL652V/Ur8iYheKofDPbG61Ptu4n2pYZOYrmTmLYmThEGDGAKu6j2rYRcTRwNOZuaie1ftsW6l9dEyGszLJ/j4iXt9n0cEUaXqDy4CHM/PCmrYuYF/Y+GVO5dWHTF8lInan+J/Zj7ahdI1iETGRIph9JzPb3U9VVZm5GriN4twd91FVxbuAORHxOHAtxWHFS9kO99ExGc5KXwMuioidACLiA8ABFMeViYj/l+KL6DuCcQPwsfL58cAtWZ75twV/SnHi4NohqF2jTHkew7eAJZn5jZpF7qeqhIjYszzsQ7k/fgB4EPdRVURmnp2ZTZk5g+IE/lsy8y/ZHvfR4bhyYqQniqHF3wIvUyThj1MMV54LPAw8DqwAdivXb6IYulwCLC6n08plk4D/CywF7gJeX/M6vwBWAi+Wr3NkzbLbgNkj/Vk4VXMCDiv3uc6afe5D7qdOVZmAFuDech+9Dzi3bHcfdarcBPwJm67W3O72UX8hgI3n+SwE7s7Mc0a6Hqk/7qeqOvdRVd32so8aziRJkipkLJ9zJkmSVDmGM0mSpAoxnEmSJFWI4UySJKlCDGeSRq2IaIqI70fEwxHxaERcHBE7DlHfp0TEHwxFX5JUy3AmaVQqb+zbDlyfmW8C3gTsBFwwBH2PB04BBhXOyruMS9JmGc4kjVbvA9Zm5r9C8buQwN8AJ0fE3Ii4eMOKEfHDiPiT8vn/FxEdEXF/RHy5Zp3HI+LciPgPit/NawW+ExGLI2KniPjDiPh5RCyKiBsjYp9yu9si4u8j4ufAp4frzUvafvmvOEmj1QFArx9Azsznyt/d29z/+76Qmc+Wo2M3R0RLZnaWy9Zm5mEAEXEaMC8zO8rfRf1n4JjMXBkRJwBfBU4tt9s1M987dG9N0mhmOJM0WgXFz7L01745fxYRp1P8/3EfYH+KnywC+O4A27wZeBvw0+JoKuMpfjJug4G2k6RXMZxJGq3uB46rbYiIKcDewCpgv5pFk8rlM4F5wDsyszsivr1hWen3A7xWAPdn5qEDLB9oO0l6Fc85kzRa3Qy8JiJOho0n8X8duBh4DJgVEeMiYl/gkHKbKRRBqici9gaO2kz/zwOTy+e/AfaMiEPL15oYEQcM9RuSNDYYziSNSln8cPCxwPER8TDFaNn6zPwqcAdFQPsvYD5wT7nNfwL3Uoy6XVGuN5BvAwsiYjHFYczjgX+MiP8EFgN/3IC3JWkM8IfPJY0JEfHHwDVAW2Yu2tL6kjRSDGeSJEkV4mFNSZKkCjGcSZIkVYjhTJIkqUIMZ5IkSRViOJMkSaoQw5kkSVKFGM4kSZIq5P8HrX7DyP6uDPkAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "f = plt.figure(figsize=(10, 5))\n",
    "x_positions = [1, 2, 3, 4]\n",
    "chart_labels = [\"1Q2017\",\"2Q2017\",\"3Q2017\",\"4Q2017\"]\n",
    "earnings_actual =[.4, .15,.29,.41]\n",
    "earnings_estimate = [.37,.15,.32,.41 ]\n",
    "plt.scatter(x_positions, earnings_actual, color='red', alpha=0.5)\n",
    "plt.scatter(x_positions, earnings_estimate, color='blue', alpha=0.5)\n",
    "plt.xticks(x_positions, chart_labels)\n",
    "plt.title('Earning vs Estimate Per Share in Cents')\n",
    "plt.xlabel('Quarter')\n",
    "plt.ylabel('Cents')\n",
    "plt.legend(['Actual', 'Estimate'])\n",
    "plt.savefig('earnings_vs_estimate.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "## Graph Literacy\n",
    "\n",
    "+ What do the purple dots tell us about the actual and estimate earnings per share in this graph? Hint: In color theory red and blue mix to make purple.  \n",
    "        The purple dots tells us that the actual and the estimate are on the same point which means the estimated earnings \n",
    "        was correct.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 7"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side. We have visualized a similar chart in the second Matplotlib lesson [Exercise 4](https://www.codecademy.com/courses/learn-matplotlib/lessons/matplotlib-ii/exercises/side-by-side-bars).\n",
    "\n",
    "As you may recall, plotting side-by-side bars in Matplotlib requires computing the width of each bar before hand. We have pasted the starter code for that exercise below. \n",
    "\n",
    "1. Fill in the `n`, `t`, `d`, `w` values for the revenue bars\n",
    "2. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `revenue_by_quarter` data\n",
    "3. Fill in the `n`, `t`, `d`, `w` values for the earnings bars\n",
    "4. Plot the revenue bars by calling `plt.bar()` with the newly computed `x_values` and the `earnings_by_quarter` data\n",
    "5. Create a legend for your bar chart with the `labels` provided\n",
    "6. Add a descriptive title for your chart with `plt.title()`\n",
    "7. Add labels to each quarter by assigning the position of the ticks through the code provided. Hint:  `plt.xticks(middle_x, quarter_labels)`\n",
    "8. Be sure to show your plot!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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G24A4Fvf+hYHHHAAEydO7Lf9akuWLOGmm27iyiuv5NRTTx20jqeffpoPfvCDzJs3jwULFvDe977XnjlJkkaRcXk5sg1PPvkkM2fO5MEHH2T33Xdn//33Z8WKFdx88828853vXNPuqaeeAuCoo47isssu4y1veQuXXnopJ5544qDtAY488khe8YpXsOOOO/Lzn/980Hruv/9+7r77bvbff3+gEw633HLLtbnLkqSXaW3fPjPShnO7jgZmCFtLVt8Ttnz5cg499FA+//nPc/zxxzN58uQ194p1O/zww/n4xz/OY489xoIFC9hvv/144oknBmwPsMEGG6wZryoA1ltvvTWXNYE1j5uoKnbaaSe+973vrc3dlCRJa4mXI9eyzTbbjLlz53LOOeew4YYbss022/C1r30N6ASjO+64A4CNN96YPffckw9/+MMceuihTJgwgU033XTA9gPZeuutuffee3nqqadYvnw51157LQDbb789S5cuXRPCnn76ae65555e7bYkSXqRDGE9sOuuuzJjxgwuvfRSLr74Yi644AJmzJjBTjvtxDe/+c017Y466iguuugijjrqqDXTBmvfn2nTpvGud72LXXbZhXe/+93suuuuAKy//vrMmzePU045hRkzZjBz5kxuvvnm3uywJEl60bL6stZYMWvWrJo/f/7zpi1atIgddtihpYrGPo+fJLXDe8LGvyQLqmpWf/PsCZMkSWqBIUySJKkFhjBJkqQWGMIkSZJaYAiTJElqQc9CWJJJSW5JckeSe5Kc2U+b2UmWJ1nYDKf3qh5JkqTRpJc9YU8B+1XVDGAmcGCSvfppd2NVzWyGT/Wwnp6aMGECM2fOXDOcddZZa2W98+fP50Mf+tBaWZckSRo9evbaouo8gGxF83FiM4zMQ8nO2Gwtr2/5kE1Wv7bopXjmmWdYb73+fxSzZs1i1qx+Hy8iSZLGsJ7eE5ZkQpKFwCPANVX1g36a7d1csvx2kp16WU8bPvWpT7HHHnuw8847M2fOnDXvfJw9ezannXYa++67L3/3d3/H7NmzOeWUU9hzzz15/etfz4033gjA9ddfz6GHHgrAGWecwXvf+15mz57Ntttuy9y5c9ds5y//8i95wxvewP77788xxxzDOeecA8DcuXPZcccd2WWXXTj66KNHeO8lSdJAehrCqurZqpoJTAX2TLJznya3AVs3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\n",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[2.35, 4.35, 5.64, 7.84]\n"
     ]
    }
   ],
   "source": [
    "f = plt.figure(figsize=(10, 5))\n",
    "# The metrics below are in billions of dollars\n",
    "revenue_by_quarter = [2.79, 2.98,3.29,3.7]\n",
    "earnings_by_quarter = [.0656,.12959,.18552,.29012]\n",
    "quarter_labels = [\"2Q2017\",\"3Q2017\",\"4Q2017\", \"1Q2018\"]\n",
    "\n",
    "# Revenue\n",
    "n = 1   # This is our first dataset (out of 2)\n",
    "t = 2   # Number of dataset\n",
    "d = 4   # Number of sets of bars\n",
    "w = 0.7 # Width of each bar\n",
    "bars1_x = [t*element + w*n for element in range(d)]\n",
    "\n",
    "# Earnings\n",
    "n = 2   # This is our first dataset (out of 2)\n",
    "t = 2   # Number of dataset\n",
    "d = 4   # Number of sets of bars\n",
    "w = 0.7 # Width of each bar\n",
    "bars2_x = [t*element + w*n for element in range(d)]\n",
    "\n",
    "middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]\n",
    "plt.bar(bars1_x, revenue_by_quarter, width=w)\n",
    "plt.bar(bars2_x, earnings_by_quarter, width=w)\n",
    "plt.legend(labels)\n",
    "plt.xticks(middle_x, quarter_labels)\n",
    "plt.xlabel('Quarter')\n",
    "plt.ylabel('Cents')\n",
    "plt.title('Earnings and Revenue per Quarter')\n",
    "plt.savefig('earn_rev_quarter.png')\n",
    "plt.show()\n",
    "print([round(earnings_by_quarter[i] / revenue_by_quarter[i] * 100, 2) for i in range(4)])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Graph Literacy\n",
    "What are your first impressions looking at the visualized data?\n",
    "\n",
    "- Does Revenue follow a trend?  \n",
    "        Yes, the revenue is growing which is a good sign for the company\n",
    "- Do Earnings follow a trend?  \n",
    "        Yes, the earnings if also growing but is much slower than the revenue\n",
    "- Roughly, what percentage of the revenue constitutes earnings?  \n",
    "        The percentage of the revenue constitutes to earning is roughly 2-8%"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Step 8\n",
    "\n",
    "In this last step, we will compare Netflix stock to the Dow Jones Industrial Average in 2017. We will accomplish this by plotting two line charts side by side in one figure. \n",
    "\n",
    "Since `Price` which is the most relevant data is in the Y axis, let's map our subplots to align vertically side by side.\n",
    "- We have set up the code for you on line 1 in the cell below. Complete the figure by passing the following arguments to `plt.subplots()` for the first plot, and tweaking the third argument for the second plot\n",
    "    - `1`-- the number of rows for the subplots\n",
    "    - `2` -- the number of columns for the subplots\n",
    "    - `1` -- the subplot you are modifying\n",
    "\n",
    "- Chart the Netflix Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`netflix_stocks['Date'], netflix_stocks['Price']`)\n",
    "- Assign \"Netflix\" as a title to this subplot. Hint: `ax1.set_title()`\n",
    "- For each subplot, `set_xlabel` to `\"Date\"` and `set_ylabel` to `\"Stock Price\"`\n",
    "- Chart the Dow Jones Stock Prices in the left-hand subplot. Using your data frame, access the `Date` and `Price` charts as the x and y axes respectively. Hint: (`dowjones_stocks['Date'], dowjones_stocks['Price']`)\n",
    "- Assign \"Dow Jones\" as a title to this subplot. Hint: `plt.set_title()`\n",
    "- There is some crowding in the Y axis labels, add some space by calling `plt.subplots_adjust(wspace=.5)`\n",
    "- Be sure to `.show()` your plots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 720x360 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']\n",
    "f = plt.figure(figsize=(10, 5))\n",
    "# Left plot Netflix\n",
    "ax1 = plt.subplot(1, 2, 1)\n",
    "plt.plot(netflix_stocks['Date'], netflix_stocks['Price'])\n",
    "ax1.set_title('Netflix')\n",
    "ax1.set_xlabel('Month')\n",
    "ax1.set_ylabel('Stock Price')\n",
    "ax1.set_xticklabels(months, rotation=45)\n",
    "\n",
    "# Right plot Dow Jones\n",
    "ax2 = plt.subplot(1, 2, 2)\n",
    "plt.plot(dowjones_stocks['Date'], dowjones_stocks['Price'])\n",
    "ax2.set_title('Dow Jones')\n",
    "ax2.set_xlabel('Month')\n",
    "ax2.set_ylabel('Stock Price')\n",
    "ax2.set_xticklabels(months, rotation=45)\n",
    "\n",
    "plt.subplots_adjust(wspace=0.5)\n",
    "plt.savefig('comp_netflix_dowjones.png')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- How did Netflix perform relative to Dow Jones Industrial Average in 2017?  \n",
    "        Netflix's performance was more volatile where there were a lot of times where the stock prices went down while \n",
    "        Dow Jones was more consistent in growing\n",
    "- Which was more volatile?  \n",
    "        Netflix\n",
    "- How do the prices of the stocks compare?\n",
    "        The prices of Dow Jones is somewhere form 20k and above while Netflix's is just somewhere between 140-200"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Step 9\n",
    "\n",
    "It's time to make your presentation! Save each of your visualizations as a png file with `plt.savefig(\"filename.png\")`.\n",
    "\n",
    "As you prepare your slides, think about the answers to the graph literacy questions. Embed your observations in the narrative of your slideshow!\n",
    "\n",
    "Remember that your slideshow must include:\n",
    "- A title slide\n",
    "- A list of your visualizations and your role in their creation for the \"Stock Profile\" team\n",
    "- A visualization of the distribution of the stock prices for Netflix in 2017\n",
    "- A visualization and a summary of Netflix stock and revenue for the past four quarters and a summary\n",
    "- A visualization and a brief summary of their earned versus actual earnings per share\n",
    "- A visualization of Netflix stock against the Dow Jones stock (to get a sense of the market) in 2017\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
