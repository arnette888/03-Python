{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 183,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Import the os module\n",
    "import os\n",
    "\n",
    "# Module for reading CSV files\n",
    "import csv\n",
    "\n",
    "# importing pandas as pd \n",
    "import pandas as pd "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 184,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set path for file\n",
    "csvpath = os.path.join(\"Resources\", \"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Open the CSV\n",
    "with open(csvpath) as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    data = list(csvreader)\n",
    "    row_count = (len(data)-1);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating the dataframe  \n",
    "df = pd.read_csv(csvpath) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 187,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The net total amount of \"Profit/Losses\" over the entire period\n",
    "totalSum = df[\"Profit/Losses\"].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 188,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The average of the changes in \"Profit/Losses\" over the entire period\n",
    "totalAverage = df[\"Profit/Losses\"].mean()\n",
    "totalAverageR = round(totalAverage,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 189,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The greatest increase in profits (date and amount) over the entire period\n",
    "profitIncrease = df.max()\n",
    "Month1 = profitIncrease[\"Date\"]\n",
    "Amount1 = profitIncrease[\"Profit/Losses\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 190,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The greatest decrease in losses (date and amount) over the entire period\n",
    "profitIncrease = df.min()\n",
    "Month2 = profitIncrease[\"Date\"]\n",
    "Amount2 = profitIncrease[\"Profit/Losses\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 191,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Months : 86\n",
      "Total:  $38382578\n",
      "Average Change: $446309.05\n",
      "Greatest Increase in Profits: Sep-2016 ($1170593)\n",
      "Greatest Decrease in Profits: Apr-2010 ($-1196225)\n"
     ]
    }
   ],
   "source": [
    "# Print results to Terminal\n",
    "print(\"Total Months : \" + str(row_count))\n",
    "print(\"Total:  $\" + str(totalSum))\n",
    "print(\"Average Change: $\" + str(totalAverageR))\n",
    "print(\"Greatest Increase in Profits: \" + str(Month1) +\" ($\"+ str(Amount1)+\")\")\n",
    "print(\"Greatest Decrease in Profits: \" + str(Month2) +\" ($\"+ str(Amount2)+\")\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Define lines to write to txt file\n",
    "L0 = [\"Python Homework Solution - David Allan Hutchinson \\n \\n\", \" Total Months : \" + str(row_count), \"\\n Total:  $\" + str(totalSum), \"\\n Average Change: $\" + str(totalAverageR), \"\\n Greatest Increase in Profits: \" + str(Month1) +\" ($\"+ str(Amount1)+\")\", \"\\n Greatest Decrease in Profits: \" + str(Month2) +\" ($\"+ str(Amount2)+\")\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write to txt file\n",
    "file1 = open(\"Analysis/PyBank - Solution.txt\", \"w\")\n",
    "file1.writelines(L0) \n",
    "file1.close() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
