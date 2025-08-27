<p align="center">
  <img src=".github/banner/CoaCoALogo.png" alt="CoaCoA logo" width="150">
</p>

<p align="center">
  <a href="https://pypi.org/project/coacoa/">
    <img src="https://img.shields.io/pypi/v/coacoa.svg?color=blue&logo=pypi&label=PyPI%20Version" alt="PyPI">
  </a>
  <a href="https://github.com/im-shashanks/coacoa/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache--2.0-green.svg" alt="License">
  </a>
  <a href="https://github.com/im-shashanks/CoaCoA/actions/workflows/ci.yml">
  <img
    src="https://img.shields.io/github/actions/workflow/status/im-shashanks/CoaCoA/ci.yml?branch=main&label=CI%20build"
    alt="CI build status"
  >
    </a>
  <a href="https://codecov.io/gh/im-shashanks/CoaCoA">
    <img src=".github/assets/coverage.svg" alt="coverage">
  </a>
</p>

<h1 align="center">CoaCoA</h1>
<p align="center"><strong>Context-Optimised Agentic Coding Assistant</strong></p>
<p align="center">
  <em>An enterprise-grade AI-powered development framework that transforms how teams build, test, and ship software</em>
</p>

---

## Overview

CoaCoA is a production-ready framework that integrates AI agents into your development workflow to deliver high-quality, tested code with enterprise-grade compliance. Built for teams who demand reliability, quality, and speed.

### Key Benefits

- **Zero Broken Builds**: Comprehensive quality gates ensure code passes tests, lint, and coverage requirements
- **Enterprise Compliance**: Human-controlled commits with staged changes for audit and review processes
- **Intelligent Automation**: 12 specialized AI agents handle everything from architecture to QA
- **Legacy Integration**: Seamlessly analyze and enhance existing codebases with automated dependency mapping
- **Quality Assurance**: Maintains 90%+ test coverage with anti-hallucination checks

---

## Quick Start

### Installation

```bash
pip install git+https://github.com/im-shashanks/CoaCoA.git
```

> **Note**: CoaCoA is currently in public beta. Installing from git ensures you get the latest features and fixes.

### Initialize Your Project

```bash
# Navigate to your project directory
cd your-project

# Initialize CoaCoA framework
coacoa init --claude-code  # For Claude Code IDE
# or
coacoa init --cline        # For Cline IDE

# Commit the framework setup
git add . && git commit -m "Add CoaCoA framework"
```

### Choose Your Workflow

#### New Projects (Greenfield)
Start with an idea and build a complete application:

```text
/analyst init "Real-time expense tracker for remote teams"
/pm new-prd
/ux-designer make-ui
/architect finalize-arch
/orchestrator run
```

#### Existing Projects (Brownfield)
Enhance existing codebases with intelligent analysis:

```text
/analyze-codebase
/pm new-prd
/architect finalize-arch
/orchestrator run
```

---

## Architecture

### Multi-Agent System

CoaCoA employs 12 specialized AI agents, each with distinct responsibilities:

| Agent | Role | Purpose |
|-------|------|---------|
| **Analyst** | Requirements Gathering | Converts ideas into detailed domain specifications |
| **Product Manager** | Strategy & Planning | Creates PRDs and defines feature requirements |
| **UX Designer** | User Experience | Designs interfaces and accessibility guidelines |
| **Product Owner** | Backlog Management | Prioritizes features and manages epic dependencies |
| **Architect** | System Design | Creates technical architecture and design decisions |
| **Scrum Master** | Project Management | Breaks epics into implementable stories |
| **Developer** | Implementation | Writes code following TDD practices with >90% coverage |
| **QA Engineer** | Quality Assurance | Validates implementations against requirements |
| **Code Explorer** | Analysis | Performs deep codebase analysis and intelligence gathering |
| **Orchestrator** | Workflow Management | Coordinates multi-agent workflows and ensures quality gates |

### Quality Framework

CoaCoA implements five comprehensive quality gates:

1. **Build Integrity**: Ensures all code compiles, tests pass, and linting requirements are met
2. **Anti-Hallucination**: Validates symbol names, paths, and API references for accuracy
3. **Architecture Integrity**: Prevents dependency cycles and enforces design principles
4. **Link Integrity**: Verifies all file references and documentation links
5. **QA Compliance**: Confirms requirements are met and edge cases are handled

---

## Project Structure

After initialization, CoaCoA creates the following structure:

```
your-project/
├── coacoa/                          # CoaCoA framework (add to .gitignore)
│   ├── coacoa.yaml                  # Configuration settings
│   ├── agents/                      # AI agent specifications
│   ├── tasks/                       # Step-by-step workflows
│   ├── templates/                   # Document templates (PRD, ADR, etc.)
│   ├── quality/                     # Quality gate checklists
│   ├── workflows/                   # Greenfield and brownfield workflows
│   └── context/                     # Generated analysis artifacts
├── CLAUDE.md                        # Claude Code command reference
├── .clinerules/                     # Cline IDE integration
└── coacoa.yaml                      # Project-specific overrides (optional)
```

---

## Configuration

### Default Configuration

CoaCoA uses a hierarchical configuration system:

- **Base configuration**: `coacoa/coacoa.yaml` (framework defaults)
- **Project overrides**: `coacoa.yaml` in your project root (optional)

### Key Configuration Options

```yaml
paths:                                # Artifact locations
  analysis: coacoa/context/analysis.md
  module_map: coacoa/context/intelligence/module_map.json
  build_info: coacoa/context/intelligence/build_info.json

limits:                               # Resource constraints
  max_snippet_loc: 120               # Lines of code per context window
  max_tokens_context: 12000          # Token budget for AI operations

quality:                             # Quality assurance settings
  anti_hallucination: coacoa/quality/anti_hallucination.md
  build_integrity: coacoa/quality/build_integrity.md

workflows:                           # Workflow definitions
  greenfield: coacoa/workflows/default_greenfield.yml
  brownfield: coacoa/workflows/default_brownfield.yml
```

---

## Command Reference

### IDE Integration

CoaCoA integrates seamlessly with AI-powered IDEs through slash commands:

| Command | Purpose | Use Case |
|---------|---------|----------|
| `/analyze-codebase` | Deep codebase analysis | Initial brownfield setup |
| `/analyst init "<idea>"` | Start requirement gathering | New project initialization |
| `/pm new-prd` | Generate product requirements | Define project scope |
| `/ux-designer make-ui` | Create UX specifications | Design user interfaces |
| `/po refine-epics` | Prioritize features | Backlog management |
| `/architect finalize-arch` | Design system architecture | Technical planning |
| `/scrum-master create` | Break down work items | Sprint planning |
| `/dev implement <story>` | Code implementation | Feature development |
| `/qa review` | Quality validation | Testing and verification |
| `/orchestrator run` | Automated workflow execution | End-to-end development |

### CLI Commands

```bash
# Get help
coacoa --help
coacoa init --help

# Initialize with IDE support
coacoa init --claude-code    # For Claude Code
coacoa init --cline         # For Cline

# Check version
coacoa version
```

---

## Workflows

### Greenfield Development

Build new applications from concept to production:

1. **Requirements Analysis**: Gather and refine requirements through AI-guided questioning
2. **Product Planning**: Generate comprehensive PRDs with measurable goals
3. **UX Design**: Create user interface specifications and accessibility guidelines
4. **Architecture Design**: Design system architecture with decision records
5. **Implementation**: Develop features with test-driven development
6. **Quality Assurance**: Validate implementations against requirements
7. **Deployment**: Stage changes for human review and approval

### Brownfield Enhancement

Modernize and enhance existing codebases:

1. **Codebase Analysis**: Automated analysis of code structure, dependencies, and complexity
2. **Technical Debt Assessment**: Identify hotspots, cycles, and improvement opportunities
3. **Architecture Alignment**: Create PRDs that align with existing system structure
4. **Incremental Enhancement**: Implement improvements without breaking existing functionality
5. **Quality Gates**: Ensure all changes meet enterprise standards

---

## Enterprise Features

### Compliance & Governance

- **Human-Controlled Commits**: All changes are staged but never automatically committed
- **Audit Trail**: Complete history of decisions through Architecture Decision Records (ADRs)
- **Quality Enforcement**: Mandatory quality gates prevent substandard code from progressing
- **Dependency Management**: Automated analysis and management of project dependencies

### Scalability & Performance

- **Token-Aware Processing**: Intelligent chunking prevents context overflow
- **Parallel Processing**: Concurrent analysis for large codebases
- **Incremental Updates**: Only processes changed components
- **Configurable Limits**: Adjustable resource constraints for different team sizes

### Integration Capabilities

- **Multi-IDE Support**: Claude Code and Cline integration out of the box
- **Version Control**: Git-native workflow with branch-per-feature development
- **Build System Detection**: Automatic detection of Maven, Gradle, NPM, Python, and other ecosystems
- **Testing Framework Integration**: Seamless integration with existing test suites

---

## FAQ

**Q: Why doesn't CoaCoA auto-commit changes?**
A: Enterprise compliance often requires human review and sign-off. CoaCoA stages all changes but leaves final commits to developers, ensuring proper audit trails and approval processes.

**Q: How does CoaCoA prevent context bloat with large projects?**
A: CoaCoA uses intelligent context management with configurable token limits (default: 12,000 tokens) and line-of-code constraints (default: 120 LOC per snippet). Large codebases are referenced by path rather than content.

**Q: Can I customize the quality requirements?**
A: Yes, all quality gates are configurable through the `coacoa.yaml` file. You can adjust coverage thresholds, add custom checklists, and modify workflow steps to match your team's standards.

**Q: Is CoaCoA suitable for large enterprises?**
A: CoaCoA is designed with enterprise requirements in mind, including human oversight, comprehensive auditing, quality enforcement, and compliance features required by large organizations.

**Q: How does CoaCoA handle existing code standards?**
A: CoaCoA analyzes existing codebases to understand patterns, conventions, and architectural decisions, then ensures all new code follows established practices while suggesting improvements where appropriate.

---

## Contributing

We welcome contributions from the community. To get started:

1. **Fork** the repository and create a feature branch
2. **Test** your changes using `/orchestrator run` on sample projects  
3. **Ensure** all quality gates pass before submitting
4. **Submit** a pull request with appropriate documentation

For major architectural changes, please create an Architecture Decision Record (ADR) as part of your submission.

---

## License

CoaCoA is licensed under the Apache-2.0 License. See [LICENSE](LICENSE) for details.

---

## Support

- **Documentation**: [CoaCoA Docs](https://docs.anthropic.com/en/docs/claude-code/)
- **Issues**: [GitHub Issues](https://github.com/im-shashanks/CoaCoA/issues)
- **Discussions**: [GitHub Discussions](https://github.com/im-shashanks/CoaCoA/discussions)

---

<p align="center">
  <strong>Ready to transform your development workflow?</strong><br>
  <code>pip install git+https://github.com/im-shashanks/CoaCoA.git && coacoa init</code>
</p>