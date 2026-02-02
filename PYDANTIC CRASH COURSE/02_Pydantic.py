# Pydantic Works on Three Steps:

# 1) Define a Pydantic Model that Represents the ideal Schema of the data. This Includes Expected Fileds, their Types, and any Validation Constraints. (e.g  gt=0 for Positive Number)

# 2) Instantiate the model with raw input data (usually a dictionary or JSON-like Structure). Pydantic Will Automatically Validate the Data and coerce it into the correct Python types (if Possible), If the Data dosen't Meet the Model's Requirements, Pydantic raises a ValidationError

# 3) Pass the Validated Model Object to Function or use it throughout codebase. This Ensures that Every Part of Your program works with clean, type-safe, and logically valid data. 


from pydantic import BaseModel
from typing import Optional

class Patient:

    name: str
    age: int
    height: Optional[int] = None
    weight: Optional[float] = None


