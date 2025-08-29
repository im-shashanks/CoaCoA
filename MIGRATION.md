# CoaCoA Migration Guide: Legacy to Unified Analysis Workflow

## Overview

CoaCoA v2.0 introduces a **unified codebase analysis workflow** that replaces the previous separate workflows for Claude Code and Cline. This migration guide helps users transition from the legacy system to the new unified approach.

---

## What Changed

### Before (Legacy System)
- **Separate workflows**: Different tasks for `claude-code` and `cline` 
- **Complex task orchestration**: Multiple templates and context transfers
- **Batch-based processing**: Required prep steps and state management
- **Limited enterprise support**: Basic analysis with separate consolidation

### After (Unified System)  
- **Single command**: `/codebase-detection` works for both IDEs
- **Planning-first approach**: All intelligence front-loaded into comprehensive plan
- **Self-contained tasks**: No complex context transfers between tasks
- **Enterprise-grade analysis**: 8-phase comprehensive analysis with executive reporting

---

## Migration Impact

### ✅ What Still Works
- **All slash commands remain the same**: `/codebase-detection` command unchanged  
- **Configuration compatibility**: Existing `coacoa.yaml` settings preserved
- **Quality gates**: All existing quality validation continues to work
- **Output location**: Analysis results still in `coacoa/context/` directory
- **Agent specifications**: All agent roles and capabilities unchanged

### 📁 Directory Structure Changes
**Old Structure:**
```
coacoa/context/
├── analysis.md                    # Single analysis document
└── intelligence/                  # Batch-generated JSON files
    ├── batch_1_module_map.json
    ├── batch_2_dep_graph.json
    └── ...
```

**New Structure:**
```
coacoa/context/analysis/           # Unified analysis directory
├── plan.md                       # Master plan with progress tracking
├── artifacts/                    # Schema-validated JSON intelligence  
│   ├── repo-intelligence.json
│   ├── build-info.json
│   ├── architecture.json
│   ├── complexity.json
│   ├── security-analysis.json
│   ├── git-analysis.json
│   └── performance-analysis.json
├── reports/                      # Individual phase reports
│   ├── task-001-analysis.md
│   └── ...
└── consolidated/                 # Executive outputs
    ├── executive-summary.md
    └── recommendations.md
```

### 🗑️ Removed Files
The following files have been removed as they are no longer needed:
- `tasks/analyze_codebase_cline.md`
- `tasks/analyze_codebase_parallel.md` 
- `tasks/prep_codebase_analysis.md`
- `tasks/consolidate_analysis.md`

---

## Migration Steps

### 1. For Existing Projects (No Action Required)

**The unified workflow is backward compatible.** Your existing projects will automatically use the new system when you run `/codebase-detection`.

### 2. For Custom Integrations

If you have custom scripts or integrations that reference the removed task files, update them:

**Old Reference:**
```bash
# This will no longer work
coacoa invoke tasks/analyze_codebase_cline.md
```

**New Reference:**  
```bash
# Use the unified task
coacoa invoke tasks/analyze_codebase.md
```

### 3. For Configuration Customizations

The new system adds additional configuration options. Update your `coacoa.yaml`:

```yaml
# NEW: Unified Analysis Configuration (optional)
analysis:
  enterprise_mode: true              # Enable enterprise-specific features  
  unified_workflow: true             # Use new unified analysis workflow
  auto_mode_detection: true          # Automatically detect Claude Code vs Cline
  schema_validation: true            # Validate all artifacts against schemas
  evidence_requirement: true         # Require evidence-based findings only
  parallel_task_limit: 8             # Max parallel tasks for Claude Code mode
```

### 4. Clean Up Old Output (Optional)

If you want to clean up old analysis outputs:

```bash
# Remove old batch-style outputs (optional)
rm -rf coacoa/context/analysis_*.md
rm -rf coacoa/context/intelligence/batch_*
rm -f coacoa/context/analysis_state.json

# The new unified workflow will create fresh outputs
```

---

## Feature Comparison

| Feature | Legacy System | Unified System |
|---------|---------------|----------------|
| **Command** | `/codebase-detection` | `/codebase-detection` ✅ Same |
| **IDE Support** | Separate workflows | Unified with auto-detection |
| **Planning** | Basic scope detection | Comprehensive upfront planning |
| **Task Management** | Complex context transfers | Self-contained tasks |
| **Progress Tracking** | Basic batch counting | Real-time phase progress |
| **Enterprise Features** | Limited | Full enterprise support |
| **Error Handling** | Basic recovery | Comprehensive error handling |
| **Executive Reporting** | Manual consolidation | Auto-generated summaries |
| **Schema Validation** | None | Built-in JSON validation |
| **Evidence Requirements** | Optional | Mandatory (no hallucinations) |

---

## New Capabilities

### 🚀 Enhanced Analysis Features
1. **Security & Compliance Analysis**: Built-in CVE scanning and license validation
2. **Enterprise Build System Support**: Bazel, Buck, Rush, Nx detection  
3. **Git History Risk Analysis**: Team collaboration patterns and knowledge risks
4. **Performance Bottleneck Detection**: Algorithmic complexity analysis
5. **Executive Dashboard**: Risk-prioritized findings with actionable recommendations

### 🔧 Improved Developer Experience  
1. **Automatic Mode Detection**: No need to specify Claude Code vs Cline workflows
2. **Progress Visibility**: Real-time updates on analysis progress
3. **Graceful Degradation**: Partial results when full analysis cannot complete
4. **Evidence-Based Findings**: All claims supported by actual code analysis
5. **Schema-Driven Validation**: Ensures consistent, reliable output format

---

## Troubleshooting

### Common Migration Issues

#### Issue: "Task file not found" error
```bash
Error: Cannot find tasks/analyze_codebase_cline.md
```
**Solution**: The legacy task files were removed. Use `/codebase-detection` which now handles both Claude Code and Cline automatically.

#### Issue: Old analysis outputs remain
```bash  
# Old files still present in coacoa/context/
```
**Solution**: This is normal. New analysis outputs will be created in the new directory structure. Old files can be safely removed.

#### Issue: Configuration errors after migration
```bash
Error: Unknown configuration key 'batch_size'
```  
**Solution**: Some legacy configuration keys are no longer used. Remove them or refer to the new configuration options above.

### Getting Help

If you encounter migration issues:

1. **Check the error handling guide**: `coacoa/templates/error_handling.md`
2. **Review configuration**: Compare your `coacoa.yaml` with `coacoa/coacoa.yaml` defaults  
3. **Reinstall if needed**: `pip install --force-reinstall git+https://github.com/im-shashanks/CoaCoA.git`
4. **Report issues**: [GitHub Issues](https://github.com/im-shashanks/CoaCoA/issues)

---

## Benefits of Migration

### For Development Teams
- **Simplified Workflow**: Single command for comprehensive analysis
- **Better Insights**: 8-phase enterprise-grade analysis vs basic code scanning
- **Executive Communication**: Ready-to-present executive summaries and recommendations
- **Risk Management**: Prioritized findings help focus improvement efforts

### For Enterprise Users  
- **Compliance Ready**: Built-in security scanning and license validation
- **Scalable Architecture**: Handles massive codebases with intelligent token management  
- **Evidence-Based Reports**: No hallucinated findings, all claims verifiable
- **Integration Friendly**: Consistent JSON schemas for tool integration

### For AI IDE Users
- **Tool Agnostic**: Same workflow whether using Claude Code or Cline
- **Optimized Execution**: Parallel processing (Claude Code) vs user-controlled sequential (Cline)
- **Better Error Handling**: Graceful degradation and clear recovery guidance
- **Progress Visibility**: Real-time updates on analysis progress

---

## Rollback (If Needed)

If you need to temporarily rollback to legacy behavior:

1. **Disable unified workflow**: Set `analysis.unified_workflow: false` in `coacoa.yaml`
2. **Use git to restore**: `git checkout HEAD~1 -- coacoa/` (if you have git history)
3. **Manual recreation**: Recreate the removed task files from git history if needed

**Note**: Rollback is not recommended as the legacy system lacks enterprise features and will not receive updates.

---

## Next Steps

1. ✅ **Try the new workflow**: Run `/codebase-detection` on a test project
2. ✅ **Review executive summaries**: Check the new consolidated reporting format  
3. ✅ **Update documentation**: Update any internal documentation referencing old workflows
4. ✅ **Train team**: Share this migration guide with your development team
5. ✅ **Provide feedback**: Report any issues or suggestions for improvement

**The unified workflow represents a major advancement in CoaCoA's capabilities. The migration is designed to be seamless while providing significant new value for enterprise development teams.**