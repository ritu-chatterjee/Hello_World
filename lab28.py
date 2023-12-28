import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Q1. Write a Pandas program to split the following data frame into groups based on Class and count the number of students in that particular class. Also generate a bar chart based on the result and explain the conclusion.

def Lab1():
    student_data = pd.DataFrame({

                                 'school_code': ['s001','s002','s003','s001','s002','s004'],

                                 'class': ['V', 'VI', 'VI', 'VI', 'V', 'VI'],

                                 'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],

                                 'age': [12, 12, 13, 13, 14, 12],

                                 'height': [173, 192, 186, 167, 151, 159],

                                 'weight': [35, 32, 33, 30, 31, 32],

                                 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
                                 } )
    print(student_data[['class','name']].groupby(['class']).agg(['count']))
    student_data['class'].value_counts().plot(kind='bar')
    plt.xlabel('Class')
    plt.ylabel('Number of students')
    plt.title('Number of Students in Each Class')
    plt.show()

Lab1()
#Conclusion:The generated bar chart visually represents the number of students in each class.we can observe that the number of students in class VI is more than the number of students in class V. 

#Q2. Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group. Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id).Also generate a line chart based on the result and explain the conclusion.
def Lab2():
    orders_data = pd.DataFrame({
                               'ord_no':[70001,70009,70002,70004,70007,70005,70008,70010,70003,70012,70011,70013],
                               'purch_amt':[150.5,270.65,65.26,110.5,948.5,2400.6,5760,1983.43,2480.4,250.45,75.29,3045.6],
                               'ord_date':['2012-10-05','2012-09-10','2012-10-05','2012-08-17','2012-09-10','2012-07-27','2012-09-10','2012-10-10','2012-10-10','2012-06-27','2012-08-17','2012-04-25'],
                               'customer_id':[3005,3001,3002,3009,3005,3007,3002,3004,3009,3008,3003,3002],
                               'salesman_id': [5002,5005,5001,5003,5002,5001,5001,5006,5003,5002,5007,5001]})
    print(orders_data[['purch_amt','customer_id']].groupby(['customer_id']).agg([ 'mean','min','max']))
    orders_data ['Date']=pd.to_datetime(orders_data ['ord_date'], format='%Y-%m-%d')
    orders_data ['Month'] = pd.DatetimeIndex(orders_data ['Date']).month
    orders_data ['Month Name'] = orders_data ['Date'].dt.month_name(locale = 'English')
    orders_sale =orders_data.groupby('Month Name')['purch_amt'].sum().reset_index()
    plt.plot(orders_sale['Month Name'], orders_sale['purch_amt'], marker='o',linestyle='-',color='b', label='purch_amt')
    plt.xlabel('order month')
    plt.ylabel('purchase amount')
    plt.title('Order month-wise Purchase amount ')
    plt.grid(True)
    plt.legend()
    plt.show()

Lab2()

#Conclusion:The generated line chart visually represents the purchase amount in each month.We can observe that September has the highest purchase amount of orders where June and August have the lowest purchase amount of orders.


