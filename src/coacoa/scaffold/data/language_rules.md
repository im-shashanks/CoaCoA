# CoaCoA Language Rules & Standards

## Purpose
This document provides language-specific guidance for AI coding assistants to ensure consistent, idiomatic, and maintainable code generation across different programming languages.

---

## Python

### Type Hints & Documentation
- **Always use type hints** for function parameters, return values, and class attributes
- Use `typing` module for complex types: `List[str]`, `Dict[str, int]`, `Optional[T]`
- For Python 3.9+, prefer built-in generics: `list[str]`, `dict[str, int]`
- **Docstrings required** for all public functions/classes (Google style preferred)

```python
def process_user_data(users: list[dict[str, Any]]) -> tuple[int, list[str]]:
    """Process user data and return statistics.
    
    Args:
        users: List of user dictionaries containing user information
        
    Returns:
        Tuple of (total_count, user_names)
        
    Raises:
        ValueError: If user data is malformed
    """
```

### Exception Handling
- Use specific exception types, avoid bare `except:`
- Create custom exceptions for domain-specific errors
- Use `raise ... from e` for exception chaining

```python
class UserNotFoundError(Exception):
    """Raised when user cannot be found in the system."""
    pass

try:
    user = get_user(user_id)
except DatabaseError as e:
    raise UserNotFoundError(f"User {user_id} not found") from e
```

### Code Organization
- Max function length: 50 lines
- Max class length: 500 lines  
- Use `__all__` in modules to define public API
- Group imports: stdlib, third-party, local (with blank lines between)

### Naming Conventions
- Functions/variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private members: prefix with single underscore `_private`

---

## TypeScript

### Type Safety
- **Enable strict mode** in tsconfig.json
- Avoid `any` type - use `unknown` or specific unions instead
- Use interfaces for object shapes, types for unions/primitives
- Prefer `readonly` for immutable data structures

```typescript
interface UserProfile {
  readonly id: string;
  name: string;
  email: string;
  roles: readonly string[];
}

type ApiResponse<T> = {
  success: true;
  data: T;
} | {
  success: false;
  error: string;
};
```

### Async Patterns
- Use `async/await` over Promises for readability
- Handle errors with try/catch blocks
- Use `Promise.allSettled()` for concurrent operations that may fail

```typescript
async function fetchUserProfiles(userIds: string[]): Promise<UserProfile[]> {
  try {
    const responses = await Promise.allSettled(
      userIds.map(id => api.getUser(id))
    );
    
    return responses
      .filter((result): result is PromiseFulfilledResult<UserProfile> => 
        result.status === 'fulfilled')
      .map(result => result.value);
  } catch (error) {
    throw new Error(`Failed to fetch user profiles: ${error.message}`);
  }
}
```

### Error Handling
- Use discriminated unions for error states
- Create typed error classes with specific error codes
- Use Result pattern for operations that can fail

```typescript
class ValidationError extends Error {
  constructor(
    message: string,
    public readonly field: string,
    public readonly code: 'REQUIRED' | 'INVALID_FORMAT' | 'TOO_LONG'
  ) {
    super(message);
    this.name = 'ValidationError';
  }
}
```

### Code Organization
- Max function length: 30 lines
- Use barrel exports (`index.ts`) for clean module structure
- Group related functions into classes or namespaces
- Separate types into `.types.ts` files for complex domains

---

## Java

### Modern Java Practices
- Use `var` for local variables when type is obvious
- Prefer records for data classes (Java 14+)
- Use sealed classes for restricted inheritance (Java 17+)
- Utilize pattern matching where available

```java
public record UserDto(String id, String name, String email) {}

public sealed interface PaymentMethod 
    permits CreditCard, BankTransfer, DigitalWallet {}

public record CreditCard(String number, String expiryDate) 
    implements PaymentMethod {}
```

### Exception Handling
- Use specific exception types from the standard library
- Create custom unchecked exceptions for business logic errors
- Use try-with-resources for resource management

```java
public class UserNotFoundException extends RuntimeException {
    public UserNotFoundException(String userId) {
        super("User not found: " + userId);
    }
}

public User findUser(String userId) throws UserNotFoundException {
    return userRepository.findById(userId)
        .orElseThrow(() -> new UserNotFoundException(userId));
}
```

### Null Safety & Optionals
- Use `Optional<T>` for potentially null values
- Never call `Optional.get()` without checking `isPresent()`
- Use `@NonNull` and `@Nullable` annotations

```java
public Optional<User> findUserByEmail(String email) {
    return userRepository.findByEmail(email);
}

public String getUserDisplayName(@NonNull User user) {
    return Optional.ofNullable(user.getDisplayName())
        .orElse(user.getUsername());
}
```

### Code Organization
- Max method length: 40 lines
- Use package-private classes when possible
- Follow single responsibility principle strictly
- Group related classes in packages, not single large classes

---

## Go

### Error Handling
- Always check errors explicitly, never ignore
- Create custom error types for different error categories
- Use error wrapping with `fmt.Errorf("%w", err)` for context

```go
type ValidationError struct {
    Field   string
    Message string
}

func (e *ValidationError) Error() string {
    return fmt.Sprintf("validation error on field %s: %s", e.Field, e.Message)
}

func processUser(user *User) error {
    if err := validateUser(user); err != nil {
        return fmt.Errorf("failed to process user %s: %w", user.ID, err)
    }
    return nil
}
```

### Interface Design
- Keep interfaces small and focused (1-3 methods)
- Define interfaces at the point of use, not implementation
- Use composition over inheritance

```go
type UserReader interface {
    GetUser(ctx context.Context, id string) (*User, error)
}

type UserWriter interface {
    SaveUser(ctx context.Context, user *User) error
}

type UserService interface {
    UserReader
    UserWriter
}
```

### Concurrency Patterns
- Use channels for communication, mutexes for shared state
- Always use context.Context for cancellation
- Prefer sync.Pool for object reuse in hot paths

```go
func processUsers(ctx context.Context, userIDs []string) error {
    const maxConcurrency = 10
    sem := make(chan struct{}, maxConcurrency)
    errCh := make(chan error, len(userIDs))
    
    for _, id := range userIDs {
        go func(userID string) {
            sem <- struct{}{}
            defer func() { <-sem }()
            
            if err := processUser(ctx, userID); err != nil {
                errCh <- fmt.Errorf("failed to process user %s: %w", userID, err)
                return
            }
            errCh <- nil
        }(id)
    }
    
    for range userIDs {
        if err := <-errCh; err != nil {
            return err
        }
    }
    return nil
}
```

### Code Organization
- Max function length: 50 lines
- Use meaningful package names (avoid `utils`, `common`)
- Keep package dependencies minimal and acyclic
- Use internal packages for implementation details

---

## General Rules (All Languages)

### Naming Conventions
- Use descriptive names that explain intent
- Avoid abbreviations unless widely understood
- Use consistent terminology throughout the codebase
- Boolean variables should start with `is`, `has`, `can`, `should`

### Comments & Documentation
- Write comments that explain WHY, not WHAT
- Update comments when code changes
- Use TODO comments sparingly and include owner/date
- Document complex algorithms and business logic

### Performance Considerations
- Avoid premature optimization
- Use appropriate data structures for the use case
- Cache expensive computations when beneficial
- Consider memory allocation patterns in hot paths

### Testing Guidelines
- Write tests for public APIs and business logic
- Use descriptive test names that explain the scenario
- Follow AAA pattern: Arrange, Act, Assert
- Test edge cases and error conditions