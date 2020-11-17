{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the first number: 8\n",
      "Enter the second number: 1\n",
      "A \t B \t A Binary \t B binary \t Diffrence in number of ones \n",
      "8 \t 1 \t 01000 \t     01 \t         0 \n",
      "Bit Balanced \n"
     ]
    }
   ],
   "source": [
    "def count_1s(a,b):\n",
    "    i=0\n",
    "    count=0\n",
    "    while(i<b):\n",
    "        f=int(a[i])\n",
    "        if f==1:\n",
    "            count+=1\n",
    "        i+=1\n",
    "    return(count)\n",
    "A=int(input('Enter the first number: '))\n",
    "B=int(input('Enter the second number: '))\n",
    "A_Bin=bin(A).replace(\"0b\", \"0\")\n",
    "B_Bin=bin(B).replace(\"0b\", \"0\")\n",
    "A1s=count_1s(A_Bin,len(A_Bin))\n",
    "B1s=count_1s(B_Bin,len(B_Bin))\n",
    "if (A1s>B1s):\n",
    "    Diff=(A1s-B1s)\n",
    "else:\n",
    "    Diff=(B1s-A1s)\n",
    "print('A \\t B \\t A Binary \\t B binary \\t Diffrence in number of ones ')\n",
    "print('{0} \\t {1} \\t {2} \\t     {3} \\t         {4} '.format(A,B,A_Bin,B_Bin,Diff))\n",
    "if(Diff==0):\n",
    "    print('Bit Balanced ')\n",
    "else:\n",
    "    print('Bit Biased ')"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
