# TypeScript Code Formatting Standards

## Prettier Configuration

Use Prettier with these settings in `.prettierrc.json`:

```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "bracketSpacing": true,
  "bracketSameLine": false,
  "arrowParens": "avoid",
  "endOfLine": "lf"
}
```

## ESLint Configuration

Configure ESLint in `.eslintrc.json`:

```json
{
  "extends": [
    "@typescript-eslint/recommended",
    "@typescript-eslint/recommended-requiring-type-checking",
    "prettier"
  ],
  "plugins": ["@typescript-eslint"],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 2022,
    "sourceType": "module",
    "project": "./tsconfig.json"
  },
  "rules": {
    "@typescript-eslint/no-unused-vars": "error",
    "@typescript-eslint/no-explicit-any": "warn",
    "@typescript-eslint/explicit-function-return-type": "warn",
    "@typescript-eslint/prefer-readonly": "error",
    "prefer-const": "error",
    "no-var": "error"
  }
}
```

## Code Structure Standards

### File and Export Organization
```typescript
// Standard order:
// 1. Type imports
// 2. Value imports (external libraries)
// 3. Relative imports
// 4. Type definitions
// 5. Constants
// 6. Main code
// 7. Default export (if applicable)

import type { User, UserRole } from './types';
import { Request, Response } from 'express';
import { ValidationError } from 'joi';

import { userService } from '../services/userService';
import { logger } from '../utils/logger';

export interface CreateUserRequest {
  name: string;
  email: string;
  role: UserRole;
}

export interface UserResponse {
  id: string;
  name: string;
  email: string;
  createdAt: Date;
}

const DEFAULT_PAGE_SIZE = 20;
const MAX_USERNAME_LENGTH = 50;

export class UserController {
  constructor(private readonly service: UserService) {}
  
  async createUser(req: Request, res: Response): Promise<void> {
    // Implementation
  }
}

export default UserController;
```

### Function and Class Layout
```typescript
export class UserService {
  private readonly repository: UserRepository;
  private readonly cache: Map<string, User> = new Map();

  constructor(repository: UserRepository) {
    this.repository = repository;
  }

  async findUser(id: string): Promise<User | null> {
    const cached = this.cache.get(id);
    if (cached) {
      return cached;
    }

    const user = await this.repository.findById(id);
    if (user) {
      this.cache.set(id, user);
    }
    
    return user;
  }

  async createUser(userData: CreateUserData): Promise<User> {
    this.validateUserData(userData);
    
    const user = await this.repository.create(userData);
    this.cache.set(user.id, user);
    
    return user;
  }

  private validateUserData(data: CreateUserData): void {
    // Validation logic
  }
}
```

## Naming Conventions

### Variables and Functions
```typescript
// camelCase for variables and functions
const userCount = 0;
const isActive = true;
const hasPermission = false;

function calculateTotalPrice(): number {
  return 0;
}

function getUserById(userId: string): Promise<User | null> {
  return Promise.resolve(null);
}

// Arrow functions for callbacks and short functions
const users = data.map(item => transformToUser(item));
const activeUsers = users.filter(user => user.isActive);
```

### Types and Interfaces
```typescript
// PascalCase for types, interfaces, classes, enums
interface UserProfile {
  id: string;
  name: string;
}

type PaymentStatus = 'pending' | 'completed' | 'failed';

class UserManager {
  // Implementation
}

enum OrderStatus {
  PENDING = 'pending',
  PROCESSING = 'processing',
  COMPLETED = 'completed',
  CANCELLED = 'cancelled',
}
```

### Constants
```typescript
// UPPER_SNAKE_CASE for module-level constants
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = 'https://api.example.com';
const DEFAULT_PAGE_SIZE = 20;

// Regular camelCase for local constants
function processData() {
  const maxItems = 100;
  const timeoutMs = 5000;
}
```

### Private Members
```typescript
class UserService {
  private readonly connection: Database;
  private cache: Map<string, User> = new Map();
  
  // Use # for truly private fields (ES2022+)
  #secretKey: string = 'secret';
  
  private internalMethod(): void {
    // Private method
  }
  
  public async getUser(id: string): Promise<User | null> {
    return this.cache.get(id) ?? null;
  }
}
```

## Type Definitions

### Interface vs Type Aliases
```typescript
// Use interfaces for object shapes that might be extended
interface BaseUser {
  id: string;
  name: string;
  email: string;
}

interface AdminUser extends BaseUser {
  permissions: string[];
  lastLogin: Date;
}

// Use type aliases for unions, primitives, computed types
type Status = 'active' | 'inactive' | 'suspended';
type UserId = string;
type EventHandler<T> = (event: T) => void;

// Use type aliases for utility types
type PartialUser = Partial<BaseUser>;
type UserEmail = Pick<BaseUser, 'email'>;
```

### Generic Types
```typescript
// Generic interfaces and types
interface Repository<T> {
  findById(id: string): Promise<T | null>;
  save(entity: T): Promise<T>;
  delete(id: string): Promise<void>;
}

type ApiResponse<T> = {
  success: true;
  data: T;
} | {
  success: false;
  error: string;
};

// Generic functions
function createRepository<T>(
  entityType: new () => T
): Repository<T> {
  // Implementation
}
```

### Strict Type Checking
```typescript
// Avoid 'any', use specific types
interface UnknownApiResponse {
  [key: string]: unknown;
}

// Use type assertions carefully
function processApiResponse(response: unknown): User {
  // Type guard
  if (isUserResponse(response)) {
    return response.user;
  }
  throw new Error('Invalid response');
}

function isUserResponse(obj: unknown): obj is { user: User } {
  return (
    typeof obj === 'object' &&
    obj !== null &&
    'user' in obj
  );
}
```

## String and Template Handling

### Template Literals
```typescript
// Prefer template literals over concatenation
const message = `User ${name} has ${count} items`;

// Good for multiline strings
const query = `
  SELECT u.id, u.name, u.email
  FROM users u
  WHERE u.active = true
    AND u.created_at > $1
  ORDER BY u.name
`;

// Use tagged templates for special formatting
const sql = SQL`
  SELECT * FROM users 
  WHERE id = ${userId}
`;
```

## Error Handling Patterns

### Result Pattern
```typescript
type Result<T, E = Error> = {
  success: true;
  data: T;
} | {
  success: false;
  error: E;
};

async function safeFetchUser(id: string): Promise<Result<User>> {
  try {
    const user = await userService.findById(id);
    return { success: true, data: user };
  } catch (error) {
    return { 
      success: false, 
      error: error instanceof Error ? error : new Error(String(error))
    };
  }
}
```

### Custom Error Types
```typescript
abstract class AppError extends Error {
  abstract readonly code: string;
  abstract readonly statusCode: number;
}

class ValidationError extends AppError {
  readonly code = 'VALIDATION_ERROR';
  readonly statusCode = 400;
  
  constructor(
    message: string,
    public readonly field: string
  ) {
    super(message);
    this.name = 'ValidationError';
  }
}

class NotFoundError extends AppError {
  readonly code = 'NOT_FOUND';
  readonly statusCode = 404;
  
  constructor(resource: string, id: string) {
    super(`${resource} with id ${id} not found`);
    this.name = 'NotFoundError';
  }
}
```

## Async/Await Standards

### Promise Handling
```typescript
// Good - explicit error handling
async function updateUser(id: string, data: UserUpdateData): Promise<User> {
  try {
    const user = await userRepository.findById(id);
    if (!user) {
      throw new NotFoundError('User', id);
    }
    
    const updated = await userRepository.update(id, data);
    await auditLogger.logUserUpdate(id, data);
    
    return updated;
  } catch (error) {
    logger.error('Failed to update user', { userId: id, error });
    throw error;
  }
}

// Good - concurrent operations
async function getUserWithProfile(id: string): Promise<UserWithProfile> {
  const [user, profile] = await Promise.all([
    userService.findById(id),
    profileService.findByUserId(id),
  ]);
  
  return { ...user, profile };
}
```

### Function Return Types
```typescript
// Always specify return types for public functions
async function createUser(data: CreateUserData): Promise<User> {
  // Implementation
}

function validateEmail(email: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// Use void for functions that don't return values
function logUserAction(userId: string, action: string): void {
  logger.info(`User ${userId} performed ${action}`);
}
```