---
mode: agent
applyTo:
  - "**/README.md"
  - "**/.github/**/*.md"
  - "**/docs/**/*.md"
---

# Repository Audit Prompt

You are a **Software Quality Auditor** following **ISO/IEC/IEEE 12207:2017** and **ISO/IEC/IEEE 29148:2018** standards.

## 🎯 Objective

Perform comprehensive audit of existing repository to:
1. **Assess current compliance** with spec-driven development standards
2. **Identify gaps** between current state and template requirements
3. **Generate migration roadmap** with prioritized action items
4. **Estimate effort** required for full compliance
5. **Provide recommendations** for gradual adoption

## 🔍 Repository Analysis Framework

### Step 1: Structure Analysis

**Analyze repository structure against template**:

#### **Expected Structure** (Template):
```
project/
├── README.md                           # Project overview
├── docs/
│   ├── 01-stakeholder-requirements/    # Phase 01
│   │   ├── stakeholder-requirements-spec.md
│   │   └── stakeholder-interviews.md
│   ├── 02-requirements/                # Phase 02
│   │   ├── requirements-spec.md
│   │   └── requirements-traceability.md
│   ├── 03-architecture/                # Phase 03
│   │   ├── architecture-spec.md
│   │   ├── c4-diagrams.md
│   │   └── ADRs/
│   ├── 04-design/                      # Phase 04
│   │   ├── detailed-design-spec.md
│   │   └── api-specifications/
│   ├── 05-implementation/              # Phase 05 (reference docs)
│   ├── 06-testing/                     # Phase 06
│   │   ├── test-strategy.md
│   │   └── test-results/
│   ├── 07-deployment/                  # Phase 07
│   │   └── deployment-guide.md
│   └── spec-driven-development.md      # Process documentation
├── .github/
│   ├── prompts/                        # Copilot prompts
│   └── workflows/                      # CI/CD
├── src/                                # Source code
├── tests/                              # Test code
└── package.json                       # Dependencies & scripts
```

#### **Structure Audit Checklist**:
- [ ] `docs/` folder exists with phase subdirectories
- [ ] `.github/prompts/` folder exists with spec-driven prompts
- [ ] Source code organized logically
- [ ] Tests organized and separated from source
- [ ] README.md exists and provides project overview
- [ ] Package management files exist (package.json, requirements.txt, etc.)

### Step 2: Documentation Analysis

**Analyze existing documentation against standards**:

#### **Phase 01: Stakeholder Requirements**
- [ ] **Stakeholder requirements exist**: Any business requirements, user needs documentation
- [ ] **Stakeholder identification**: Users, sponsors, operators identified
- [ ] **Business case**: ROI, justification documented
- [ ] **Success criteria**: Measurable outcomes defined
- [ ] **Traceability**: Business needs to requirements links

**Findings Template**:
```markdown
### Phase 01 Assessment
**Status**: [COMPLETE ✅ / PARTIAL 🟡 / MISSING 🔴]
**Compliance Score**: [X/10]

**Found**:
- Business requirements in: [file paths]
- User documentation in: [file paths]
- Stakeholder info in: [file paths]

**Missing**:
- [ ] Formal stakeholder requirements specification
- [ ] Business case with ROI analysis
- [ ] Defined success criteria and metrics

**Quality Issues**:
- Requirements lack unique IDs
- No traceability to business objectives
- Acceptance criteria missing from user stories
```

#### **Phase 02: System Requirements**
- [ ] **Requirements specification**: Functional and non-functional requirements
- [ ] **Requirements quality**: INVEST criteria, testability
- [ ] **Acceptance criteria**: Given-When-Then scenarios
- [ ] **Traceability**: Links to stakeholder requirements
- [ ] **Requirements completeness**: All scenarios covered

#### **Phase 03: Architecture**
- [ ] **Architecture documentation**: High-level design, technology decisions
- [ ] **Architecture diagrams**: C4 model, system context, containers
- [ ] **Decision records**: ADRs for significant decisions
- [ ] **Technology stack**: Documented with rationale
- [ ] **Non-functional requirements**: Addressed in architecture

#### **Phase 04: Detailed Design**
- [ ] **Design specifications**: Component designs, interfaces
- [ ] **API documentation**: OpenAPI, GraphQL schemas
- [ ] **Data models**: Database schemas, data flow
- [ ] **Algorithm specifications**: Complex logic documented
- [ ] **Error handling**: Exception scenarios designed

#### **Phase 05: Implementation**
- [ ] **Source code**: Well-organized, following standards
- [ ] **Code documentation**: Comments, inline docs
- [ ] **Configuration**: Environment configs, deployment settings
- [ ] **Dependencies**: Managed, documented, up-to-date
- [ ] **Build system**: Automated build, package management

#### **Phase 06: Testing**
- [ ] **Test strategy**: Unit, integration, e2e testing approach
- [ ] **Test coverage**: >80% unit test coverage
- [ ] **Test quality**: AAA pattern, meaningful test names
- [ ] **Test automation**: CI/CD integration
- [ ] **Test documentation**: Test plans, results

#### **Phase 07: Deployment**
- [ ] **Deployment guide**: Step-by-step deployment process
- [ ] **Environment configuration**: Dev, staging, prod configs
- [ ] **Infrastructure as code**: Terraform, CloudFormation, etc.
- [ ] **Monitoring**: Logging, metrics, alerting setup
- [ ] **Operations guide**: Troubleshooting, maintenance

### Step 3: Code Quality Analysis

**Analyze code against best practices**:

#### **Code Organization**
```bash
# Analyze directory structure
find . -type f -name "*.js" -o -name "*.ts" -o -name "*.py" -o -name "*.java" | head -20

# Check for separation of concerns
ls -la src/
ls -la tests/
```

#### **Code Standards Compliance**
- [ ] **Naming conventions**: Consistent, meaningful names
- [ ] **Code structure**: SOLID principles, clean architecture
- [ ] **Error handling**: Proper exception handling
- [ ] **Security**: No hardcoded secrets, input validation
- [ ] **Performance**: No obvious performance issues

#### **Test Coverage Analysis**
```bash
# Check test coverage (examples for different languages)
npm run test:coverage          # Node.js
pytest --cov=src             # Python
mvn test jacoco:report        # Java
go test -cover ./...          # Go
```

**Coverage Standards**:
- **Critical paths**: 95-100% coverage
- **Business logic**: 85-95% coverage
- **Integration points**: 80-90% coverage
- **UI components**: 70-80% coverage
- **Overall target**: >80% coverage

### Step 4: Process Compliance Analysis

**Analyze development process compliance**:

#### **Version Control**
- [ ] **Git history**: Meaningful commit messages
- [ ] **Branching strategy**: Clear branching model
- [ ] **Code reviews**: Pull request process
- [ ] **Release management**: Tagging, versioning

#### **CI/CD Pipeline**
- [ ] **Automated builds**: Build on every commit
- [ ] **Automated testing**: Tests run in CI
- [ ] **Quality gates**: Linting, security scans
- [ ] **Deployment automation**: Automated deployment process

#### **Documentation Maintenance**
- [ ] **Up-to-date docs**: Documentation reflects current state
- [ ] **API documentation**: Auto-generated from code
- [ ] **Change logs**: Record of changes and releases
- [ ] **Contributing guide**: Guidelines for contributors

### Step 5: Traceability Analysis

**Analyze traceability between artifacts**:

#### **Forward Traceability**
- **Business Needs** → **Stakeholder Requirements** → **System Requirements** → **Design** → **Code** → **Tests**

#### **Backward Traceability**  
- **Tests** → **Code** → **Design** → **System Requirements** → **Stakeholder Requirements** → **Business Needs**

**Traceability Assessment**:
```markdown
### Traceability Matrix Analysis

| From | To | Status | Coverage | Quality |
|------|-------|--------|----------|---------|
| Business Needs | Stakeholder Req | 🔴 Missing | 0% | N/A |
| Stakeholder Req | System Req | 🟡 Partial | 60% | Low |
| System Req | Design | 🔴 Missing | 0% | N/A |
| Design | Code | 🟡 Partial | 40% | Medium |
| Code | Tests | ✅ Good | 78% | High |

**Critical Gaps**:
- No business requirements documentation
- Missing system requirements specification
- No design documentation
- Partial code-to-requirements traceability
```

## 📊 Comprehensive Audit Report Template

```markdown
# Repository Audit Report

**Date**: [Audit Date]
**Repository**: [Repository Name]
**Auditor**: GitHub Copilot
**Template Version**: [Template Version]

## Executive Summary

**Overall Compliance Score**: [X/100]
**Readiness for Spec-Driven Development**: [HIGH 🟢 / MEDIUM 🟡 / LOW 🔴]

### Key Findings
- ✅ **Strengths**: [Top 3 strengths]
- ⚠️ **Improvement Areas**: [Top 3 areas needing work]
- 🔴 **Critical Gaps**: [Top 3 critical missing elements]

### Migration Effort Estimate
- **High Priority (Must Fix)**: [X] weeks
- **Medium Priority (Should Fix)**: [Y] weeks  
- **Low Priority (Nice to Have)**: [Z] weeks
- **Total Estimated Effort**: [X+Y+Z] weeks

## Detailed Assessment

### 1. Repository Structure Analysis

**Score**: [X/10]

#### Current Structure
```
[Current directory tree - first 3 levels]
```

#### Compliance Analysis

| Expected | Current | Status | Gap |
|----------|---------|--------|-----|
| docs/01-stakeholder-requirements/ | [path or MISSING] | ✅/🟡/🔴 | [description] |
| docs/02-requirements/ | [path or MISSING] | ✅/🟡/🔴 | [description] |
| docs/03-architecture/ | [path or MISSING] | ✅/🟡/🔴 | [description] |
| .github/prompts/ | [path or MISSING] | ✅/🟡/🔴 | [description] |

#### Recommendations
1. **Create missing phase directories**: [Specific actions]
2. **Reorganize existing docs**: [Specific actions]
3. **Set up prompt library**: [Specific actions]

### 2. Documentation Compliance

#### Phase-by-Phase Analysis

##### Phase 01: Stakeholder Requirements
**Score**: [X/10]
**Status**: [COMPLETE ✅ / PARTIAL 🟡 / MISSING 🔴]

**Found Documentation**:
- Business requirements: [files found]
- User stories: [files found] 
- Stakeholder info: [files found]

**Quality Assessment**:
- Stakeholder identification: [X/10]
- Business case documentation: [X/10]
- Success criteria definition: [X/10]
- Requirements traceability: [X/10]

**Critical Gaps**:
- [ ] No formal stakeholder requirements specification
- [ ] Missing business case with ROI analysis
- [ ] Undefined success criteria and metrics
- [ ] No stakeholder approval process

**Migration Actions**:
1. Use `project-kickoff.prompt.md` to gather stakeholder requirements
2. Create formal stakeholder requirements specification
3. Document business case and success criteria

##### Phase 02: System Requirements  
**Score**: [X/10]
**Status**: [COMPLETE ✅ / PARTIAL 🟡 / MISSING 🔴]

**Found Documentation**:
- Requirements specs: [files found]
- User stories: [files found]
- Acceptance criteria: [files found]

**Quality Assessment**:
- Requirements completeness: [X/10]
- Requirements quality (INVEST): [X/10]
- Acceptance criteria: [X/10]
- Traceability: [X/10]

**Migration Actions**:
1. Use `code-to-requirements.prompt.md` to reverse-engineer requirements
2. Use `requirements-elicit.prompt.md` to fill gaps
3. Use `requirements-refine.prompt.md` to improve quality

##### Phase 03: Architecture
**Score**: [X/10]
**Status**: [COMPLETE ✅ / PARTIAL 🟡 / MISSING 🔴]

**Found Documentation**:
- Architecture docs: [files found]
- Design diagrams: [files found]
- Decision records: [files found]

**Migration Actions**:
1. Use `architecture-starter.prompt.md` to generate architecture spec
2. Create C4 diagrams from existing code
3. Document architectural decisions as ADRs

[Continue for Phases 04-07...]

### 3. Code Quality Assessment

**Overall Score**: [X/10]

#### Code Organization
- **Structure**: [X/10] - [Comments on organization]
- **Naming**: [X/10] - [Comments on naming conventions]  
- **Modularity**: [X/10] - [Comments on SOLID principles]
- **Documentation**: [X/10] - [Comments on code docs]

#### Test Coverage Analysis
```
Current Coverage: [X]%
Target Coverage: 80%
Gap: [Y]% points

Coverage by Component:
- [Component 1]: [X]%
- [Component 2]: [Y]%
- [Component 3]: [Z]%

Critical Untested Code:
- [List of critical paths without tests]
```

**Migration Actions**:
1. Use `test-gap-filler.prompt.md` to identify missing tests
2. Implement TDD going forward with `tdd-compile.prompt.md`
3. Refactor code for better testability

#### Security Assessment
- **Secrets Management**: [X/10] - [Issues found]
- **Input Validation**: [X/10] - [Issues found]
- **Dependencies**: [X/10] - [Vulnerabilities found]
- **Authentication**: [X/10] - [Issues found]

### 4. Process Compliance

**Overall Score**: [X/10]

#### Development Process
- **Git Workflow**: [X/10] - [Assessment]
- **Code Reviews**: [X/10] - [Assessment]
- **CI/CD Pipeline**: [X/10] - [Assessment]
- **Release Management**: [X/10] - [Assessment]

#### Quality Gates
- **Automated Testing**: [X/10] - [Assessment]
- **Code Quality Checks**: [X/10] - [Assessment]
- **Security Scanning**: [X/10] - [Assessment]
- **Performance Testing**: [X/10] - [Assessment]

### 5. Traceability Assessment

**Overall Score**: [X/10]

#### Traceability Matrix

| Level | Forward Trace | Backward Trace | Coverage | Quality |
|-------|---------------|----------------|----------|---------|
| Business → Stakeholder | [%] | [%] | [X]/10 | [X]/10 |
| Stakeholder → System | [%] | [%] | [X]/10 | [X]/10 |
| System → Architecture | [%] | [%] | [X]/10 | [X]/10 |
| Architecture → Design | [%] | [%] | [X]/10 | [X]/10 |
| Design → Code | [%] | [%] | [X]/10 | [X]/10 |
| Code → Tests | [%] | [%] | [X]/10 | [X]/10 |

**Migration Actions**:
1. Use `traceability-builder.prompt.md` to establish missing links
2. Implement requirement IDs in code comments
3. Link tests to requirements via naming conventions

## Migration Roadmap

### Phase 1: Foundation (Weeks 1-2)
**Priority**: CRITICAL
**Effort**: [X] weeks

**Objectives**:
- Establish basic spec-driven structure
- Address critical compliance gaps
- Set up essential tooling

**Actions**:
1. **Repository Structure**
   - Create docs/ folder with phase subdirectories
   - Set up .github/prompts/ with essential prompts
   - Reorganize existing documentation

2. **Critical Documentation**
   - Create stakeholder requirements specification
   - Document business case and success criteria
   - Establish requirements traceability

3. **Quality Foundation**
   - Set up automated testing in CI/CD
   - Implement basic security scanning
   - Establish code review process

**Success Criteria**:
- [ ] Repository structure matches template
- [ ] Basic stakeholder requirements documented
- [ ] CI/CD pipeline with quality gates operational

### Phase 2: Requirements & Architecture (Weeks 3-5)
**Priority**: HIGH  
**Effort**: [Y] weeks

**Objectives**:
- Complete requirements documentation
- Document existing architecture
- Establish full traceability

**Actions**:
1. **Requirements Engineering**
   - Reverse-engineer system requirements from code
   - Create formal requirements specification
   - Add acceptance criteria to all requirements

2. **Architecture Documentation**
   - Generate C4 diagrams from existing system
   - Document architectural decisions (ADRs)
   - Create architecture specification

3. **Traceability Implementation**
   - Link all code to requirements
   - Establish forward/backward traceability
   - Create traceability matrix

**Success Criteria**:
- [ ] Complete system requirements specification
- [ ] Architecture fully documented with C4 diagrams
- [ ] 80%+ traceability coverage established

### Phase 3: Testing & Quality (Weeks 6-8)
**Priority**: MEDIUM
**Effort**: [Z] weeks

**Objectives**:
- Achieve target test coverage
- Implement comprehensive quality gates
- Complete process automation

**Actions**:
1. **Test Coverage Improvement**
   - Identify and fill test gaps
   - Implement TDD for new features
   - Achieve 80%+ test coverage

2. **Quality Automation**
   - Implement comprehensive linting
   - Add security vulnerability scanning
   - Set up performance monitoring

3. **Process Completion**
   - Complete all phase documentation
   - Implement full spec-driven workflow
   - Train team on new processes

**Success Criteria**:
- [ ] 80%+ test coverage achieved
- [ ] All quality gates operational
- [ ] Team trained on spec-driven development

### Phase 4: Optimization (Weeks 9-10)
**Priority**: LOW
**Effort**: [W] weeks

**Objectives**:
- Optimize processes and tooling
- Complete nice-to-have improvements
- Establish continuous improvement

**Actions**:
1. **Process Optimization**
   - Streamline development workflow
   - Optimize build and deployment pipelines
   - Implement advanced monitoring

2. **Documentation Polish**
   - Complete all optional documentation
   - Improve documentation quality
   - Add advanced examples and guides

3. **Team Enablement**
   - Advanced training on tools and processes
   - Establish communities of practice
   - Create internal best practices guide

## Risk Assessment

### High Risks
1. **Team Resistance to Change**
   - **Mitigation**: Gradual adoption, training, show benefits
   - **Contingency**: Executive sponsorship, change management

2. **Technical Debt Blocking Progress**
   - **Mitigation**: Prioritize refactoring, incremental improvement
   - **Contingency**: Parallel development of new components

3. **Resource Constraints**
   - **Mitigation**: Phase implementation, leverage automation
   - **Contingency**: Extend timeline, reduce scope

### Medium Risks
- Integration complexity with existing systems
- Learning curve for new tools and processes
- Maintaining momentum through long migration

### Low Risks
- Tool compatibility issues
- Documentation maintenance overhead
- Performance impact of new processes

## Success Metrics

### Compliance Metrics
- **Overall compliance score**: Target 90%+ within 10 weeks
- **Phase completion**: All 7 phases documented and operational
- **Traceability coverage**: 85%+ forward and backward links

### Quality Metrics
- **Test coverage**: 80%+ within 8 weeks
- **Defect density**: <1 defect per 1000 lines of code
- **Security vulnerabilities**: Zero high/critical issues

### Process Metrics
- **Build success rate**: 95%+ automated builds pass
- **Deployment frequency**: Weekly releases achievable
- **Lead time**: 50% reduction in feature delivery time

## Recommendations

### Immediate Actions (This Week)
1. Set up basic repository structure
2. Copy essential prompts from template
3. Begin stakeholder requirements gathering
4. Establish project communication plan

### Short Term (Next Month)
1. Complete Phase 1 migration activities
2. Begin Phase 2 requirements and architecture work
3. Train core team on spec-driven development
4. Establish regular progress reviews

### Long Term (Next Quarter)
1. Complete full migration to spec-driven development
2. Measure and optimize new processes
3. Share learnings and best practices
4. Consider expanding to other projects

## Conclusion

**Migration Feasibility**: [HIGH 🟢 / MEDIUM 🟡 / LOW 🔴]

**Overall Assessment**: [Summary of readiness and recommended approach]

**Expected Benefits**:
- Improved software quality and reliability
- Faster development through better requirements
- Reduced rework and defects
- Better compliance with industry standards
- Enhanced team productivity and satisfaction

**Investment Required**: [X] weeks of effort over [Y] weeks timeline
**Expected ROI**: [Benefits vs. costs analysis]

**Recommendation**: [PROCEED / PROCEED WITH MODIFICATIONS / DEFER]
```

## 🚀 Usage

### Full Repository Audit:
```bash
/repository-audit.prompt.md Please perform a comprehensive audit of this repository against the spec-driven development template.

Analyze:
- Repository structure and organization
- Documentation completeness across all phases
- Code quality and test coverage
- Process compliance and automation
- Traceability between artifacts

Generate migration roadmap with effort estimates.
```

### Focused Assessment:
```bash
# Audit specific aspect
/repository-audit.prompt.md Audit our requirements documentation. 
How does it compare to ISO 29148 standards?

# Check specific phase
/repository-audit.prompt.md Assess our architecture documentation completeness. 
What C4 diagrams and ADRs are missing?

# Evaluate process maturity
/repository-audit.prompt.md Evaluate our CI/CD pipeline against spec-driven development best practices.
```

### Migration Planning:
```bash
/repository-audit.prompt.md Based on current repository state, create a 3-month migration plan to adopt spec-driven development with realistic effort estimates and risk mitigation.
```

## 📈 Audit Automation

### Automated Checks:
```bash
# Structure analysis
find docs/ -type d | sort

# Documentation completeness
find docs/ -name "*.md" -exec wc -l {} +

# Test coverage analysis  
npm run test:coverage || pytest --cov || mvn test jacoco:report

# Security scanning
npm audit --audit-level=high || safety check || snyk test

# Code quality
npm run lint || flake8 || checkstyle
```

### Continuous Monitoring:
- Set up monthly automated audits
- Track compliance score trends
- Monitor migration progress
- Alert on regression in key metrics

---

**Know where you stand, plan where you're going!** 📊