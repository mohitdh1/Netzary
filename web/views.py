from django.shortcuts import render
from datetime import date
import datetime

# Create your views here.
def show(request):
    if request.method=='POST':
        print(request.POST)
        f_date=request.POST['start_date']
        l_date=request.POST['end_date']
        a=  datetime.datetime.strptime(l_date, "%Y-%m-%d")
        b=  datetime.datetime.strptime(f_date, "%Y-%m-%d")
        roi=int(request.POST['int']) 
        principal=int(request.POST['principal'])
        delta= a-b            
        year=delta.days//360
        print(year)
        months=(delta.days-360*year)//30
        print(months)
        total_days=(delta.days-360*year)-30*months
        print(total_days)
        #if year>=1:

        
        if int(principal):
            if year>=1:
                ci=principal * (pow((1 + roi / 100), year))
                final_ci= ci-principal
                total_ci=final_ci*(year*12)
                principal=total_ci + principal
                print(principal)
                perm=float((principal/100)*roi)
                print(perm)
                total_months_rate=float(months*perm)
                print(total_months_rate)
                total_days_rate=float(perm/30)*total_days
                
                intr=total_months_rate + total_days_rate
                print(intr)
                final=principal + intr 
            else:
                perm=float((principal/100)*roi)
                total_months_rate=float(months*perm)
                total_days_rate=float(perm/30)*total_days
                year_rate=(year*12)*perm
                intr=total_months_rate + total_days_rate + year_rate
                final=principal + intr
    else:
        final=0
        total_days=0
        months=0
        year=0
        intr=0
    return render(request, 'main.html',{'final': final,'year': year, 'month': months, 'day': total_days, 'int': int})

