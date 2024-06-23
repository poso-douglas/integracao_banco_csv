import pandera as pa
from pandera import Column, Check, Index
from pandera.typing import Series

class SchemaCustomer(pa.SchemaModel):
    CustomerKey: Series[int] 
    GeographyKey: Series[int] # = pa.Field(ge=1,le=10,nullable=False)
    FirstName: Series[str] = pa.Field(nullable=True)
    LastName: Series[str] = pa.Field(nullable=True)
    BirthDate: Series[str] = pa.Field(nullable=True)
    MaritalStatus: Series[str] = pa.Field(nullable=True)
    Gender: Series[str] = pa.Field(nullable=True)
    EmailAddress: Series[str] = pa.Field(nullable=True)
    Education: Series[str] = pa.Field(nullable=True)
    Occupation: Series[str] = pa.Field(nullable=True)
    CustomerType: Series[str] = pa.Field(nullable=True)
    CompanyName: Series[str] = pa.Field(nullable=True)

    class Config: 
        coerce = True
        strict = True


class SchemaCustomerCSV(SchemaCustomer):
    FullName: Series[str] = pa.Field(nullable=True)
    #Age: Series[int]

    class Config: 
        coerce = True
        strict = True
        
    
