# AI Model Adaptation Protocol

## Model Detection Instructions
Add this section to the beginning of every agent file:

### AI Environment Detection
Before executing any agent instructions, detect the AI environment:

```bash
# Detect AI model environment
if [[ "$CLAUDE_CODE_DETECTED" == "true" ]] || command -v claude-code >/dev/null 2>&1; then
    AI_ENVIRONMENT="claude-code"
    PARALLEL_CAPABLE="true"
    MAX_CONTEXT_TOKENS="200000"
elif [[ "$CLINE_DETECTED" == "true" ]] || [[ -f ".clinerules" ]]; then
    AI_ENVIRONMENT="cline"  
    PARALLEL_CAPABLE="false"
    MAX_CONTEXT_TOKENS="128000"
else
    AI_ENVIRONMENT="generic"
    PARALLEL_CAPABLE="false" 
    MAX_CONTEXT_TOKENS="8000"
fi
```

## Model-Specific Instruction Adaptations

### For Claude Code (Parallel Processing)
```markdown
**IF AI_ENVIRONMENT="claude-code":**
- Use parallel Task tool execution for analysis phases
- Launch multiple analysis tasks simultaneously  
- Optimize for 200K token context window
- Enable automatic progress tracking across parallel tasks
- Use batch processing for file analysis
```

### For Cline (Sequential Processing)  
```markdown
**IF AI_ENVIRONMENT="cline":**
- Execute phases sequentially with user approval
- Provide detailed progress updates between phases
- Optimize for 128K token context window
- Enable resume capability at any phase
- Use checkpoint-based state management
```

### For Generic AI (Conservative Mode)
```markdown
**IF AI_ENVIRONMENT="generic":**
- Execute minimal viable analysis only
- Focus on critical findings only (security, build failures)
- Optimize for 8K token context window  
- Use aggressive summarization
- Prioritize actionable findings over comprehensive analysis
```

## Token Allocation Strategies

### Context Window Management
```yaml
# Claude Code (200K tokens)
token_allocation:
  codebase_context: 80000      # 40%
  analysis_instructions: 40000  # 20% 
  generated_content: 60000     # 30%
  safety_buffer: 20000         # 10%

# Cline (128K tokens)  
token_allocation:
  codebase_context: 50000      # 39%
  analysis_instructions: 25000  # 20%
  generated_content: 38000     # 30%
  safety_buffer: 15000         # 11%

# Generic AI (8K tokens)
token_allocation:
  codebase_context: 3000       # 37%
  analysis_instructions: 1500   # 19%
  generated_content: 2500      # 31%
  safety_buffer: 1000          # 13%
```

## Prompt Optimization Rules

### Model-Specific Formatting
```markdown
**For Claude Code:**
- Use structured headings and bullet points
- Include explicit parallel execution instructions
- Provide comprehensive context upfront
- Use tool-calling syntax optimization

**For Cline:**
- Use conversational, step-by-step instructions
- Include explicit user interaction points  
- Provide context incrementally
- Use resume/continue prompts

**For Generic AI:**
- Use simple, direct instructions only
- Minimize context and focus on essentials
- Use basic markdown formatting only
- Avoid complex multi-step workflows
```

## Agent Template Integration

### Standard Addition to Agent Files
Add this section after the frontmatter in every agent file:

```markdown
### AI Environment Adaptation
**CRITICAL: Execute environment detection before proceeding with agent instructions.**

1. **Detect AI environment** using model_adaptation.md protocol
2. **Apply appropriate token allocation** based on detected environment  
3. **Use model-specific instruction format** for optimal performance
4. **Adjust analysis depth** based on context window limitations

**Environment-Specific Behavior**:
- **Claude Code**: {{instructions_for_claude_code}}
- **Cline**: {{instructions_for_cline}}  
- **Generic**: {{instructions_for_generic}}
```

## Context Optimization by Model

### Claude Code Optimizations
- **Batch Processing**: Group similar operations for parallel execution
- **Rich Context**: Include comprehensive background information
- **Tool Chaining**: Use multiple tools in sequence for complex operations
- **Structured Output**: Use consistent formatting for better parsing

### Cline Optimizations  
- **Incremental Delivery**: Break large tasks into user-approved chunks
- **Progress Indicators**: Show clear progress throughout execution
- **Resumable State**: Design workflows that can be paused and resumed
- **User Guidance**: Provide clear next steps for user interaction

### Generic AI Optimizations
- **Minimal Context**: Focus only on essential information
- **Simple Instructions**: Avoid complex multi-step procedures
- **Conservative Scope**: Limit analysis to critical components only
- **Direct Output**: Minimize formatting and focus on content

## Implementation Guidelines

### Configuration Integration
Add to `coacoa.yaml`:

```yaml
# AI Model Adaptation Settings
ai_adaptation:
  auto_detect_environment: true       # Automatically detect Claude Code vs Cline
  token_allocation_strategy: "adaptive" # adaptive|conservative|aggressive
  model_specific_formatting: true     # Use model-optimized prompt formats
  fallback_mode: "generic"           # Fallback when detection fails
  
  # Token limits by environment
  token_limits:
    claude_code: 200000
    cline: 128000
    generic: 8000
```

### Quality Assurance
- **Test across environments**: Verify workflows work in Claude Code, Cline, and generic AI
- **Monitor token usage**: Track actual vs allocated token consumption
- **Validate outputs**: Ensure quality doesn't degrade in constrained environments
- **Document limitations**: Clearly state what's not supported in each environment

This adaptation protocol ensures CoaCoA works optimally across different AI environments while maintaining consistent functionality and quality standards.