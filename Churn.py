from pydantic import BaseModel
# 2. Class which describes data values
class Churn(BaseModel):
    SeniorCitizen: int 
    Partner : str
    Dependents: str
    tenure : int   
    MultipleLines : str
    InternetService: str 
    OnlineSecurity :str
    OnlineBackup : str
    DeviceProtection: str
    TechSupport : str
    StreamingTV : str
    StreamingMovies : str   
    Contract : str        
    PaperlessBilling : str 
    PaymentMethod : str 
    MonthlyCharges : float
    TotalCharges :float 