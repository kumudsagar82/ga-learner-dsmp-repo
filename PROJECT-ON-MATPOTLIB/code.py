# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)
print(data)
loan_status=data['Loan_Status'].value_counts()
print(loan_status)
data['Loan_Status'].value_counts().plot(kind="bar")

#Code starts here


# --------------
#Code starts here
import matplotlib.pyplot as plt
property_and_loan= data.groupby(['Property_Area', 'Loan_Status']).size().unstack()
# Plot stacked bar chart
property_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')




# --------------
#Code starts here
import matplotlib.pyplot as plt
education_and_loan= data.groupby(['Education', 'Loan_Status']).size().unstack()
# Plot stacked bar chart
education_and_loan.plot(kind='bar', stacked=False, figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)



# --------------
#Code starts here
graduate=data[data['Education'] == 'Graduate']
print(graduate)

not_graduate=data[data['Education'] == 'Not Graduate']
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='nonGraduate')











#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
#ax_1.scatter(data['ApplicantIncome'],data["LoanAmount"])

fig, (ax_1,ax_2,ax_3) = plt.subplots(3,1, figsize=(20,10))

# Stacked bar-chart representing counts


ax_1.scatter(data["ApplicantIncome"],data["LoanAmount"])

ax_1.set_title('Applicant Income')
ax_2.scatter(data["CoapplicantIncome"],data["LoanAmount"])
ax_2.set_title('Coapplicant Income')
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
ax_3.scatter(data["TotalIncome"],data["LoanAmount"])
ax_3.set_title('Total Income')


