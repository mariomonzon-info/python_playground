# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a Python learning playground repository containing numbered educational Python scripts organized sequentially by topic. The repository serves as a structured environment for learning Python fundamentals through hands-on examples and exercises.

## Architecture and Structure

- **Sequential Learning Pattern**: Files are numbered sequentially (00-, 01-, 02-, etc.) to indicate learning progression
- **Topic-based Organization**: Each file focuses on a specific Python concept or feature
- **Minimal Dependencies**: Pure Python scripts with no external dependencies, using only the standard library

## Common Commands

### Running Scripts
```bash
# Run a specific Python script
python3 00-hello.py

# Run any numbered script by replacing the filename
python3 01-variables.py
python3 02-operators.py
python3 03-strings.py
```

### Development Workflow
```bash
# Create a new learning script (follow naming convention)
touch 04-new-topic.py

# Check Python version in use
python3 --version

# Run all Python files in order (for testing progression)
for file in [0-9][0-9]-*.py; do echo "=== Running $file ==="; python3 "$file"; echo; done
```

### Testing and Validation
```bash
# Check syntax of all Python files
python3 -m py_compile *.py

# Run a script with verbose output for debugging
python3 -v script-name.py

# Check for basic syntax errors across all files
find . -name "*.py" -exec python3 -m py_compile {} \;
```

## Development Environment

- **Python Version**: Python 3.10.12 (system default)
- **No Virtual Environment**: Uses system Python installation
- **No Package Manager**: Pure Python standard library only
- **Git Tracking**: Repository is version controlled with Git

## File Naming Convention

Files follow a strict naming pattern:
- Format: `NN-topic-name.py` where NN is a zero-padded number
- Numbers indicate learning sequence and should be consecutive
- Topic names should be descriptive and use hyphens for spaces
- Examples: `00-hello.py`, `01-variables.py`, `02-operators.py`

## Code Style Guidelines

Since this is a learning repository:
- Focus on clarity and educational value over optimization
- Include comments explaining concepts where helpful
- Keep examples simple and focused on the specific topic
- One main concept per file to maintain clear learning progression

## Working with This Repository

1. **Adding New Topics**: Create new files following the numbering sequence
2. **Modifying Examples**: Edit existing files to improve or expand examples
3. **Testing Changes**: Run individual scripts to verify they work as expected
4. **Sequential Learning**: Work through files in numerical order for structured learning

## Python Environment Notes

- Uses system Python 3.10.12 installation
- No virtual environment required for this simple setup
- Standard library imports only (no pip installations needed)
- Compatible with any Python 3.6+ environment
