{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=int(input('Enter the value of a:'))\n",
    "b=bin(a).replace(\"0b\", \"0\")\n",
    "print(b)\n",
    "c=len(b)\n",
    "print(c)\n",
    "i=0\n",
    "count=0\n",
    "while(i<c):\n",
    "    f=int(b[i])\n",
    "    if f==1:\n",
    "        count+=1\n",
    "        print('*')\n",
    "    i+=1\n",
    "print(count)"
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
