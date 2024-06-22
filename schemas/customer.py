import pandera as pa
from pandera import Column, Check, Index

class SchemaCustomer(pa.SchemaModel):
    CustomerKey: pa.Column[int] = Column(
        pa.Int,
        checks=[
            Check.greater_than_or_equal_to(min_value=1),
            Check.less_than_or_equal_to(max_value=19145),
        ],
        nullable=False,
        required=True,
    )
    GeographyKey: pa.Column[int] = Column(
        pa.Int,
        checks=[
            Check.greater_than_or_equal_to(min_value=423),
            Check.less_than_or_equal_to(max_value=952),
        ],
        nullable=False,
        required=True,
    )
    FirstName: pa.Column[str] = Column(pa.String, nullable=True, required=True)
    LastName: pa.Column[str] = Column(pa.String, nullable=True, required=True)
    BirthDate: pa.Column[str] = Column(pa.String, nullable=True, required=True)
    MaritalStatus: pa.Column[str] = Column(pa.String, nullable=True, required=True)
    Gender: pa.Column[str] = Column(pa.String, nullable=True, required=True)
    EmailAddress: pa.Column[str] = Column(pa.String, nullable=True, required=True)
    Education: pa.Column[str] = Column(pa.String, nullable=True, required=True)
    Occupation: pa.Column[str] = Column(pa.String, nullable=True, required=True)
    CustomerType: pa.Column[str] = Column(pa.String, nullable=False, required=True)
    CompanyName: pa.Column[str] = Column(pa.String, nullable=True, required=True)

    # Index definition
    index: pa.Index = Index(
        pa.Int,
        checks=[
            Check.greater_than_or_equal_to(min_value=0),
            Check.less_than_or_equal_to(max_value=18868),
        ],
        nullable=False,
    )

    class Config:
        coerce = True
        strict = False
        report_duplicates = "all"
