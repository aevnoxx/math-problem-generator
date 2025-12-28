# Math Problem Generator

![Tests](https://img.shields.io/github/actions/workflow/status/aevnoxx/math-problem-generator/ci-cd.yml?branch=main&label=tests)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A powerful tool for automatically generating calculus problems with step-by-step solutions. Perfect for educators, students, and anyone learning or teaching mathematics.

## 🎯 Description

This project generates mathematical problems in three categories:
- **Derivatives** - Find derivatives of various functions
- **Integrals** - Calculate indefinite integrals
- **Limits** - Evaluate limits at different points

Each problem includes:
- Original function in both text and LaTeX format
- Complete solution
- Step-by-step explanation
- Adjustable difficulty levels (easy, medium, hard)

## ✨ Features

- 📊 **Multiple Problem Types**: Derivatives, integrals, and limits
- 🎚️ **Difficulty Levels**: Easy, medium, and hard problems
- 📝 **Multiple Export Formats**: Markdown, LaTeX, plain text, and JSON
- 🔄 **Reproducible Results**: Use seed parameter for consistent problem sets
- 🤖 **Automated Weekly Generation**: GitHub Actions automatically generates problem sets
- ✅ **Well-Tested**: Comprehensive test suite with >90% coverage

## 📦 Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/aevnoxx/math-problem-generator.git
cd math-problem-generator
```

2. Create and activate virtual environment:
```bash
python -m venv venv

# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Basic Usage

Generate 5 random problems with default settings:
```bash
python main.py
```

### Custom Problem Generation

Generate 10 medium-difficulty problems and save to file:
```bash
python main.py -n 10 -d medium -o problems.md
```

Generate only derivative problems:
```bash
python main.py -n 5 -t derivative -o derivatives.md
```

Generate hard problems in LaTeX format:
```bash
python main.py -n 8 -d hard -f latex -o homework.tex
```

Use seed for reproducible results:
```bash
python main.py -n 5 -s 42 -o reproducible.md
```

### Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-n`, `--count` | Number of problems to generate | 5 |
| `-d`, `--difficulty` | Difficulty level (easy/medium/hard) | medium |
| `-t`, `--types` | Problem types (derivative/integral/limit) | all types |
| `-f`, `--format` | Output format (markdown/latex/text/json) | markdown |
| `-o`, `--output` | Output file path | stdout |
| `-s`, `--seed` | Random seed for reproducibility | random |
| `--title` | Title for the problem set | "Math Problem Set" |

## 📖 Example Output

### Markdown Format

```markdown
# Math Problem Set

*Generated on: 2025-12-28 14:30*

---

## Problem 1

**Type:** Derivative  
**Difficulty:** Medium  

Find the derivative of:

$$f(x) = x^2 + 2x\sin(x)$$

### Solution

$$2x + 2\sin(x) + 2x\cos(x)$$

### Steps

- Given function: f(x) = x**2 + 2*x*sin(x)
- Apply derivative rules:
- Derivative of sin(x) is cos(x)
- Result: f'(x) = 2*x + 2*sin(x) + 2*x*cos(x)

---
```

## 🏗️ Project Structure

```
math-problem-generator/
├── src/                      # Source code
│   ├── __init__.py
│   ├── generator.py         # Problem generation logic
│   └── exporter.py          # Export to different formats
├── tests/                   # Unit tests
│   ├── __init__.py
│   ├── test_generator.py   # Generator tests
│   └── test_exporter.py    # Exporter tests
├── examples/                # Example outputs and generated sets
├── data/                    # Generated problem sets in JSON
├── docs/                    # Additional documentation
├── .github/workflows/       # CI/CD automation
│   └── ci-cd.yml           # GitHub Actions workflow
├── main.py                 # CLI entry point
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md
```

## 🤖 Automated Problem Generation

This project includes advanced CI/CD automation using GitHub Actions:

### Weekly Automatic Generation
- **Schedule**: Every Monday at 9:00 AM UTC
- **Output**: Generates 10 medium-difficulty problems
- **Formats**: Markdown, LaTeX, and JSON
- **Auto-commit**: Results are automatically committed to the repository

### Manual Generation
You can manually trigger problem generation:
1. Go to "Actions" tab in GitHub
2. Select "Tests and Weekly Problem Generation" workflow
3. Click "Run workflow"
4. Specify custom parameters (count, difficulty)

### Artifacts
Generated problem sets are stored as artifacts for 90 days and can be downloaded from the Actions page.

## 🧪 Testing

Run all tests:
```bash
pytest
```

Run with coverage report:
```bash
pytest --cov=src tests/
```

Run with verbose output:
```bash
pytest -v
```

## 🛠️ Development

### Code Quality

Check code style:
```bash
flake8 src tests main.py
```

Format code:
```bash
black src tests main.py
```

### Running Tests Locally
```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
pytest tests/ -v --cov=src
```

## 📊 Use Cases

### For Educators
- Generate unique problem sets for homework assignments
- Create practice exams with solutions
- Prepare tutorial materials with step-by-step solutions

### For Students
- Practice calculus problems at your own pace
- Study solution steps to understand techniques
- Generate custom problem sets for self-study

### For Tutors
- Create personalized problem sets for students
- Export to professional LaTeX documents
- Track problem difficulty progression

## 🔧 Technical Details

### Dependencies
- **SymPy** (≥1.12): Symbolic mathematics
- **NumPy** (≥1.24.0): Numerical computations
- **pytest** (≥7.4.0): Testing framework
- **flake8** (≥6.1.0): Code linting
- **black** (≥23.0.0): Code formatting

### Algorithm
The generator uses SymPy's symbolic computation engine to:
1. Generate random mathematical expressions
2. Compute derivatives/integrals/limits symbolically
3. Format results in multiple output formats
4. Create step-by-step solution explanations

## 🤝 Contributing

Contributions are welcome! Please feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is licensed under the MIT License.

## 👤 Author

Razuvaev Maksim

## 🙏 Acknowledgments

- Built with [SymPy](https://www.sympy.org/) for symbolic mathematics
- Inspired by the need for automated educational content generation
- Thanks to the open-source community for excellent tools and libraries

## 📮 Contact

For questions or suggestions, please open an issue on GitHub.

---

**Note**: Generated problem sets are automatically created weekly and stored in the `examples/` directory. Check the [Actions](https://github.com/aevnoxx/math-problem-generator/actions) tab for the latest generated sets.
