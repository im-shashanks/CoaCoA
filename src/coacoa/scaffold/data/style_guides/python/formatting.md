# Python Code Formatting Standards

## Black Configuration

Use Black with these settings in `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py39', 'py310', 'py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''
```

## Import Organization (isort)

Configure isort in `pyproject.toml`:

```toml
[tool.isort]
profile = "black"
multi_line_output = 3
include_trailing_comma = true
force_grid_wrap = 0
use_parentheses = true
ensure_newline_before_comments = true
line_length = 88
src_paths = ["src", "tests"]

known_first_party = ["your_project_name"]
known_third_party = ["pytest", "requests", "fastapi"]

sections = ["FUTURE", "STDLIB", "THIRDPARTY", "FIRSTPARTY", "LOCALFOLDER"]
```

## Code Structure Standards

### Function and Class Layout
```python
# Standard order:
# 1. Module docstring
# 2. Imports (stdlib, third-party, local)
# 3. Constants
# 4. Classes
# 5. Functions

"""Module docstring describing the purpose."""

import os
import sys
from pathlib import Path

import requests
from fastapi import FastAPI

from .models import User
from .exceptions import UserNotFoundError

API_VERSION = "v1"
DEFAULT_TIMEOUT = 30

class UserService:
    """Service for managing user operations."""
    
    def __init__(self, database_url: str) -> None:
        """Initialize the user service."""
        self.database_url = database_url
    
    def get_user(self, user_id: str) -> User:
        """Retrieve user by ID."""
        pass

def create_user(name: str, email: str) -> User:
    """Create a new user with given details."""
    pass
```

### Line Length and Wrapping
- Maximum line length: 88 characters
- Use parentheses for line continuation, not backslashes
- Break long function calls at logical points

```python
# Good
result = some_function(
    parameter_one="value",
    parameter_two="another_value",
    parameter_three="yet_another_value",
)

# Good - method chaining
user = (
    User.query
    .filter_by(active=True)
    .filter(User.created_at > datetime.now() - timedelta(days=30))
    .order_by(User.name)
    .all()
)
```

### Whitespace Rules
- Two blank lines around top-level classes and functions
- One blank line around method definitions inside classes
- Use spaces around operators and after commas
- No trailing whitespace

```python
class UserService:
    """Service class."""

    def __init__(self) -> None:
        self.users = []

    def add_user(self, user: User) -> None:
        """Add a user to the service."""
        self.users.append(user)


def standalone_function() -> str:
    """A standalone function."""
    return "result"
```

## Naming Conventions

### Variables and Functions
```python
# snake_case for variables and functions
user_count = 0
is_active = True
has_permission = False

def calculate_total_price() -> float:
    pass

def get_user_by_id(user_id: str) -> User:
    pass
```

### Classes and Exceptions
```python
# PascalCase for classes
class UserManager:
    pass

class DatabaseConnection:
    pass

class UserNotFoundError(Exception):
    pass
```

### Constants
```python
# UPPER_SNAKE_CASE for constants
MAX_RETRY_ATTEMPTS = 3
API_BASE_URL = "https://api.example.com"
DEFAULT_PAGE_SIZE = 20
```

### Private Members
```python
class UserService:
    def __init__(self):
        self._connection = None  # Protected
        self.__secret_key = "key"  # Private (name mangling)
    
    def _internal_method(self):  # Protected method
        pass
    
    def __private_method(self):  # Private method
        pass
```

## String Formatting

### Prefer f-strings for formatting
```python
# Good
name = "Alice"
age = 30
message = f"User {name} is {age} years old"

# Good for complex expressions
result = f"Result: {calculation() if condition else default_value}"

# Use .format() for logging templates
logger.info("User {} performed action {}", user_id, action)

# Use % formatting only for logging with lazy evaluation
logger.debug("Processing %d items", len(items))
```

## Comments and Docstrings

### Docstring Format (Google Style)
```python
def process_payment(
    amount: Decimal,
    currency: str,
    payment_method: PaymentMethod,
) -> PaymentResult:
    """Process a payment transaction.
    
    Args:
        amount: The payment amount in the specified currency
        currency: Three-letter ISO currency code (e.g., 'USD', 'EUR')
        payment_method: The payment method to use for the transaction
        
    Returns:
        PaymentResult object containing transaction details and status
        
    Raises:
        PaymentError: If the payment processing fails
        ValidationError: If the input parameters are invalid
        
    Example:
        >>> result = process_payment(
        ...     amount=Decimal('29.99'),
        ...     currency='USD',
        ...     payment_method=CreditCard(number='****1234')
        ... )
        >>> result.success
        True
    """
    pass
```

### Inline Comments
```python
# Use inline comments sparingly and for clarification
users = get_active_users()  # Only users who logged in within 30 days

# Explain complex logic
if (user.is_premium and user.trial_expired) or (not user.is_premium and user.usage_exceeded):
    # Block access for expired premium users or exceeded free users
    block_user_access(user)
```

## Type Hints Standards

### Always use type hints for public APIs
```python
from typing import Optional, List, Dict, Union, Any
from pathlib import Path

def get_user_data(
    user_id: str,
    include_private: bool = False
) -> Dict[str, Any]:
    """Get user data with optional private fields."""
    pass

def find_users(
    query: str,
    limit: Optional[int] = None
) -> List[User]:
    """Find users matching the query."""
    pass

class UserService:
    def __init__(self, config: Dict[str, str]) -> None:
        self.config = config
        self._cache: Dict[str, User] = {}
    
    @property
    def user_count(self) -> int:
        return len(self._cache)
```

### Use Union sparingly, prefer specific types
```python
# Good - specific return type
def parse_config(path: Path) -> Dict[str, str]:
    pass

# Acceptable for error handling
def safe_parse_config(path: Path) -> Union[Dict[str, str], None]:
    pass

# Better - use Optional
def safe_parse_config(path: Path) -> Optional[Dict[str, str]]:
    pass
```