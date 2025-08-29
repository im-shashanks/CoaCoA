# JWT Authentication Patterns

## Overview
JSON Web Tokens (JWT) are a secure way to transmit information between parties. This guide provides patterns for implementing JWT authentication across different languages and frameworks.

## Token Structure

### JWT Payload Standard
```json
{
  "sub": "user123",           // Subject (user ID)
  "iat": 1642694400,         // Issued at (timestamp)
  "exp": 1642697400,         // Expiration (timestamp)  
  "aud": "your-app",         // Audience
  "iss": "your-auth-service", // Issuer
  "jti": "token-id-123",     // JWT ID (for revocation)
  "role": "user",            // User role
  "permissions": ["read", "write"] // User permissions
}
```

## Implementation Patterns

### Python (FastAPI)

```python
from datetime import datetime, timedelta
from typing import Optional, List
import jwt
from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

class JWTManager:
    def __init__(self, secret_key: str, algorithm: str = "HS256"):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.bearer = HTTPBearer()
    
    def create_access_token(
        self, 
        user_id: str, 
        role: str,
        permissions: List[str],
        expires_delta: Optional[timedelta] = None
    ) -> str:
        """Create a new access token."""
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(hours=1)
            
        payload = {
            "sub": user_id,
            "iat": datetime.utcnow(),
            "exp": expire,
            "aud": "your-app",
            "iss": "your-auth-service",
            "role": role,
            "permissions": permissions
        }
        
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def create_refresh_token(self, user_id: str) -> str:
        """Create a refresh token (longer expiry, fewer claims)."""
        payload = {
            "sub": user_id,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(days=30),
            "type": "refresh"
        }
        
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)
    
    def verify_token(self, token: str) -> dict:
        """Verify and decode a token."""
        try:
            payload = jwt.decode(
                token, 
                self.secret_key, 
                algorithms=[self.algorithm],
                audience="your-app",
                issuer="your-auth-service"
            )
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
    
    async def get_current_user(
        self, 
        credentials: HTTPAuthorizationCredentials = Depends(bearer)
    ) -> dict:
        """FastAPI dependency to get current user from token."""
        return self.verify_token(credentials.credentials)

# Usage in FastAPI routes
jwt_manager = JWTManager("your-secret-key")

@app.post("/login")
async def login(credentials: LoginCredentials):
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = jwt_manager.create_access_token(
        user_id=user.id,
        role=user.role,
        permissions=user.permissions
    )
    refresh_token = jwt_manager.create_refresh_token(user.id)
    
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }

@app.get("/protected")
async def protected_route(
    current_user: dict = Depends(jwt_manager.get_current_user)
):
    return {"message": f"Hello {current_user['sub']}"}
```

### TypeScript (Express)

```typescript
import jwt from 'jsonwebtoken';
import { Request, Response, NextFunction } from 'express';

export interface JWTPayload {
  sub: string;
  iat: number;
  exp: number;
  aud: string;
  iss: string;
  role: string;
  permissions: string[];
}

export interface AuthenticatedRequest extends Request {
  user?: JWTPayload;
}

export class JWTService {
  private readonly secretKey: string;
  private readonly algorithm = 'HS256';
  
  constructor(secretKey: string) {
    this.secretKey = secretKey;
  }
  
  createAccessToken(
    userId: string,
    role: string,
    permissions: string[],
    expiresIn: string = '1h'
  ): string {
    const payload = {
      sub: userId,
      iat: Math.floor(Date.now() / 1000),
      aud: 'your-app',
      iss: 'your-auth-service',
      role,
      permissions
    };
    
    return jwt.sign(payload, this.secretKey, { 
      algorithm: this.algorithm,
      expiresIn 
    });
  }
  
  createRefreshToken(userId: string): string {
    const payload = {
      sub: userId,
      type: 'refresh'
    };
    
    return jwt.sign(payload, this.secretKey, {
      algorithm: this.algorithm,
      expiresIn: '30d'
    });
  }
  
  verifyToken(token: string): JWTPayload {
    try {
      return jwt.verify(token, this.secretKey, {
        algorithms: [this.algorithm],
        audience: 'your-app',
        issuer: 'your-auth-service'
      }) as JWTPayload;
    } catch (error) {
      if (error instanceof jwt.TokenExpiredError) {
        throw new Error('Token has expired');
      }
      if (error instanceof jwt.JsonWebTokenError) {
        throw new Error('Invalid token');
      }
      throw error;
    }
  }
  
  // Express middleware
  authenticateToken = (
    req: AuthenticatedRequest, 
    res: Response, 
    next: NextFunction
  ): void => {
    const authHeader = req.headers.authorization;
    const token = authHeader?.split(' ')[1]; // Bearer TOKEN
    
    if (!token) {
      res.status(401).json({ error: 'Access token required' });
      return;
    }
    
    try {
      const user = this.verifyToken(token);
      req.user = user;
      next();
    } catch (error) {
      res.status(403).json({ error: error.message });
    }
  };
  
  // Role-based authorization middleware
  requireRole = (allowedRoles: string[]) => {
    return (req: AuthenticatedRequest, res: Response, next: NextFunction): void => {
      if (!req.user) {
        res.status(401).json({ error: 'Authentication required' });
        return;
      }
      
      if (!allowedRoles.includes(req.user.role)) {
        res.status(403).json({ error: 'Insufficient permissions' });
        return;
      }
      
      next();
    };
  };
  
  // Permission-based authorization middleware
  requirePermission = (requiredPermission: string) => {
    return (req: AuthenticatedRequest, res: Response, next: NextFunction): void => {
      if (!req.user) {
        res.status(401).json({ error: 'Authentication required' });
        return;
      }
      
      if (!req.user.permissions.includes(requiredPermission)) {
        res.status(403).json({ error: 'Insufficient permissions' });
        return;
      }
      
      next();
    };
  };
}

// Usage
const jwtService = new JWTService(process.env.JWT_SECRET!);

app.post('/login', async (req, res) => {
  const { username, password } = req.body;
  
  try {
    const user = await authenticateUser(username, password);
    if (!user) {
      return res.status(401).json({ error: 'Invalid credentials' });
    }
    
    const accessToken = jwtService.createAccessToken(
      user.id, 
      user.role, 
      user.permissions
    );
    const refreshToken = jwtService.createRefreshToken(user.id);
    
    res.json({
      accessToken,
      refreshToken,
      tokenType: 'bearer'
    });
  } catch (error) {
    res.status(500).json({ error: 'Authentication failed' });
  }
});

app.get('/profile', 
  jwtService.authenticateToken,
  (req: AuthenticatedRequest, res) => {
    res.json({ user: req.user });
  }
);

app.get('/admin', 
  jwtService.authenticateToken,
  jwtService.requireRole(['admin', 'superuser']),
  (req, res) => {
    res.json({ message: 'Admin access granted' });
  }
);
```

### Go Implementation

```go
package auth

import (
    "context"
    "fmt"
    "net/http"
    "strings"
    "time"
    
    "github.com/golang-jwt/jwt/v5"
)

type JWTManager struct {
    secretKey []byte
    issuer    string
    audience  string
}

type Claims struct {
    UserID      string   `json:"sub"`
    Role        string   `json:"role"`
    Permissions []string `json:"permissions"`
    jwt.RegisteredClaims
}

func NewJWTManager(secretKey, issuer, audience string) *JWTManager {
    return &JWTManager{
        secretKey: []byte(secretKey),
        issuer:    issuer,
        audience:  audience,
    }
}

func (j *JWTManager) CreateAccessToken(
    userID, role string, 
    permissions []string, 
    duration time.Duration,
) (string, error) {
    claims := Claims{
        UserID:      userID,
        Role:        role,
        Permissions: permissions,
        RegisteredClaims: jwt.RegisteredClaims{
            ExpiresAt: jwt.NewNumericDate(time.Now().Add(duration)),
            IssuedAt:  jwt.NewNumericDate(time.Now()),
            Issuer:    j.issuer,
            Audience:  []string{j.audience},
        },
    }
    
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    return token.SignedString(j.secretKey)
}

func (j *JWTManager) CreateRefreshToken(userID string) (string, error) {
    claims := jwt.RegisteredClaims{
        Subject:   userID,
        ExpiresAt: jwt.NewNumericDate(time.Now().Add(30 * 24 * time.Hour)),
        IssuedAt:  jwt.NewNumericDate(time.Now()),
        Issuer:    j.issuer,
        Audience:  []string{j.audience},
    }
    
    token := jwt.NewWithClaims(jwt.SigningMethodHS256, claims)
    return token.SignedString(j.secretKey)
}

func (j *JWTManager) VerifyToken(tokenString string) (*Claims, error) {
    token, err := jwt.ParseWithClaims(
        tokenString,
        &Claims{},
        func(token *jwt.Token) (interface{}, error) {
            if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
                return nil, fmt.Errorf("unexpected signing method: %v", token.Header["alg"])
            }
            return j.secretKey, nil
        },
    )
    
    if err != nil {
        return nil, fmt.Errorf("failed to parse token: %w", err)
    }
    
    claims, ok := token.Claims.(*Claims)
    if !ok || !token.Valid {
        return nil, fmt.Errorf("invalid token")
    }
    
    return claims, nil
}

// HTTP Middleware
func (j *JWTManager) AuthenticateMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        authHeader := r.Header.Get("Authorization")
        if authHeader == "" {
            http.Error(w, "Authorization header required", http.StatusUnauthorized)
            return
        }
        
        parts := strings.SplitN(authHeader, " ", 2)
        if len(parts) != 2 || parts[0] != "Bearer" {
            http.Error(w, "Invalid authorization header format", http.StatusUnauthorized)
            return
        }
        
        claims, err := j.VerifyToken(parts[1])
        if err != nil {
            http.Error(w, "Invalid token: "+err.Error(), http.StatusUnauthorized)
            return
        }
        
        // Add claims to context
        ctx := context.WithValue(r.Context(), "user", claims)
        next.ServeHTTP(w, r.WithContext(ctx))
    })
}

func (j *JWTManager) RequireRole(allowedRoles []string) func(http.Handler) http.Handler {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            claims, ok := r.Context().Value("user").(*Claims)
            if !ok {
                http.Error(w, "Authentication required", http.StatusUnauthorized)
                return
            }
            
            roleAllowed := false
            for _, role := range allowedRoles {
                if claims.Role == role {
                    roleAllowed = true
                    break
                }
            }
            
            if !roleAllowed {
                http.Error(w, "Insufficient permissions", http.StatusForbidden)
                return
            }
            
            next.ServeHTTP(w, r)
        })
    }
}

// Usage example
func main() {
    jwtManager := NewJWTManager("your-secret-key", "your-service", "your-app")
    
    mux := http.NewServeMux()
    
    mux.HandleFunc("/login", func(w http.ResponseWriter, r *http.Request) {
        // Authentication logic here
        accessToken, _ := jwtManager.CreateAccessToken(
            "user123", 
            "user", 
            []string{"read", "write"}, 
            time.Hour,
        )
        
        fmt.Fprintf(w, `{"access_token": "%s"}`, accessToken)
    })
    
    // Protected route
    protected := jwtManager.AuthenticateMiddleware(
        http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            claims := r.Context().Value("user").(*Claims)
            fmt.Fprintf(w, "Hello %s", claims.UserID)
        }),
    )
    mux.Handle("/profile", protected)
    
    // Admin-only route
    adminOnly := jwtManager.RequireRole([]string{"admin"})(
        http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            w.Write([]byte("Admin access granted"))
        }),
    )
    mux.Handle("/admin", jwtManager.AuthenticateMiddleware(adminOnly))
    
    http.ListenAndServe(":8080", mux)
}
```

## Security Best Practices

### Token Storage
- **Frontend**: Store access tokens in memory, refresh tokens in httpOnly cookies
- **Mobile**: Use secure keychain/keystore for token storage
- **Never**: Store tokens in localStorage for sensitive applications

### Token Rotation
```typescript
class TokenManager {
  private accessToken: string | null = null;
  private refreshToken: string | null = null;
  private tokenRefreshPromise: Promise<string> | null = null;
  
  async getValidToken(): Promise<string> {
    if (this.isTokenValid(this.accessToken)) {
      return this.accessToken!;
    }
    
    // Prevent multiple simultaneous refresh attempts
    if (!this.tokenRefreshPromise) {
      this.tokenRefreshPromise = this.refreshAccessToken();
    }
    
    try {
      return await this.tokenRefreshPromise;
    } finally {
      this.tokenRefreshPromise = null;
    }
  }
  
  private async refreshAccessToken(): Promise<string> {
    const response = await fetch('/api/auth/refresh', {
      method: 'POST',
      credentials: 'include', // Include httpOnly cookie
    });
    
    if (!response.ok) {
      throw new Error('Failed to refresh token');
    }
    
    const data = await response.json();
    this.accessToken = data.access_token;
    return this.accessToken;
  }
  
  private isTokenValid(token: string | null): boolean {
    if (!token) return false;
    
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      return payload.exp * 1000 > Date.now();
    } catch {
      return false;
    }
  }
}
```

### HTTPS Requirements
- Always use HTTPS in production
- Use secure, httpOnly cookies for refresh tokens
- Implement proper CORS policies
- Use strong JWT secrets (256-bit minimum)