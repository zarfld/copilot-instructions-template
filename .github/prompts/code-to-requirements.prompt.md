---
mode: agent
applyTo:
  - "**/src/**/*.js"
  - "**/src/**/*.ts"
  - "**/src/**/*.py"
  - "**/src/**/*.java"
  - "**/src/**/*.go"
  - "**/src/**/*.cs"
  - "**/lib/**/*"
  - "**/app/**/*"
  - "**/tests/**/*"
  - "**/test/**/*"
---

# Code to Requirements Reverse Engineering Prompt

You are a **Requirements Engineer** and **Static Code Analysis Expert** following **ISO/IEC/IEEE 29148:2018**.

## 🎯 Objective

Reverse engineer formal requirements specifications from existing code:
1. **Analyze code behavior** to infer functional requirements
2. **Extract non-functional requirements** from implementation patterns
3. **Generate acceptance criteria** from test cases
4. **Create traceability links** between code and requirements
5. **Produce ISO 29148 compliant** requirements specification

## 🔍 Code Analysis Framework

### Step 1: Code Structure Analysis

**Identify system components**:

#### **Frontend Analysis**
```bash
# Identify UI components and pages
find src/ -name "*.jsx" -o -name "*.tsx" -o -name "*.vue" -o -name "*.html"

# Extract user-facing features
grep -r "onClick\|onSubmit\|useEffect\|useState" src/components/
```

#### **Backend Analysis** 
```bash
# Identify API endpoints
grep -r "app.get\|app.post\|@GetMapping\|@PostMapping\|def.*get\|def.*post" src/

# Extract business logic
find src/ -name "*service*" -o -name "*controller*" -o -name "*handler*"
```

#### **Database Analysis**
```bash
# Find data models and schemas
find src/ -name "*model*" -o -name "*schema*" -o -name "*.sql"

# Extract data operations
grep -r "SELECT\|INSERT\|UPDATE\|DELETE\|CREATE TABLE" src/
```

### Step 2: Functional Requirements Extraction

**Extract requirements from code patterns**:

#### **API Endpoints → Functional Requirements**

**Code Pattern**:
```javascript
// Express.js example
app.post('/api/users', async (req, res) => {
  const { email, password, name } = req.body;
  
  // Validation
  if (!email || !isValidEmail(email)) {
    return res.status(400).json({ error: 'Valid email required' });
  }
  if (!password || password.length < 8) {
    return res.status(400).json({ error: 'Password must be at least 8 characters' });
  }
  
  // Business logic
  const existingUser = await User.findByEmail(email);
  if (existingUser) {
    return res.status(409).json({ error: 'User already exists' });
  }
  
  const hashedPassword = await bcrypt.hash(password, 12);
  const user = await User.create({
    email,
    password: hashedPassword,
    name,
    createdAt: new Date()
  });
  
  res.status(201).json({ id: user.id, email: user.email, name: user.name });
});
```

**Generated Requirement**:
```markdown
## REQ-F-USER-001: User Registration

**ID**: REQ-F-USER-001
**Priority**: High (P1)
**Source**: Derived from POST /api/users endpoint implementation
**Status**: Implemented

### Description
The system shall allow new users to register by providing email, password, and name.

### Functional Requirements

#### REQ-F-USER-001.1: Registration Data Collection
The system shall accept user registration requests with:
- Email address (required, must be valid email format)
- Password (required, minimum 8 characters)
- Full name (required)

#### REQ-F-USER-001.2: Email Uniqueness Validation
The system shall ensure email addresses are unique across all users.

#### REQ-F-USER-001.3: Password Security
The system shall hash passwords using bcrypt with cost factor 12 before storage.

#### REQ-F-USER-001.4: User Account Creation
The system shall create user account with generated unique ID and timestamp.

### Acceptance Criteria

```gherkin
Scenario: Successful user registration
  Given no user exists with email "john@example.com"
  When user submits registration with:
    | email | john@example.com |
    | password | SecurePass123 |
    | name | John Smith |
  Then user account is created successfully
  And response contains user ID, email, and name
  And password is hashed with bcrypt
  And HTTP status is 201 Created

Scenario: Registration with existing email
  Given user exists with email "john@example.com"
  When user submits registration with email "john@example.com"
  Then registration fails with "User already exists"
  And HTTP status is 409 Conflict
  And no duplicate user is created

Scenario: Registration with invalid email
  Given user submits registration with email "invalid-email"
  Then registration fails with "Valid email required"
  And HTTP status is 400 Bad Request

Scenario: Registration with weak password
  Given user submits registration with password "123"
  Then registration fails with "Password must be at least 8 characters"
  And HTTP status is 400 Bad Request
```

### Traceability
- **Implemented in**: src/controllers/userController.js (POST /api/users)
- **Tests**: tests/user.registration.test.js
- **Database**: users table (email, password_hash, name, created_at)
```

#### **Business Logic → Requirements**

**Code Pattern**:
```python
# Python example - Order processing
def process_order(order_data):
    order = Order(**order_data)
    
    # Inventory check
    for item in order.items:
        if not inventory_service.is_available(item.product_id, item.quantity):
            raise InsufficientInventoryError(f"Not enough {item.product_id}")
    
    # Calculate pricing
    subtotal = sum(item.price * item.quantity for item in order.items)
    tax = calculate_tax(subtotal, order.shipping_address.state)
    shipping = calculate_shipping(order.weight, order.shipping_address)
    total = subtotal + tax + shipping
    
    # Apply discount
    if order.discount_code:
        discount = apply_discount(order.discount_code, subtotal)
        total = total - discount
    
    # Process payment
    payment_result = payment_service.charge(order.payment_method, total)
    if not payment_result.success:
        raise PaymentFailedError(payment_result.error_message)
    
    # Update inventory
    for item in order.items:
        inventory_service.reserve(item.product_id, item.quantity)
    
    # Create order record
    order.status = 'confirmed'
    order.total_amount = total
    order.payment_id = payment_result.transaction_id
    order.save()
    
    # Send confirmation
    email_service.send_order_confirmation(order)
    
    return order
```

**Generated Requirements**:
```markdown
## REQ-F-ORDER-002: Order Processing

**ID**: REQ-F-ORDER-002
**Priority**: Critical (P0)
**Source**: Derived from process_order() function implementation

### Description
The system shall process customer orders including inventory validation, pricing calculation, payment processing, and order confirmation.

### Sub-Requirements

#### REQ-F-ORDER-002.1: Inventory Validation
The system shall verify sufficient inventory exists for all ordered items before processing.

#### REQ-F-ORDER-002.2: Price Calculation
The system shall calculate order total including:
- Item subtotal (price × quantity for each item)
- Tax calculation based on shipping address
- Shipping cost based on weight and destination
- Discount application (if valid discount code provided)

#### REQ-F-ORDER-002.3: Payment Processing
The system shall process payment using provided payment method and handle payment failures gracefully.

#### REQ-F-ORDER-002.4: Inventory Reservation
The system shall reserve inventory for confirmed orders to prevent overselling.

#### REQ-F-ORDER-002.5: Order Confirmation
The system shall create order record with confirmed status and send confirmation email to customer.

### Error Handling

#### REQ-F-ORDER-002.E1: Insufficient Inventory
When inventory is insufficient, system shall return error "Not enough [product_id]" without processing order.

#### REQ-F-ORDER-002.E2: Payment Failure
When payment fails, system shall return payment error message without updating inventory or creating order.

### Acceptance Criteria

```gherkin
Scenario: Successful order processing
  Given inventory has sufficient quantities for all items
  And customer has valid payment method
  When order is submitted for processing
  Then inventory is validated for all items
  And total price is calculated (subtotal + tax + shipping - discount)
  And payment is processed successfully
  And inventory is reserved for ordered items
  And order record is created with 'confirmed' status
  And confirmation email is sent to customer

Scenario: Order with insufficient inventory
  Given inventory has insufficient quantity for item "PROD-123"
  When order containing "PROD-123" is processed
  Then system throws InsufficientInventoryError
  And error message includes "Not enough PROD-123"
  And no payment is processed
  And no inventory is reserved

Scenario: Order with payment failure
  Given order has valid inventory
  But payment processing fails with "Card declined"
  When order is processed
  Then system throws PaymentFailedError
  And error message is "Card declined"
  And no inventory is reserved
  And no order record is created
```
```

### Step 3: Non-Functional Requirements Extraction

**Extract NFRs from code patterns**:

#### **Performance Requirements**

**Code Patterns to Analyze**:
```javascript
// Caching patterns
const cache = new Redis();
app.get('/api/products', async (req, res) => {
  const cacheKey = `products:${req.query.page}:${req.query.limit}`;
  let products = await cache.get(cacheKey);
  
  if (!products) {
    products = await Product.findAll({
      limit: req.query.limit || 20,
      offset: (req.query.page - 1) * (req.query.limit || 20)
    });
    await cache.setex(cacheKey, 300, JSON.stringify(products)); // 5 min cache
  }
  
  res.json(products);
});

// Database indexing
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at);

// Pagination limits
const MAX_PAGE_SIZE = 100;
const DEFAULT_PAGE_SIZE = 20;
```

**Generated NFR**:
```markdown
## REQ-NF-PERF-001: Product Listing Performance

**ID**: REQ-NF-PERF-001
**Priority**: High (P1)
**Source**: Derived from caching and pagination implementation

### Description
The system shall provide fast product listing with caching and pagination for optimal performance.

### Performance Requirements

#### REQ-NF-PERF-001.1: Response Time
Product listing API shall respond within 200ms for 95% of requests under normal load.

#### REQ-NF-PERF-001.2: Caching Strategy
System shall cache product listing results for 5 minutes to reduce database load.

#### REQ-NF-PERF-001.3: Pagination Limits
System shall support pagination with:
- Default page size: 20 items
- Maximum page size: 100 items
- Efficient offset-based pagination

#### REQ-NF-PERF-001.4: Database Optimization
System shall use database indexes on frequently queried columns (category_id, created_at).

### Acceptance Criteria

```gherkin
Scenario: Fast product listing response
  Given system has cached product data
  When client requests product listing
  Then response is returned within 200ms
  And response contains requested page of products
  And cache-control headers indicate 5-minute cache

Scenario: Efficient pagination
  Given client requests page 5 with 50 items per page
  When system processes request
  Then database query uses LIMIT 50 OFFSET 200
  And response includes pagination metadata
  And database indexes are utilized for performance
```
```

#### **Security Requirements**

**Code Patterns**:
```javascript
// Authentication middleware
const jwt = require('jsonwebtoken');
const authenticate = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) {
    return res.status(401).json({ error: 'Authentication required' });
  }
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    req.user = decoded;
    next();
  } catch (error) {
    return res.status(401).json({ error: 'Invalid token' });
  }
};

// Input validation
const validateUserInput = (req, res, next) => {
  const { email, password } = req.body;
  
  // SQL injection prevention
  if (typeof email !== 'string' || typeof password !== 'string') {
    return res.status(400).json({ error: 'Invalid input type' });
  }
  
  // XSS prevention
  req.body.email = xss(email);
  req.body.name = xss(req.body.name);
  
  next();
};

// Rate limiting
const rateLimit = require('express-rate-limit');
const loginLimiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 5, // 5 attempts per window
  message: 'Too many login attempts, please try again later'
});
```

**Generated NFR**:
```markdown
## REQ-NF-SEC-001: Authentication and Authorization

**ID**: REQ-NF-SEC-001
**Priority**: Critical (P0)
**Source**: Derived from authentication middleware implementation

### Description
The system shall implement secure authentication and authorization using JWT tokens.

### Security Requirements

#### REQ-NF-SEC-001.1: JWT Authentication
System shall use JWT tokens for user authentication with:
- Token-based stateless authentication
- Configurable token expiration
- Secure token verification

#### REQ-NF-SEC-001.2: Input Validation and Sanitization
System shall validate and sanitize all user inputs to prevent:
- SQL injection attacks (type checking)
- XSS attacks (input sanitization)
- Invalid data type submissions

#### REQ-NF-SEC-001.3: Rate Limiting
System shall implement rate limiting for authentication endpoints:
- Maximum 5 login attempts per 15-minute window
- Clear error messages for rate limit violations
- IP-based rate limiting

### Acceptance Criteria

```gherkin
Scenario: Valid JWT authentication
  Given user has valid JWT token
  When user accesses protected endpoint
  Then request is processed successfully
  And user context is available in request

Scenario: Invalid JWT authentication
  Given user provides invalid or expired JWT token
  When user accesses protected endpoint
  Then request is rejected with 401 Unauthorized
  And error message is "Invalid token"

Scenario: Rate limiting on login attempts
  Given user has made 5 failed login attempts in 15 minutes
  When user attempts to login again
  Then request is rejected with 429 Too Many Requests
  And error message is "Too many login attempts, please try again later"
```
```

### Step 4: Test-Driven Requirements

**Extract acceptance criteria from existing tests**:

#### **Unit Tests → Acceptance Criteria**

**Test Code**:
```javascript
describe('User Registration', () => {
  test('should create user with valid data', async () => {
    const userData = {
      email: 'test@example.com',
      password: 'SecurePassword123',
      name: 'Test User'
    };
    
    const response = await request(app)
      .post('/api/users')
      .send(userData)
      .expect(201);
      
    expect(response.body).toHaveProperty('id');
    expect(response.body.email).toBe(userData.email);
    expect(response.body.name).toBe(userData.name);
    expect(response.body).not.toHaveProperty('password');
  });
  
  test('should reject duplicate email', async () => {
    await User.create({
      email: 'existing@example.com',
      password: 'hashedpassword',
      name: 'Existing User'
    });
    
    const response = await request(app)
      .post('/api/users')
      .send({
        email: 'existing@example.com',
        password: 'NewPassword123',
        name: 'New User'
      })
      .expect(409);
      
    expect(response.body.error).toBe('User already exists');
  });
});
```

**Generated Acceptance Criteria**:
```gherkin
Scenario: Create user with valid data
  Given no user exists with email "test@example.com"
  When POST request to "/api/users" with:
    | email | test@example.com |
    | password | SecurePassword123 |
    | name | Test User |
  Then response status is 201 Created
  And response body contains user ID
  And response body contains email "test@example.com"
  And response body contains name "Test User"
  And response body does not contain password

Scenario: Reject duplicate email registration
  Given user exists with email "existing@example.com"
  When POST request to "/api/users" with:
    | email | existing@example.com |
    | password | NewPassword123 |
    | name | New User |
  Then response status is 409 Conflict
  And response body contains error "User already exists"
```

### Step 5: Requirements Specification Generation

**Complete ISO 29148 Requirements Document**:

```markdown
# System Requirements Specification

**Document Version**: 1.0
**Date**: [Generated Date]
**Source**: Reverse engineered from existing codebase
**Status**: Draft for Review

## 1. Introduction

### 1.1 Purpose
This document specifies the system requirements derived from analysis of the existing codebase implementation.

### 1.2 Scope
This specification covers functional and non-functional requirements extracted from:
- API endpoint implementations
- Business logic functions  
- Database schemas and operations
- Test cases and validation logic
- Security and performance patterns

### 1.3 Definitions and Acronyms
| Term | Definition |
|------|------------|
| API | Application Programming Interface |
| JWT | JSON Web Token |
| NFR | Non-Functional Requirement |
| TDD | Test-Driven Development |

## 2. System Overview

### 2.1 System Purpose
[Inferred from code analysis - what the system does]

### 2.2 System Architecture
[High-level architecture derived from code structure]

### 2.3 Key Components
[Main modules/services identified in codebase]

## 3. Functional Requirements

### 3.1 User Management (REQ-F-USER-xxx)
[Requirements derived from user-related code]

### 3.2 Order Processing (REQ-F-ORDER-xxx)
[Requirements derived from order processing logic]

### 3.3 Product Catalog (REQ-F-PRODUCT-xxx)
[Requirements derived from product management code]

[Continue for all functional areas...]

## 4. Non-Functional Requirements

### 4.1 Performance Requirements (REQ-NF-PERF-xxx)
[Requirements derived from caching, pagination, optimization patterns]

### 4.2 Security Requirements (REQ-NF-SEC-xxx)
[Requirements derived from authentication, validation, rate limiting]

### 4.3 Reliability Requirements (REQ-NF-REL-xxx)
[Requirements derived from error handling, logging patterns]

### 4.4 Usability Requirements (REQ-NF-USE-xxx)
[Requirements derived from UI/UX implementation]

## 5. System Interfaces

### 5.1 External APIs
[Interfaces derived from external service integrations]

### 5.2 Database Interfaces
[Data models and schemas found in code]

### 5.3 User Interfaces
[UI components and pages identified]

## 6. Data Requirements

### 6.1 Data Models
[Entity relationships derived from code]

### 6.2 Data Storage
[Database structure inferred from models and migrations]

### 6.3 Data Processing
[Data transformations found in business logic]

## 7. Traceability Matrix

| Requirement ID | Source Code | Test Cases | Database | UI Component |
|----------------|-------------|------------|----------|--------------|
| REQ-F-USER-001 | userController.js | user.test.js | users table | RegisterForm.jsx |
| REQ-F-ORDER-002 | orderService.py | order.test.py | orders table | OrderForm.vue |
[Continue for all requirements...]

## 8. Validation and Verification

### 8.1 Requirements Validation
- All requirements derived from actual implemented functionality
- Requirements verified against existing test cases
- Acceptance criteria match test assertions

### 8.2 Completeness Assessment
- **Code Coverage**: [%] of codebase analyzed for requirements
- **Test Coverage**: [%] of requirements have corresponding tests  
- **Gap Analysis**: [Areas where requirements may be incomplete]

## 9. Assumptions and Dependencies

### 9.1 Assumptions
[Assumptions made during reverse engineering process]

### 9.2 Dependencies
[External dependencies identified in code]

## 10. Change Management

### 10.1 Requirements Baseline
This specification represents the current implemented functionality as of [date].

### 10.2 Future Changes
New requirements should follow the spec-driven development process using elicitation and refinement prompts.
```

## 🚀 Usage

### Full Codebase Analysis:
```bash
/code-to-requirements.prompt.md Analyze the entire codebase and generate a complete requirements specification.

Focus on:
- All API endpoints and business logic
- Security and performance patterns
- Database operations and data models
- Test cases for acceptance criteria
- Error handling and validation logic

Generate ISO 29148 compliant requirements document.
```

### Specific Component Analysis:
```bash
# Analyze specific module
/code-to-requirements.prompt.md Analyze the user authentication module and generate security requirements.

Files to analyze:
- src/auth/authController.js
- src/middleware/authentication.js  
- tests/auth.test.js

# Analyze API endpoints
/code-to-requirements.prompt.md Extract functional requirements from all REST API endpoints in the order management service.
```

### Test-Driven Requirements:
```bash
/code-to-requirements.prompt.md Generate acceptance criteria based on existing test cases.

Analyze test files:
- tests/user.test.js
- tests/order.test.js
- tests/payment.test.js

Create Gherkin scenarios matching test assertions.
```

## 📊 Analysis Patterns

### **Code Pattern Recognition**:

1. **CRUD Operations** → Functional requirements
2. **Validation Logic** → Business rules and constraints  
3. **Error Handling** → Exception scenarios
4. **Caching/Optimization** → Performance requirements
5. **Authentication/Authorization** → Security requirements
6. **Rate Limiting** → Scalability requirements
7. **Logging/Monitoring** → Observability requirements
8. **Test Assertions** → Acceptance criteria

### **Traceability Establishment**:

- **API Endpoint** ↔ **Functional Requirement**
- **Test Case** ↔ **Acceptance Criteria**
- **Database Model** ↔ **Data Requirement**
- **Validation Logic** ↔ **Business Rule**
- **Error Handler** ↔ **Exception Scenario**

---

**Transform code into compliant requirements!** 🔄