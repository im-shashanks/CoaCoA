# Result and Error Handling Patterns

## Overview
Result patterns provide a functional approach to error handling, making errors explicit in the type system and avoiding exception-based control flow.

## Result Pattern Implementations

### TypeScript Result Pattern

```typescript
// Core Result type
export type Result<T, E = Error> = Success<T> | Failure<E>;

export interface Success<T> {
  readonly success: true;
  readonly data: T;
}

export interface Failure<E> {
  readonly success: false;
  readonly error: E;
}

// Constructor functions
export const Ok = <T>(data: T): Success<T> => ({
  success: true,
  data,
});

export const Err = <E>(error: E): Failure<E> => ({
  success: false,
  error,
});

// Result utility functions
export class ResultUtils {
  static isSuccess<T, E>(result: Result<T, E>): result is Success<T> {
    return result.success;
  }
  
  static isFailure<T, E>(result: Result<T, E>): result is Failure<E> {
    return !result.success;
  }
  
  static map<T, U, E>(
    result: Result<T, E>,
    fn: (value: T) => U
  ): Result<U, E> {
    return result.success ? Ok(fn(result.data)) : result;
  }
  
  static flatMap<T, U, E>(
    result: Result<T, E>,
    fn: (value: T) => Result<U, E>
  ): Result<U, E> {
    return result.success ? fn(result.data) : result;
  }
  
  static mapError<T, E, F>(
    result: Result<T, E>,
    fn: (error: E) => F
  ): Result<T, F> {
    return result.success ? result : Err(fn(result.error));
  }
  
  // Combine multiple results
  static combine<T, E>(results: Result<T, E>[]): Result<T[], E> {
    const values: T[] = [];
    
    for (const result of results) {
      if (!result.success) {
        return result;
      }
      values.push(result.data);
    }
    
    return Ok(values);
  }
  
  // Extract value or provide default
  static unwrapOr<T, E>(result: Result<T, E>, defaultValue: T): T {
    return result.success ? result.data : defaultValue;
  }
  
  // Extract value or throw error
  static unwrap<T, E>(result: Result<T, E>): T {
    if (!result.success) {
      throw result.error;
    }
    return result.data;
  }
}

// Async Result utilities
export class AsyncResult {
  static async from<T>(promise: Promise<T>): Promise<Result<T, Error>> {
    try {
      const data = await promise;
      return Ok(data);
    } catch (error) {
      return Err(error instanceof Error ? error : new Error(String(error)));
    }
  }
  
  static async map<T, U, E>(
    resultPromise: Promise<Result<T, E>>,
    fn: (value: T) => U | Promise<U>
  ): Promise<Result<U, E>> {
    const result = await resultPromise;
    if (!result.success) {
      return result;
    }
    
    try {
      const mapped = await fn(result.data);
      return Ok(mapped);
    } catch (error) {
      return Err(error instanceof Error ? error : new Error(String(error))) as Failure<E>;
    }
  }
  
  static async flatMap<T, U, E>(
    resultPromise: Promise<Result<T, E>>,
    fn: (value: T) => Promise<Result<U, E>>
  ): Promise<Result<U, E>> {
    const result = await resultPromise;
    return result.success ? fn(result.data) : result;
  }
}

// Usage examples
async function getUserById(id: string): Promise<Result<User, UserError>> {
  if (!id) {
    return Err(new ValidationError('User ID is required', 'id'));
  }
  
  try {
    const user = await userRepository.findById(id);
    if (!user) {
      return Err(new NotFoundError('User', id));
    }
    return Ok(user);
  } catch (error) {
    return Err(new DatabaseError('Failed to fetch user', error));
  }
}

async function updateUserProfile(
  userId: string, 
  updates: UserProfileUpdate
): Promise<Result<User, UserError>> {
  const userResult = await getUserById(userId);
  if (!userResult.success) {
    return userResult;
  }
  
  const validationResult = validateUserProfileUpdate(updates);
  if (!validationResult.success) {
    return validationResult;
  }
  
  try {
    const updatedUser = await userRepository.update(userId, updates);
    return Ok(updatedUser);
  } catch (error) {
    return Err(new DatabaseError('Failed to update user', error));
  }
}

// Chaining operations
async function getUserProfileSummary(userId: string): Promise<Result<ProfileSummary, UserError>> {
  return AsyncResult.flatMap(
    getUserById(userId),
    async (user) => {
      const profileResult = await getUserProfile(user.id);
      return AsyncResult.map(
        Promise.resolve(profileResult),
        (profile) => createProfileSummary(user, profile)
      );
    }
  );
}
```

### Python Result Pattern

```python
from typing import TypeVar, Generic, Union, Callable, List, Optional
from dataclasses import dataclass
from enum import Enum

T = TypeVar('T')
E = TypeVar('E')
U = TypeVar('U')

@dataclass(frozen=True)
class Success(Generic[T]):
    value: T
    
    def is_success(self) -> bool:
        return True
    
    def is_failure(self) -> bool:
        return False

@dataclass(frozen=True)
class Failure(Generic[E]):
    error: E
    
    def is_success(self) -> bool:
        return False
    
    def is_failure(self) -> bool:
        return True

Result = Union[Success[T], Failure[E]]

class ResultUtils:
    @staticmethod
    def ok(value: T) -> Success[T]:
        return Success(value)
    
    @staticmethod
    def err(error: E) -> Failure[E]:
        return Failure(error)
    
    @staticmethod
    def map(result: Result[T, E], func: Callable[[T], U]) -> Result[U, E]:
        if isinstance(result, Success):
            return Success(func(result.value))
        return result
    
    @staticmethod
    def flat_map(result: Result[T, E], func: Callable[[T], Result[U, E]]) -> Result[U, E]:
        if isinstance(result, Success):
            return func(result.value)
        return result
    
    @staticmethod
    def map_error(result: Result[T, E], func: Callable[[E], U]) -> Result[T, U]:
        if isinstance(result, Failure):
            return Failure(func(result.error))
        return result
    
    @staticmethod
    def combine(results: List[Result[T, E]]) -> Result[List[T], E]:
        values = []
        for result in results:
            if isinstance(result, Failure):
                return result
            values.append(result.value)
        return Success(values)
    
    @staticmethod
    def unwrap_or(result: Result[T, E], default: T) -> T:
        return result.value if isinstance(result, Success) else default
    
    @staticmethod
    def unwrap(result: Result[T, E]) -> T:
        if isinstance(result, Success):
            return result.value
        raise result.error if isinstance(result.error, Exception) else Exception(str(result.error))

# Async utilities
import asyncio

class AsyncResultUtils:
    @staticmethod
    async def from_coroutine(coro) -> Result[T, Exception]:
        try:
            value = await coro
            return Success(value)
        except Exception as e:
            return Failure(e)
    
    @staticmethod
    async def map(
        result_coro: Callable[[], Result[T, E]], 
        func: Callable[[T], U]
    ) -> Result[U, E]:
        result = await result_coro() if asyncio.iscoroutinefunction(result_coro) else result_coro()
        return ResultUtils.map(result, func)

# Custom error types
class UserError(Exception):
    pass

class ValidationError(UserError):
    def __init__(self, message: str, field: str):
        self.field = field
        super().__init__(message)

class NotFoundError(UserError):
    def __init__(self, resource: str, identifier: str):
        self.resource = resource
        self.identifier = identifier
        super().__init__(f"{resource} with id {identifier} not found")

class DatabaseError(UserError):
    def __init__(self, message: str, original_error: Exception = None):
        self.original_error = original_error
        super().__init__(message)

# Usage examples
def get_user_by_id(user_id: str) -> Result[User, UserError]:
    if not user_id:
        return ResultUtils.err(ValidationError("User ID is required", "id"))
    
    try:
        user = user_repository.find_by_id(user_id)
        if not user:
            return ResultUtils.err(NotFoundError("User", user_id))
        return ResultUtils.ok(user)
    except Exception as e:
        return ResultUtils.err(DatabaseError("Failed to fetch user", e))

def validate_email(email: str) -> Result[str, ValidationError]:
    if not email:
        return ResultUtils.err(ValidationError("Email is required", "email"))
    
    if '@' not in email:
        return ResultUtils.err(ValidationError("Invalid email format", "email"))
    
    return ResultUtils.ok(email.lower().strip())

def create_user(user_data: CreateUserData) -> Result[User, UserError]:
    # Chain validations
    email_result = validate_email(user_data.email)
    if isinstance(email_result, Failure):
        return email_result
    
    # Check for existing user
    existing_result = get_user_by_email(email_result.value)
    if isinstance(existing_result, Success):
        return ResultUtils.err(ValidationError("Email already exists", "email"))
    
    # Create user
    try:
        user = User(
            email=email_result.value,
            username=user_data.username,
            password_hash=hash_password(user_data.password)
        )
        saved_user = user_repository.create(user)
        return ResultUtils.ok(saved_user)
    except Exception as e:
        return ResultUtils.err(DatabaseError("Failed to create user", e))

# Functional chaining
def process_user_registration(data: RegistrationData) -> Result[UserProfile, UserError]:
    return ResultUtils.flat_map(
        create_user(data),
        lambda user: ResultUtils.flat_map(
            create_user_profile(user.id, data.profile_data),
            lambda profile: send_welcome_email(user.email).map(
                lambda _: UserProfile(user=user, profile=profile)
            )
        )
    )
```

### Go Result Pattern

```go
package result

import (
    "fmt"
)

// Result represents either a successful value or an error
type Result[T any] struct {
    value T
    err   error
}

// Ok creates a successful Result
func Ok[T any](value T) Result[T] {
    return Result[T]{value: value, err: nil}
}

// Err creates a failed Result
func Err[T any](err error) Result[T] {
    var zero T
    return Result[T]{value: zero, err: err}
}

// IsSuccess returns true if the result is successful
func (r Result[T]) IsSuccess() bool {
    return r.err == nil
}

// IsError returns true if the result contains an error
func (r Result[T]) IsError() bool {
    return r.err != nil
}

// Unwrap returns the value if successful, panics if error
func (r Result[T]) Unwrap() T {
    if r.err != nil {
        panic(r.err)
    }
    return r.value
}

// UnwrapOr returns the value if successful, or default if error
func (r Result[T]) UnwrapOr(defaultValue T) T {
    if r.err != nil {
        return defaultValue
    }
    return r.value
}

// Map transforms the value if successful, preserves error otherwise
func Map[T, U any](r Result[T], fn func(T) U) Result[U] {
    if r.err != nil {
        return Err[U](r.err)
    }
    return Ok(fn(r.value))
}

// FlatMap transforms the value if successful, preserves error otherwise
func FlatMap[T, U any](r Result[T], fn func(T) Result[U]) Result[U] {
    if r.err != nil {
        return Err[U](r.err)
    }
    return fn(r.value)
}

// MapError transforms the error if present, preserves value otherwise
func MapError[T any](r Result[T], fn func(error) error) Result[T] {
    if r.err != nil {
        return Err[T](fn(r.err))
    }
    return r
}

// Combine multiple results into a single result containing a slice
func Combine[T any](results ...Result[T]) Result[[]T] {
    values := make([]T, 0, len(results))
    
    for _, result := range results {
        if result.err != nil {
            return Err[[]T](result.err)
        }
        values = append(values, result.value)
    }
    
    return Ok(values)
}

// Custom error types
type ValidationError struct {
    Field   string
    Message string
}

func (e ValidationError) Error() string {
    return fmt.Sprintf("validation error on field %s: %s", e.Field, e.Message)
}

type NotFoundError struct {
    Resource string
    ID       string
}

func (e NotFoundError) Error() string {
    return fmt.Sprintf("%s with id %s not found", e.Resource, e.ID)
}

type DatabaseError struct {
    Operation string
    Cause     error
}

func (e DatabaseError) Error() string {
    return fmt.Sprintf("database error during %s: %v", e.Operation, e.Cause)
}

func (e DatabaseError) Unwrap() error {
    return e.Cause
}

// Usage examples
func GetUserByID(ctx context.Context, userID string) Result[*User] {
    if userID == "" {
        return Err[*User](ValidationError{
            Field:   "id",
            Message: "user ID is required",
        })
    }
    
    user, err := userRepository.FindByID(ctx, userID)
    if err != nil {
        return Err[*User](DatabaseError{
            Operation: "find user by ID",
            Cause:     err,
        })
    }
    
    if user == nil {
        return Err[*User](NotFoundError{
            Resource: "User",
            ID:       userID,
        })
    }
    
    return Ok(user)
}

func ValidateEmail(email string) Result[string] {
    if email == "" {
        return Err[string](ValidationError{
            Field:   "email",
            Message: "email is required",
        })
    }
    
    if !strings.Contains(email, "@") {
        return Err[string](ValidationError{
            Field:   "email",
            Message: "invalid email format",
        })
    }
    
    return Ok(strings.ToLower(strings.TrimSpace(email)))
}

func CreateUser(ctx context.Context, userData CreateUserRequest) Result[*User] {
    // Validate email
    emailResult := ValidateEmail(userData.Email)
    if emailResult.IsError() {
        return Err[*User](emailResult.err)
    }
    
    // Check for existing user
    existingUser := GetUserByEmail(ctx, emailResult.value)
    if existingUser.IsSuccess() {
        return Err[*User](ValidationError{
            Field:   "email",
            Message: "email already exists",
        })
    }
    
    // Create user
    user := &User{
        Email:        emailResult.value,
        Username:     userData.Username,
        PasswordHash: hashPassword(userData.Password),
    }
    
    if err := userRepository.Create(ctx, user); err != nil {
        return Err[*User](DatabaseError{
            Operation: "create user",
            Cause:     err,
        })
    }
    
    return Ok(user)
}

// Chaining operations
func ProcessUserRegistration(ctx context.Context, data RegistrationData) Result[*UserProfile] {
    return FlatMap(
        CreateUser(ctx, data.UserData),
        func(user *User) Result[*UserProfile] {
            return FlatMap(
                CreateUserProfile(ctx, user.ID, data.ProfileData),
                func(profile *Profile) Result[*UserProfile] {
                    return Map(
                        SendWelcomeEmail(ctx, user.Email),
                        func(_ bool) *UserProfile {
                            return &UserProfile{
                                User:    user,
                                Profile: profile,
                            }
                        },
                    )
                },
            )
        },
    )
}

// Service layer using results
type UserService struct {
    repo UserRepository
}

func (s *UserService) RegisterUser(ctx context.Context, req RegistrationRequest) Result[*User] {
    // Multiple validation steps
    validations := []Result[string]{
        ValidateEmail(req.Email),
        ValidatePassword(req.Password),
        ValidateUsername(req.Username),
    }
    
    // Combine all validations
    validationResult := Combine(validations...)
    if validationResult.IsError() {
        return Err[*User](validationResult.err)
    }
    
    return CreateUser(ctx, CreateUserRequest{
        Email:    req.Email,
        Password: req.Password,
        Username: req.Username,
    })
}

func (s *UserService) HandleRegistration(ctx context.Context, req RegistrationRequest) {
    result := s.RegisterUser(ctx, req)
    
    switch {
    case result.IsSuccess():
        user := result.Unwrap()
        log.Printf("User registered successfully: %s", user.ID)
        
    case result.IsError():
        switch err := result.err.(type) {
        case ValidationError:
            log.Printf("Validation failed: %v", err)
            // Handle validation error
            
        case NotFoundError:
            log.Printf("Resource not found: %v", err)
            // Handle not found error
            
        case DatabaseError:
            log.Printf("Database error: %v", err)
            // Handle database error
            
        default:
            log.Printf("Unknown error: %v", err)
            // Handle unknown error
        }
    }
}
```

## Best Practices

### 1. Error Type Design
```typescript
// Create specific error types for different failure modes
export abstract class AppError extends Error {
  abstract readonly code: string;
  abstract readonly statusCode: number;
  
  constructor(message: string, public readonly context?: Record<string, any>) {
    super(message);
    this.name = this.constructor.name;
  }
}

export class ValidationError extends AppError {
  readonly code = 'VALIDATION_ERROR';
  readonly statusCode = 400;
  
  constructor(message: string, public readonly field: string, context?: Record<string, any>) {
    super(message, { ...context, field });
  }
}

export class BusinessLogicError extends AppError {
  readonly code = 'BUSINESS_LOGIC_ERROR';
  readonly statusCode = 422;
}

export class ExternalServiceError extends AppError {
  readonly code = 'EXTERNAL_SERVICE_ERROR';
  readonly statusCode = 502;
  
  constructor(
    message: string, 
    public readonly service: string,
    public readonly originalError?: Error,
    context?: Record<string, any>
  ) {
    super(message, { ...context, service, originalError: originalError?.message });
  }
}
```

### 2. Early Returns Pattern
```typescript
async function processPayment(paymentData: PaymentData): Promise<Result<Payment, PaymentError>> {
  // Validate input early
  const validationResult = validatePaymentData(paymentData);
  if (!validationResult.success) {
    return validationResult;
  }
  
  // Check user permissions early
  const userResult = await getCurrentUser();
  if (!userResult.success) {
    return Err(new AuthenticationError('User not authenticated'));
  }
  
  const user = userResult.data;
  if (!user.canMakePayments) {
    return Err(new AuthorizationError('User cannot make payments'));
  }
  
  // Process payment
  const paymentResult = await paymentGateway.process(paymentData);
  if (!paymentResult.success) {
    return Err(new PaymentProcessingError(
      'Payment failed', 
      paymentResult.error.code
    ));
  }
  
  return Ok(paymentResult.data);
}
```

### 3. Result Conversion Utilities
```python
# Convert between Result and traditional exception handling
def try_to_result(func: Callable[[], T]) -> Result[T, Exception]:
    """Convert a function that may throw to Result."""
    try:
        return ResultUtils.ok(func())
    except Exception as e:
        return ResultUtils.err(e)

def result_to_optional(result: Result[T, E]) -> Optional[T]:
    """Convert Result to Optional, discarding error information."""
    return result.value if isinstance(result, Success) else None

# Async version
async def async_try_to_result(coro) -> Result[T, Exception]:
    """Convert a coroutine that may throw to Result."""
    try:
        return ResultUtils.ok(await coro)
    except Exception as e:
        return ResultUtils.err(e)

# Usage
user_result = try_to_result(lambda: expensive_user_lookup(user_id))
user_optional = result_to_optional(user_result)
```

### 4. Testing Result-Based Code
```typescript
describe('User Service', () => {
  it('should return validation error for invalid email', async () => {
    const result = await userService.createUser({
      email: 'invalid-email',
      username: 'testuser',
      password: 'password123'
    });
    
    expect(result.success).toBe(false);
    if (!result.success) {
      expect(result.error).toBeInstanceOf(ValidationError);
      expect((result.error as ValidationError).field).toBe('email');
    }
  });
  
  it('should create user successfully with valid data', async () => {
    const result = await userService.createUser({
      email: 'test@example.com',
      username: 'testuser',
      password: 'password123'
    });
    
    expect(result.success).toBe(true);
    if (result.success) {
      expect(result.data.email).toBe('test@example.com');
      expect(result.data.id).toBeDefined();
    }
  });
});
```