import pandas as pd
import os
print("_______________________________________________________________________________")
base_path = "RAW DATA"
file_catering = "catering_log.csv"
file_camera="camera_dept.csv"
file_talent="talent_payouts.csv"
file_transport="transport_dubai.csv"
full_path_catering = os.path.join(base_path, file_catering)
read_catering_file=pd.read_csv(full_path_catering)
valid_col_catering={"Date","Vendor","Meal_Type","Headcount","Price_Per_Head"}
current_col_catering=set(read_catering_file.columns)
missing_col_catering=valid_col_catering-current_col_catering
print('Checking catering file\n')
if not missing_col_catering:
    print("Succes! all columns are present.Proceeding") 
    read_catering_file["Total_Spend"]=read_catering_file["Headcount"]*read_catering_file["Price_Per_Head"]
    os.makedirs("PROCESSED_DATA",exist_ok=True)
    read_catering_file.to_csv("PROCESSED_DATA\Cleaned_catering.csv",index=False)
    print("\nfile saved in processed_data folder as Cleaned_catering.csv\n_______________________________________________________________________________")
else:
    print(f"columns missing {missing_col_catering} \n fix that !")


full_path_camera=os.path.join(base_path,file_camera)
read_camera_file=pd.read_csv(full_path_camera)
valid_col_camera={"Date","Item_Name","Daily_Rate","Days","Total_Cost"}
current_col_camera=set(read_camera_file.columns)
missing_col_camera=valid_col_camera-current_col_camera
print('Checking camera file\n')
if not missing_col_camera:
     print("Succes! all required columns are present in camera_dept.csv file.Proceeding") 
     read_camera_file["Daily_Rate"]=read_camera_file["Daily_Rate"].str.replace("AED","")
     read_camera_file["Daily_Rate"]=pd.to_numeric(read_camera_file["Daily_Rate"])
     read_camera_file["Days"]=pd.to_numeric(read_camera_file["Days"])
     read_camera_file["Total_Cost"]=read_camera_file["Days"]*read_camera_file["Daily_Rate"]
     os.makedirs("PROCESSED_DATA",exist_ok=True)
     read_camera_file.to_csv("PROCESSED_DATA\Cleaned_camera_dept.csv",index=False)
     print("\nfile saved in processed_data folder as Cleaned_camera_dept.csv\n_______________________________________________________________________________")
else:
    print(f"columns missing {missing_col_camera} \n fix that !")

full_path_transport=os.path.join(base_path,file_transport)
read_transport_file=pd.read_csv(full_path_transport)
valid_col_transport={"Date","Vehicle_Type","Fuel_AED","Salik_Tolls","Driver_OT_Hours"}
current_col_transport=set(read_transport_file.columns)
missing_col_transport=valid_col_transport-current_col_transport
print('Checking transport file\n')
if not missing_col_transport:
     print("Succes! all required columns are present in transport_dubai.csv file.Proceeding")
     read_transport_file["Driver_OT_Hours"]=pd.to_numeric(read_transport_file["Driver_OT_Hours"])
     read_transport_file["Fuel_AED"]=pd.to_numeric(read_transport_file["Fuel_AED"])
     read_transport_file["Salik_Tolls"]=pd.to_numeric(read_transport_file["Salik_Tolls"])
     read_transport_file["Total_Transport_Cost"]=read_transport_file["Fuel_AED"]+read_transport_file["Salik_Tolls"]+(read_transport_file["Driver_OT_Hours"]*50)
     os.makedirs("PROCESSED_DATA",exist_ok=True)
     read_transport_file.to_csv("PROCESSED_DATA\Cleaned_Transport_Dubai.csv",index=False)
     print("\nfile saved in processed_data folder as Cleaned_Transport_Dubai.csv\n_______________________________________________________________________________")
else:
     print(f"columns missing {missing_col_transport} \n fix that !")

full_path_talent=os.path.join(base_path,file_talent)
read_talent_file=pd.read_csv(full_path_talent)
valid_col_talent={"Actor_Name","Role","Agency","Contract_Fee","Status"}
current_col_talent=set(read_talent_file.columns)
missing_col_talent=valid_col_talent-current_col_talent
print('Checking talent file\n')
if not missing_col_talent:
          print("Succes! all required columns are present in talent_payout.csv file.Proceeding")
          read_talent_file["Contract_Fee"]=pd.to_numeric(read_talent_file["Contract_Fee"])
          read_talent_file=read_talent_file[read_talent_file["Status"].str.lower()!="pending"]
          os.makedirs("PROCESSED_DATA",exist_ok=True)
          read_talent_file.to_csv("PROCESSED_DATA/Cleaned_Talent_Payout.csv",index=False)
          print("\nfile saved in processed_data folder as Cleaned_Talent_Payout.csv\n_______________________________________________________________________________")
else:
        print(f"columns missing {missing_col_talent} \n fix that !")
                          