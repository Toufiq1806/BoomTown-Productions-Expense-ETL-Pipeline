import pandas as pd
import os
folder="PROCESSED_DATA"
try:
      
    file_camera=os.path.join(folder,"Cleaned_Camera_dept.csv")
    file_catering=os.path.join(folder,"Cleaned_catering.csv")
    file_transport=os.path.join(folder,"Cleaned_Transport_Dubai.csv")
    file_talent=os.path.join(folder,"Cleaned_Talent_Payout.csv")
    read_camera_dept=pd.read_csv(file_camera)
    read_transport=pd.read_csv(file_transport)
    read_catering=pd.read_csv(file_catering)
    read_talent=pd.read_csv(file_talent)
   
    read_camera_dept=read_camera_dept[["Date","Total_Cost"]]
    read_camera_dept.rename(columns={"Date":"date","Total_Cost":"amount"},inplace=True)
    read_camera_dept["department"]="camera"
    read_camera_dept["project_id"]=1

    read_catering=read_catering[['Date', 'Total_Spend']]
    read_catering.rename(columns={'Date': 'date', 'Total_Spend': 'amount'}, inplace=True)
    read_catering['department'] = 'catering'
    read_catering['project_id'] = 1
   
    read_transport=read_transport[["Date","Total_Transport_Cost"]]
    read_transport.rename(columns={"Date":"date","Total_Transport_Cost":"amount"},inplace=True)
    read_transport["department"]="transport"
    read_transport["project_id"]=1

    read_talent=read_talent[["Contract_Fee"]]
    read_talent.rename(columns={"Contract_Fee":"amount"},inplace=True)
    read_talent["department"]="talent"
    read_talent["date"]="2026-04-01"
    read_talent["project_id"]=1

    combined=pd.concat([read_camera_dept,read_catering,read_transport,read_talent],ignore_index=True)
    combined_record=combined[["project_id","department","amount","date"]]
    combined_record.to_csv("Combined_Record/combined_expenses.csv",index=False)
    print("combined expenses created successfully in combined_record folder!!")
    
except FileNotFoundError as e:
      print("ERROR: Could not find the processed files. Did you run the cleaning script first?")
