# Database Repository Patterns

## Overview
Repository patterns provide a consistent interface for data access operations, abstracting database implementation details and making code more testable and maintainable.

## Basic Repository Pattern

### Python (SQLAlchemy)

```python
from abc import ABC, abstractmethod
from typing import List, Optional, Generic, TypeVar
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc, asc

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    """Abstract base repository with common CRUD operations."""
    
    def __init__(self, db_session: Session, model_class: type[T]):
        self.db = db_session
        self.model_class = model_class
    
    def create(self, entity: T) -> T:
        """Create a new entity."""
        self.db.add(entity)
        self.db.commit()
        self.db.refresh(entity)
        return entity
    
    def get_by_id(self, entity_id: int) -> Optional[T]:
        """Retrieve entity by ID."""
        return self.db.query(self.model_class).filter(
            self.model_class.id == entity_id
        ).first()
    
    def get_all(self, offset: int = 0, limit: int = 100) -> List[T]:
        """Retrieve all entities with pagination."""
        return self.db.query(self.model_class).offset(offset).limit(limit).all()
    
    def update(self, entity: T) -> T:
        """Update an existing entity."""
        self.db.commit()
        self.db.refresh(entity)
        return entity
    
    def delete(self, entity_id: int) -> bool:
        """Delete entity by ID."""
        entity = self.get_by_id(entity_id)
        if entity:
            self.db.delete(entity)
            self.db.commit()
            return True
        return False
    
    def count(self) -> int:
        """Count total entities."""
        return self.db.query(self.model_class).count()

class UserRepository(BaseRepository[User]):
    """User-specific repository with custom queries."""
    
    def __init__(self, db_session: Session):
        super().__init__(db_session, User)
    
    def find_by_email(self, email: str) -> Optional[User]:
        """Find user by email address."""
        return self.db.query(User).filter(User.email == email).first()
    
    def find_by_username(self, username: str) -> Optional[User]:
        """Find user by username."""
        return self.db.query(User).filter(User.username == username).first()
    
    def find_active_users(self, limit: int = 50) -> List[User]:
        """Find active users ordered by last login."""
        return (
            self.db.query(User)
            .filter(User.is_active == True)
            .order_by(desc(User.last_login))
            .limit(limit)
            .all()
        )
    
    def search_users(
        self, 
        query: str, 
        offset: int = 0, 
        limit: int = 20
    ) -> List[User]:
        """Search users by name or email."""
        search_filter = or_(
            User.name.ilike(f"%{query}%"),
            User.email.ilike(f"%{query}%")
        )
        
        return (
            self.db.query(User)
            .filter(search_filter)
            .offset(offset)
            .limit(limit)
            .all()
        )
    
    def get_users_by_role(self, role: str) -> List[User]:
        """Get all users with a specific role."""
        return self.db.query(User).filter(User.role == role).all()
    
    def bulk_update_last_login(self, user_ids: List[int]) -> None:
        """Bulk update last login timestamp for multiple users."""
        self.db.query(User).filter(
            User.id.in_(user_ids)
        ).update(
            {User.last_login: datetime.utcnow()},
            synchronize_session=False
        )
        self.db.commit()

# Usage with dependency injection
class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo
    
    async def register_user(self, user_data: CreateUserData) -> User:
        # Check if user already exists
        existing = self.user_repo.find_by_email(user_data.email)
        if existing:
            raise ValueError("User with this email already exists")
        
        # Create new user
        user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=hash_password(user_data.password)
        )
        
        return self.user_repo.create(user)
```

### TypeScript (TypeORM)

```typescript
import { Repository, EntityRepository, SelectQueryBuilder } from 'typeorm';
import { User } from '../entities/User';

export interface IUserRepository {
  findById(id: string): Promise<User | null>;
  findByEmail(email: string): Promise<User | null>;
  findByUsername(username: string): Promise<User | null>;
  create(userData: Partial<User>): Promise<User>;
  update(id: string, userData: Partial<User>): Promise<User>;
  delete(id: string): Promise<boolean>;
  findActiveUsers(limit?: number): Promise<User[]>;
  searchUsers(query: string, offset?: number, limit?: number): Promise<User[]>;
}

@EntityRepository(User)
export class UserRepository extends Repository<User> implements IUserRepository {
  
  async findById(id: string): Promise<User | null> {
    return this.findOne({ where: { id } });
  }
  
  async findByEmail(email: string): Promise<User | null> {
    return this.findOne({ where: { email } });
  }
  
  async findByUsername(username: string): Promise<User | null> {
    return this.findOne({ where: { username } });
  }
  
  async create(userData: Partial<User>): Promise<User> {
    const user = this.create(userData);
    return this.save(user);
  }
  
  async update(id: string, userData: Partial<User>): Promise<User> {
    await this.update(id, userData);
    const updatedUser = await this.findById(id);
    if (!updatedUser) {
      throw new Error('User not found after update');
    }
    return updatedUser;
  }
  
  async delete(id: string): Promise<boolean> {
    const result = await this.delete(id);
    return (result.affected ?? 0) > 0;
  }
  
  async findActiveUsers(limit: number = 50): Promise<User[]> {
    return this.find({
      where: { isActive: true },
      order: { lastLogin: 'DESC' },
      take: limit
    });
  }
  
  async searchUsers(
    query: string, 
    offset: number = 0, 
    limit: number = 20
  ): Promise<User[]> {
    return this.createQueryBuilder('user')
      .where('user.name ILIKE :query OR user.email ILIKE :query', {
        query: `%${query}%`
      })
      .skip(offset)
      .take(limit)
      .getMany();
  }
  
  async getUsersWithProfile(): Promise<User[]> {
    return this.createQueryBuilder('user')
      .leftJoinAndSelect('user.profile', 'profile')
      .where('user.isActive = :active', { active: true })
      .getMany();
  }
  
  async getUserStatsByRole(): Promise<Array<{ role: string; count: number }>> {
    return this.createQueryBuilder('user')
      .select('user.role', 'role')
      .addSelect('COUNT(*)', 'count')
      .groupBy('user.role')
      .getRawMany();
  }
  
  // Complex query with joins and filtering
  async findUsersWithRecentActivity(days: number = 30): Promise<User[]> {
    const cutoffDate = new Date();
    cutoffDate.setDate(cutoffDate.getDate() - days);
    
    return this.createQueryBuilder('user')
      .leftJoin('user.activities', 'activity')
      .where('activity.createdAt > :cutoff', { cutoff: cutoffDate })
      .distinctOn(['user.id'])
      .orderBy('user.id')
      .addOrderBy('activity.createdAt', 'DESC')
      .getMany();
  }
}

// Service layer using the repository
export class UserService {
  constructor(
    private readonly userRepository: IUserRepository
  ) {}
  
  async createUser(userData: CreateUserRequest): Promise<User> {
    // Validate uniqueness
    const existingUser = await this.userRepository.findByEmail(userData.email);
    if (existingUser) {
      throw new ValidationError('Email already exists', 'email');
    }
    
    // Create user
    const user = await this.userRepository.create({
      ...userData,
      id: generateId(),
      createdAt: new Date(),
      isActive: true
    });
    
    return user;
  }
  
  async getUserProfile(userId: string): Promise<User> {
    const user = await this.userRepository.findById(userId);
    if (!user) {
      throw new NotFoundError('User', userId);
    }
    return user;
  }
}
```

### Go (GORM)

```go
package repository

import (
    "context"
    "fmt"
    
    "gorm.io/gorm"
)

type User struct {
    ID       uint   `gorm:"primaryKey"`
    Username string `gorm:"uniqueIndex;not null"`
    Email    string `gorm:"uniqueIndex;not null"`
    IsActive bool   `gorm:"default:true"`
    Role     string `gorm:"default:user"`
}

type UserRepository interface {
    Create(ctx context.Context, user *User) error
    GetByID(ctx context.Context, id uint) (*User, error)
    GetByEmail(ctx context.Context, email string) (*User, error)
    GetByUsername(ctx context.Context, username string) (*User, error)
    Update(ctx context.Context, user *User) error
    Delete(ctx context.Context, id uint) error
    FindActiveUsers(ctx context.Context, limit int) ([]User, error)
    SearchUsers(ctx context.Context, query string, offset, limit int) ([]User, error)
    Count(ctx context.Context) (int64, error)
}

type userRepository struct {
    db *gorm.DB
}

func NewUserRepository(db *gorm.DB) UserRepository {
    return &userRepository{db: db}
}

func (r *userRepository) Create(ctx context.Context, user *User) error {
    return r.db.WithContext(ctx).Create(user).Error
}

func (r *userRepository) GetByID(ctx context.Context, id uint) (*User, error) {
    var user User
    err := r.db.WithContext(ctx).First(&user, id).Error
    if err != nil {
        if err == gorm.ErrRecordNotFound {
            return nil, nil
        }
        return nil, fmt.Errorf("failed to get user by ID: %w", err)
    }
    return &user, nil
}

func (r *userRepository) GetByEmail(ctx context.Context, email string) (*User, error) {
    var user User
    err := r.db.WithContext(ctx).Where("email = ?", email).First(&user).Error
    if err != nil {
        if err == gorm.ErrRecordNotFound {
            return nil, nil
        }
        return nil, fmt.Errorf("failed to get user by email: %w", err)
    }
    return &user, nil
}

func (r *userRepository) GetByUsername(ctx context.Context, username string) (*User, error) {
    var user User
    err := r.db.WithContext(ctx).Where("username = ?", username).First(&user).Error
    if err != nil {
        if err == gorm.ErrRecordNotFound {
            return nil, nil
        }
        return nil, fmt.Errorf("failed to get user by username: %w", err)
    }
    return &user, nil
}

func (r *userRepository) Update(ctx context.Context, user *User) error {
    return r.db.WithContext(ctx).Save(user).Error
}

func (r *userRepository) Delete(ctx context.Context, id uint) error {
    result := r.db.WithContext(ctx).Delete(&User{}, id)
    if result.Error != nil {
        return fmt.Errorf("failed to delete user: %w", result.Error)
    }
    if result.RowsAffected == 0 {
        return gorm.ErrRecordNotFound
    }
    return nil
}

func (r *userRepository) FindActiveUsers(ctx context.Context, limit int) ([]User, error) {
    var users []User
    err := r.db.WithContext(ctx).
        Where("is_active = ?", true).
        Order("created_at desc").
        Limit(limit).
        Find(&users).Error
    
    if err != nil {
        return nil, fmt.Errorf("failed to find active users: %w", err)
    }
    return users, nil
}

func (r *userRepository) SearchUsers(
    ctx context.Context, 
    query string, 
    offset, limit int,
) ([]User, error) {
    var users []User
    searchPattern := "%" + query + "%"
    
    err := r.db.WithContext(ctx).
        Where("username ILIKE ? OR email ILIKE ?", searchPattern, searchPattern).
        Offset(offset).
        Limit(limit).
        Find(&users).Error
    
    if err != nil {
        return nil, fmt.Errorf("failed to search users: %w", err)
    }
    return users, nil
}

func (r *userRepository) Count(ctx context.Context) (int64, error) {
    var count int64
    err := r.db.WithContext(ctx).Model(&User{}).Count(&count).Error
    if err != nil {
        return 0, fmt.Errorf("failed to count users: %w", err)
    }
    return count, nil
}

// Advanced queries
func (r *userRepository) FindUsersWithRoleCount(ctx context.Context) (map[string]int64, error) {
    type RoleCount struct {
        Role  string
        Count int64
    }
    
    var roleCounts []RoleCount
    err := r.db.WithContext(ctx).
        Model(&User{}).
        Select("role, count(*) as count").
        Group("role").
        Scan(&roleCounts).Error
    
    if err != nil {
        return nil, fmt.Errorf("failed to get role counts: %w", err)
    }
    
    result := make(map[string]int64)
    for _, rc := range roleCounts {
        result[rc.Role] = rc.Count
    }
    
    return result, nil
}

// Service using the repository
type UserService struct {
    userRepo UserRepository
}

func NewUserService(userRepo UserRepository) *UserService {
    return &UserService{
        userRepo: userRepo,
    }
}

func (s *UserService) CreateUser(ctx context.Context, req CreateUserRequest) (*User, error) {
    // Check if user already exists
    existingUser, err := s.userRepo.GetByEmail(ctx, req.Email)
    if err != nil {
        return nil, fmt.Errorf("failed to check existing user: %w", err)
    }
    if existingUser != nil {
        return nil, ErrUserAlreadyExists
    }
    
    // Create new user
    user := &User{
        Username: req.Username,
        Email:    req.Email,
        Role:     req.Role,
        IsActive: true,
    }
    
    if err := s.userRepo.Create(ctx, user); err != nil {
        return nil, fmt.Errorf("failed to create user: %w", err)
    }
    
    return user, nil
}
```

## Advanced Patterns

### Unit of Work Pattern

```python
from contextlib import contextmanager
from typing import List, Any

class UnitOfWork:
    """Unit of Work pattern for managing database transactions."""
    
    def __init__(self, session_factory):
        self.session_factory = session_factory
        self._repositories = {}
    
    def __enter__(self):
        self.session = self.session_factory()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.rollback()
        self.session.close()
    
    def commit(self):
        self.session.commit()
    
    def rollback(self):
        self.session.rollback()
    
    @property
    def users(self) -> UserRepository:
        if 'users' not in self._repositories:
            self._repositories['users'] = UserRepository(self.session)
        return self._repositories['users']
    
    @property
    def orders(self) -> OrderRepository:
        if 'orders' not in self._repositories:
            self._repositories['orders'] = OrderRepository(self.session)
        return self._repositories['orders']

# Usage
def transfer_order_to_user(user_id: int, order_id: int):
    with UnitOfWork(session_factory) as uow:
        user = uow.users.get_by_id(user_id)
        order = uow.orders.get_by_id(order_id)
        
        if not user or not order:
            raise ValueError("User or order not found")
        
        # Business logic
        order.user_id = user_id
        order.status = "assigned"
        user.order_count += 1
        
        # Both updates happen in the same transaction
        uow.orders.update(order)
        uow.users.update(user)
        uow.commit()
```

### Repository with Specifications

```typescript
// Specification pattern for complex queries
export abstract class Specification<T> {
  abstract isSatisfiedBy(entity: T): boolean;
  abstract toSqlQuery(): string;
  
  and(other: Specification<T>): Specification<T> {
    return new AndSpecification(this, other);
  }
  
  or(other: Specification<T>): Specification<T> {
    return new OrSpecification(this, other);
  }
}

export class ActiveUserSpecification extends Specification<User> {
  isSatisfiedBy(user: User): boolean {
    return user.isActive === true;
  }
  
  toSqlQuery(): string {
    return "is_active = true";
  }
}

export class UserRoleSpecification extends Specification<User> {
  constructor(private role: string) {
    super();
  }
  
  isSatisfiedBy(user: User): boolean {
    return user.role === this.role;
  }
  
  toSqlQuery(): string {
    return `role = '${this.role}'`;
  }
}

// Enhanced repository with specifications
export class SpecificationUserRepository extends UserRepository {
  async findBySpecification(spec: Specification<User>): Promise<User[]> {
    return this.createQueryBuilder('user')
      .where(spec.toSqlQuery())
      .getMany();
  }
}

// Usage
const activeAdmins = await userRepository.findBySpecification(
  new ActiveUserSpecification().and(new UserRoleSpecification('admin'))
);
```

## Best Practices

### Error Handling
```python
class RepositoryError(Exception):
    """Base exception for repository errors."""
    pass

class EntityNotFoundError(RepositoryError):
    """Raised when entity is not found."""
    def __init__(self, entity_type: str, entity_id: Any):
        self.entity_type = entity_type
        self.entity_id = entity_id
        super().__init__(f"{entity_type} with id {entity_id} not found")

class DuplicateEntityError(RepositoryError):
    """Raised when attempting to create duplicate entity."""
    pass

# Use in repository methods
def get_by_id(self, entity_id: int) -> T:
    entity = self.db.query(self.model_class).filter(
        self.model_class.id == entity_id
    ).first()
    
    if not entity:
        raise EntityNotFoundError(self.model_class.__name__, entity_id)
    
    return entity
```

### Connection Management
```go
// Repository with connection pooling and timeout handling
type repositoryWithTimeout struct {
    db      *gorm.DB
    timeout time.Duration
}

func (r *repositoryWithTimeout) GetByID(ctx context.Context, id uint) (*User, error) {
    ctx, cancel := context.WithTimeout(ctx, r.timeout)
    defer cancel()
    
    var user User
    err := r.db.WithContext(ctx).First(&user, id).Error
    if err != nil {
        if err == context.DeadlineExceeded {
            return nil, ErrQueryTimeout
        }
        if err == gorm.ErrRecordNotFound {
            return nil, ErrUserNotFound
        }
        return nil, fmt.Errorf("database error: %w", err)
    }
    return &user, nil
}
```