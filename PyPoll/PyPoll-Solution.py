{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 302,
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
   "execution_count": 303,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Set path for file\n",
    "csvpath = os.path.join(\"Resources\", \"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 304,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Votes: 3521001\n"
     ]
    }
   ],
   "source": [
    "# Open the CSV\n",
    "with open(csvpath) as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    data = list(csvreader)\n",
    "    row_count = (len(data)-1);\n",
    "    \n",
    "print(\"Total Votes: \" + str(row_count))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 305,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Creating the dataframe  \n",
    "df = pd.read_csv(csvpath) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 306,
   "metadata": {},
   "outputs": [],
   "source": [
    "# The unique method shows every element of the series that appears only once\n",
    "unique = df[\"Candidate\"].unique()\n",
    "uniqueCount = (len(unique));"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 307,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Khan        2218231\n",
       "Correy       704200\n",
       "Li           492940\n",
       "O'Tooley     105630\n",
       "Name: Candidate, dtype: int64"
      ]
     },
     "execution_count": 307,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# The value_counts method counts unique values in a column\n",
    "count = df[\"Candidate\"].value_counts()\n",
    "count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 308,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Khan        63.0\n",
       "Correy      20.0\n",
       "Li          14.0\n",
       "O'Tooley     3.0\n",
       "Name: Candidate, dtype: float64"
      ]
     },
     "execution_count": 308,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate the percentage of votes by dividing the number of Canidates by the total number of votes for each Canidate \n",
    "percent = ((count / row_count)*100)\n",
    "percentR = round(percent,0)\n",
    "percentR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 317,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "_______________________________\n",
      "Total Votes: 3521001\n",
      "_______________________________\n",
      "Khan : 63.0% (2218231)\n",
      "Correy : 20.0% (704200)\n",
      "Li : 14.0% (492940)\n",
      "O'Tooley : 3.0% (105630)\n",
      "_______________________________\n",
      "Winner:Khan\n",
      "_______________________________\n"
     ]
    }
   ],
   "source": [
    "# Print to Terminal\n",
    "print(\"Election Results\")\n",
    "print(\"_______________________________\")\n",
    "print(\"Total Votes: \" + str(row_count))\n",
    "print(\"_______________________________\")\n",
    "for i in range(0,uniqueCount):\n",
    "    print(unique[i] +\" : \" + str(percentR[i]) + \"% (\" + str(count[i]) +\")\")\n",
    "print(\"_______________________________\")\n",
    "winner = unique[0]\n",
    "print(\"Winner:\" + winner)\n",
    "print(\"_______________________________\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 318,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Print to file\n",
    "L0 = [\"Election Results\\n\",\"_______________________________\\n\",\"Total Votes: \" + str(row_count) +\"\\n\",\"_______________________________\\n\", \"\\n\" + unique[0] + \" : \" + str(percentR[0]) + \" : \" +str(count[0]), \"\\n\" + unique[1] +\" : \"+ str(percentR[1]) +\"% : \"+str(count[1]), \"\\n\" + unique[2] +\" : \"+ str(percentR[2]) +\"% : \"+str(count[2]), \"\\n\" + unique[3] +\" : \"+ str(percentR[3]) +\"% : \"+str(count[3]), \"\\n\" + \"_______________________________\",\"\\nWinner:\" + winner ]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 319,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write to txt file\n",
    "file1 = open(\"Analysis/PyPoll - Solution.txt\", \"w\")\n",
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
